import React, {Component} from 'react';
import { Container, Grid, Image, Menu, Segment, Dropdown, Header, Statistic, Placeholder, Dimmer, Loader} from 'semantic-ui-react'
import './App.css';
import teams from './teamlogos.json'


const weeks = [
  {
    key:'Week 2',
    text:'Week 2',
    value:'2'
  },
  {
    key:'Week 3',
    text:'Week 3',
    value:'3'
  },
  {
    key:'Week 4',
    text:'Week 4',
    value:'4'
  },
  {
    key:'Week 5',
    text:'Week 5',
    value:'5'
  },
  {
    key:'Week 6',
    text:'Week 6',
    value:'6'
  },
  {
    key:'Week 7',
    text:'Week 7',
    value:'7'
  },
  {
    key:'Week 8',
    text:'Week 8',
    value:'8'
  },
  {
    key:'Week 9',
    text:'Week 9',
    value:'9'
  },
  {
    key:'Week 10',
    text:'Week 10',
    value:'10'
  },
  {
    key:'Week 11',
    text:'Week 11',
    value:'11'
  },
  {
    key:'Week 12',
    text:'Week 12',
    value:'12'
  },
  {
    key:'Week 13',
    text:'Week 13',
    value:'13'
  },
]

export default class App extends Component{
  state = {
    awayTeamName: teams[0].text,
    awayTeamImage: teams[0].imgsrc,
    homeTeamName: teams[0].text,
    homeTeamImage: teams[0].imgsrc,
    week: 2,
    awayTeamStats: null,
    homeTeamStats: null,
    resultJson: null
  }

