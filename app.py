from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import json
import sys
sys.path.insert(1, 'C:\\Users\\nguyenco\\cfb\\ML_CollegeFootball\\src')
from getrankings import get_team_ranking
from apirandomforest import get_prediction
from getsingleteamrank import get_solo_team_rank

app = Flask(__name__)
CORS(app)
api = Api(app)

class Predict(Resource):
    def get(self, week):
        parser = reqparse.RequestParser()
        parser.add_argument("away")
        parser.add_argument("home")
        args = parser.parse_args()
        away_prob, home_prob = get_prediction(get_team_ranking(week,args["away"],args["home"]))[0][0], get_prediction(get_team_ranking(week,args["away"],args["home"]))[0][1]
        away_prob, home_prob = round(away_prob, 5), round(home_prob, 5)
        return json.dumps([away_prob, home_prob])
        # [away rank],[away offense],[away defense],[away pass O],[away pass D],[away rush O],[away rush D],[away num games]

        # [home rank],[home offense],[home defense],[home pass O],[home pass D],[home rush O],[home rush D],[home num games]
api.add_resource(Predict, "/predict/<int:week>")

class Rank(Resource):
    def get(self, week):
        parser = reqparse.RequestParser()
        parser.add_argument("teamName")
        args = parser.parse_args()
        team_stats = get_solo_team_rank(week,args["teamName"])
        return json.dumps(team_stats)

api.add_resource(Rank, "/rank/<int:week>")


app.run(host='0.0.0.0', port=8000, debug=True)
