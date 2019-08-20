from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import sys
sys.path.insert(1, 'C:\\Users\\nguyenco\\cfb\\ML_CollegeFootball\\src')
from getrankings import get_team_ranking
from apirandomforest import get_prediction

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    def get(self, week):
        parser = reqparse.RequestParser()
        parser.add_argument("away")
        parser.add_argument("home")
        args = parser.parse_args()
        away_prob, home_prob = get_prediction(get_team_ranking(week,args["away"],args["home"]))[0][0], get_prediction(get_team_ranking(week,args["away"],args["home"]))[0][1]
        return json.dumps([away_prob, home_prob])
        # [away rank],[away offense],[away defense],[away pass O],[away pass D],[away rush O],[away rush D],[away num games]

        # [home rank],[home offense],[home defense],[home pass O],[home pass D],[home rush O],[home rush D],[home num games]
api.add_resource(Predict, "/predict/<int:week>")

app.run(debug=True)
