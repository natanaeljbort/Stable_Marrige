# Stable_Marrige (Used on NBA Draft 2020)

## Introduction

The Gale-Shapely Algorithm [1] other known as "Stable Marriage" is an Algorithm that finds a stable set of matches between two equally sized set of elements with each element from both sets giving an order of preference from the values of the other set. In their paper, Gale and shapely demonstrated this algorithm by finding the optimal marriage pairs between a group of men and a group of women hence the famous nickname. By definition: "we call a set of marriages _unstable_ if under the specific marriage is a man and a woman who are not married to each other but prefer each other to their actual mates. [1]"

In this project we will use the real world example of the NBA Draft. For those unfamiliar with the draft, it is held annually by the National Basketball Assiciation where ever team in the league picks the top available player based on their individial preference (need/assesment). Before the draft, well prepared teams have an ordered player list which they start crossing off from after the desired player is no longer available. The team names of this project will all be real and ordered as they will be in the upcoming 2020 draft while the player names were scrapped from nbadraft.net/nba-mock-drafts [2]. For the purpose of this project, we are pretending to have hacked the databases of each teams to get their list of preferences and also hacked each player's agents in order to get the list of the players favorite teams.
  
```python

NBA_Team_List = ['1 New York Knicks', '2 Cleveland Cavs', '3 Phoenix Suns','4 Chicago Bulls','5 Atlanta Hawks','6 Washington Wizards', '7 New_Orleans Pelicans','8 Memphis Grizzlies','9 Dallas Mavs','10 Minnesota Timberwolves''11 LA Lakes','12 Charlotte Hornets', '13 Miami Heat', '14 Sacrameto Kings', '15 Detroit Pistons', '16 Orlando Magic', '17 Brooklyn Nets', '18 Indiana Pacers', '19 San Antonio Spurs', '20 LA Clippers', '21 Oklahoma City', '22 Boston Celtics', '23 Utah Jazz', '24 Philadelphia Sixers', '25 Portland Blazzers', '26 Houston Rockets', '27 Denver Nuggets', '28 GoldenState Warriors', '29 Toronto Raptors', '30 Milwaukee Bucks']
 
Players_List = ['Athony Edwards', 'James Wiseman', 'Jaden McDaniels', 'Cole Anthony', 'LaMelo Ball', 'Vernon Carey', 'Theo Maledon', 'Deni Avdija', 'Nico Mannion', 'Obi Toppin', 'Isaiah Stewart', 'NFaly Dante', 'Zeke Nnaji', 'Tyrese Haliburton', 'Killian Hayes', 'Ochai Agbaji', 'Bryan Antoine', 'Onyeka Okongwu', 'Precious Achiuwa', 'Tyrese Maxey', 'RJ Hampton', 'Jordan Nwora', 'Aaron Henry', 'Steve Enoch', 'Charles Bassey', 'Omer Yurtseven', 'Ashton Hagans', 'Jay Scrubb', 'Tyler Bey', 'Jalen Smith']

```


# References
<p> [1] D. Gale and L.S. Shapley (1962). College Admissions and the Stability of Marriage <br>
&nbsp;&nbsp;&nbsp;&nbsp;<i> Source: The American Mathematical Monthly (pages 9-15) </i> Published by: Mathematical Association of America, Retrieved from: https://www.kaggle.com/datasnaek/youtube-new </p>


<p> [2] Unkown Authors (2019). 2020 Mock Draft <br>
&nbsp;&nbsp;&nbsp;&nbsp;<i> Source: NBADRAFT.NET </i> Published by: Sports Phenoms, Inc., All Rights Reserved, Retrieved from: https://www.nbadraft.net/nba-mock-drafts/ </p>