  async componentDidMount(){
    var predictionGet = 'http://localhost:8000/predict/' + this.state.week + '?away=' + this.state.awayTeamName + '&home=' + this.state.homeTeamName
    await fetch(predictionGet, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({resultJson: data})}).catch(console.log)
    var awayRankGet = 'http://localhost:8000/rank/' + this.state.week + '?teamName=' + this.state.awayTeamName
    await fetch(awayRankGet, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({awayTeamStats: JSON.parse(data)})}).catch(console.log)
    var homeRankGet = 'http://localhost:8000/rank/' + this.state.week + '?teamName=' + this.state.homeTeamName
    await fetch(homeRankGet, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({homeTeamStats: JSON.parse(data)})}).catch(console.log)
  }

  awayChange = async (event, {value}) =>{
    this.setState({
      awayTeamName: teams[value].text,
      awayTeamImage: teams[value].imgsrc,
      awayTeamStats: null,
      resultJson: null
    })
    var newurl = 'http://localhost:8000/predict/' + this.state.week + '?away=' + teams[value].text + '&home=' + this.state.homeTeamName
    await fetch(newurl, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({resultJson: data})}).catch(console.log)
    var awayRankGet = 'http://localhost:8000/rank/' + this.state.week + '?teamName=' + teams[value].text
    await fetch(awayRankGet, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({awayTeamStats: JSON.parse(data)})}).catch(console.log)
  }
  homeChange = async (event, {value}) =>{
    this.setState({
      homeTeamName: teams[value].text,
      homeTeamImage: teams[value].imgsrc,
      homeTeamStats: null,
      resultJson: null
    });
    var newurl = 'http://localhost:8000/predict/' + this.state.week + '?away=' + this.state.awayTeamName + '&home=' + teams[value].text
    await fetch(newurl, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({resultJson: data})}).catch(console.log)
    var homeRankGet = 'http://localhost:8000/rank/' + this.state.week + '?teamName=' + teams[value].text
    await fetch(homeRankGet, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({homeTeamStats: JSON.parse(data)})}).catch(console.log)
  }

  weekChange = async (event, {value}) =>{
    this.setState({
      week:value,
      awayTeamStats:null,
      homeTeamStats:null,
      resultJson:null
    })
    var newurl = 'http://localhost:8000/predict/' + value + '?away=' + this.state.awayTeamName + '&home=' + this.state.homeTeamName
    await fetch(newurl, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({resultJson: data})}).catch(console.log)
    var awayRankGet = 'http://localhost:8000/rank/' + value + '?teamName=' + this.state.awayTeamName
    await fetch(awayRankGet, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({awayTeamStats: JSON.parse(data)})}).catch(console.log)
    var homeRankGet = 'http://localhost:8000/rank/' + this.state.week + '?teamName=' + this.state.homeTeamName
    await fetch(homeRankGet, {mode: 'cors'}).then(res => res.json()).then((data) => {this.setState({homeTeamStats: JSON.parse(data)})}).catch(console.log)
  }

  handleItemClick = (e, { name }) => this.setState({activeItem: name})
  render() {
    const {activeItem} = this.state
    return (
        <Container style={{width: '90%'}}>
          <Menu>
            <Menu.Item header>Coulby Nguyen</Menu.Item>
            <Menu.Item
              name='Weekly Matchups'
              active={activeItem === 'weeklyMatchups'}
              onClick={this.handleItemClick}
            />
            <Menu.Item name='Custom Matchups'
              active={activeItem === 'customMatchups'}
              onClick={this.handleItemClick} />
          </Menu>

          <Grid columns='equal'>
            <Grid.Column>
              <Segment>
                <Dropdown placeholder='Select Team' fluid selection search options={teams} value={this.state.value} onChange={this.awayChange}/>
              </Segment>
            </Grid.Column>
            <Grid.Column width={3}>
            <Segment>
              <Dropdown placeholder='Select Week' fluid selection options={weeks} value={this.state.value} onChange={this.weekChange}/>
            </Segment>
            </Grid.Column>
            <Grid.Column>
              <Segment>
                <Dropdown placeholder='Select Team' fluid selection search options={teams} value={this.state.value} onChange={this.homeChange}/>
              </Segment>
            </Grid.Column>
          </Grid>
          <Grid columns='equal'>

            <Grid.Column>
              <Segment>
                <Container style={{marginTop:'50px'}}>
                  <Image className='ui centered image' src={this.state.awayTeamImage} size='small'/>
                </Container>
                <Container style={{marginTop:'25px'}}>
                  <Header textAlign='center' size='huge'>{this.state.awayTeamName}</Header>
                </Container>

                <Container style={{marginTop:'50px'}}>
                  <Statistic.Group widths='3' size='small'>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.awayTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.awayTeamStats[0]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.awayTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Overall Offense</Statistic.Label>
                    </Statistic>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.awayTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.awayTeamStats[1]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.awayTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Overall Defense</Statistic.Label>
                    </Statistic>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.awayTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.awayTeamStats[6]}</Statistic.Value>}
                      {!this.state.awayTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Games Played</Statistic.Label>
                    </Statistic>
                  </Statistic.Group>
                  <Statistic.Group widths='2' size='small'>
                  <Statistic style={{alignItems:'center'}}>
                      {this.state.awayTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.awayTeamStats[2]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.awayTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Pass Offense</Statistic.Label>
                    </Statistic>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.awayTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.awayTeamStats[3]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.awayTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Pass Defense</Statistic.Label>
                    </Statistic>
                  </Statistic.Group>
                  <Statistic.Group widths='2' size='small'>
                  <Statistic style={{alignItems:'center'}}>
                      {this.state.awayTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.awayTeamStats[4]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.awayTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Rush Offense</Statistic.Label>
                    </Statistic>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.awayTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.awayTeamStats[5]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.awayTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Rush Defense</Statistic.Label>
                    </Statistic>
                  </Statistic.Group>
                </Container>
              </Segment>
            </Grid.Column>
            <Grid.Column width={3}>
              <Segment>
              <Container style={{marginTop:'25px'}}>
                <Header textAlign='center' style={{fontSize: '84pt', marginTop:'75px'}}>@</Header>
                <Header textAlign='center' size='tiny'>[% Away Wins, % Home Wins]</Header>
                {this.state.resultJson && <Header textAlign='center' size='tiny'>{this.state.resultJson}</Header>}
                {!this.state.resultJson && <Placeholder><Placeholder.Line/></Placeholder>}

              </Container>
              </Segment>
            </Grid.Column>
            <Grid.Column>
              <Segment>
                <Container style={{marginTop:'50px'}}>
                  <Image className='ui centered image' src={this.state.homeTeamImage} size='small'/>
                </Container>
                <Container style={{marginTop:'25px'}}>
                  <Header textAlign='center' size='huge'>{this.state.homeTeamName}</Header>
                </Container>
                <Container style={{marginTop:'50px'}}>
                  <Statistic.Group widths='3' size='small'>
                  <Statistic style={{alignItems:'center'}}>
                      {this.state.homeTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.homeTeamStats[0]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.homeTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Overall Offense</Statistic.Label>
                    </Statistic>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.homeTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.homeTeamStats[1]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.homeTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Overall Defense</Statistic.Label>
                    </Statistic>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.homeTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.homeTeamStats[6]}</Statistic.Value>}
                      {!this.state.homeTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Games Played</Statistic.Label>
                    </Statistic>
                  </Statistic.Group>
                  <Statistic.Group widths='2' size='small'>
                  <Statistic style={{alignItems:'center'}}>
                      {this.state.homeTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.homeTeamStats[2]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.homeTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Pass Offense</Statistic.Label>
                    </Statistic>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.homeTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.homeTeamStats[3]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.homeTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Pass Defense</Statistic.Label>
                    </Statistic>
                  </Statistic.Group>
                  <Statistic.Group widths='2' size='small'>
                  <Statistic style={{alignItems:'center'}}>
                      {this.state.homeTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.homeTeamStats[4]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.homeTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Rush Offense</Statistic.Label>
                    </Statistic>
                    <Statistic style={{alignItems:'center'}}>
                      {this.state.homeTeamStats && <Statistic.Value style={{display:'flex'}}>{this.state.homeTeamStats[5]}<p style={{fontSize: '12pt', display:'flex'}}>th</p></Statistic.Value>}
                      {!this.state.homeTeamStats && <Placeholder style={{ height: 75, width: 75 }}><Placeholder.Image /></Placeholder>}
                      <Statistic.Label>Rush Defense</Statistic.Label>
                    </Statistic>
                  </Statistic.Group>
                </Container>
              </Segment>
            </Grid.Column>
          </Grid>
        </Container>
    );
  }
}
