"""
Created November 20th 2019

Author: Gael Ruta Gatera

"""
NBA_Team_List = ['1 New York Knicks', '2 Cleveland Cavs', '3 Phoenix Suns','4 Chicago Bulls',
                 '5 Atlanta Hawks','6 Washington Wizards', '7 New_Orleans Pelicans','8 Memphis Grizzlies',
                 '9 Dallas Mavs','10 Minnesota Timberwolves','11 LA Lakes','12 Charlotte Hornets', 
                 '13 Miami Heat', '14 Sacrameto Kings', '15 Detroit Pistons', '16 Orlando Magic', 
                 '17 Brooklyn Nets', '18 Indiana Pacers', '19 San Antonio Spurs', '20 LA Clippers', 
                 '21 Oklahoma City', '22 Boston Celtics', '23 Utah Jazz', '24 Philadelphia Sixers', 
                 '25 Portland Blazzers', '26 Houston Rockets', '27 Denver Nuggets', '28 GoldenState Warriors', 
                 '29 Toronto Raptors', '30 Milwaukee Bucks']
 
Players_List = ['Athony Edwards', 'James Wiseman', 'Jaden McDaniels', 'Cole Anthony', 'LaMelo Ball', 
                'Vernon Carey','Theo Maledon', 'Deni Avdija', 'Nico Mannion', 'Obi Toppin', 'Isaiah Stewart', 
                'NFaly Dante','Zeke Nnaji', 'Tyrese Haliburton', 'Killian Hayes', 'Ochai Agbaji', 'Bryan Antoine', 
                'Onyeka Okongwu','Precious Achiuwa', 'Tyrese Maxey', 'RJ Hampton', 'Jordan Nwora', 'Aaron Henry', 
                'Steve Enoch','Charles Bassey', 'Omer Yurtseven', 'Ashton Hagans', 'Jay Scrubb', 'Tyler Bey', 
                'Jalen Smith']
"""
Implementing Match making algorithms such as stabble-marriage or the stabble roomate can be easier implemented 
using imported libraries such Pandas. This Library removes the need to create a function that creates random 
matrices. Pandas allows developers to access the dictionaries as key value pairs and to skip directly to checking 
for the stability of each key value pair. Furthermore, since Pandas is portable. The size of the data or 
ramdom variables selection can be dynamically altered without having to do so in the actual function. The above, 
NBA_Team_List and Players_List are the same as implemeted in original stable marriage implentation (section 3.1 with code 
seen in Appendix 4.1).
"""
# Assigning k random player choices for each team
TeamChoices = {
'1 New York Knicks':[random.choices(Players_List,k=3)],'2 Cleveland Cavs':[random.choices(Players_List,k=3)], 
'3 Phoenix Suns':[random.choices(Players_List,k=3)],'4 Chicago Bulls':[random.choices(Players_List,k=3)],
'5 Atlanta Hawks':[random.choices(Players_List,k=3)],'6 Washington Wizards':[random.choices(Players_List,k=3)], 
'7 New_Orleans Pelicans':[random.choices(Players_List,k=3)],'8 Memphis Grizzlies':[random.choices(Players_List,k=3)],
'9 Dallas Mavs':[random.choices(Players_List,k=3)],'10 Minnesota Timberwolves':[random.choices(Players_List,k=3)],
'11 LA Lakes':[random.choices(Players_List,k=3)],'12 Charlotte Hornets':[random.choices(Players_List,k=3)], 
'13 Miami Heat':[random.choices(Players_List,k=3)],'14 Sacrameto Kings':[random.choices(Players_List,k=3)], 
'15 Detroit Pistons':[random.choices(Players_List,k=3)], 16 Orlando Magic':[random.choices(Players_List,k=3)], 
'17 Brooklyn Nets':[random.choices(Players_List,k=3)],'18 Indiana Pacers':[random.choices(Players_List,k=3)], 
'19 San Antonio Spurs':[random.choices(Players_List,k=3)], 20 LA Clippers':[random.choices(Players_List,k=3)], 
'21 Oklahoma City':[random.choices(Players_List,k=3)],'22 Boston Celtics':[random.choices(Players_List,k=3)], 
'23 Utah Jazz':[random.chices(Players_List,k=3)],'24 Philadelphia Sixers':[random.choices(Players_List,k=3)], 
'25 Portland Blazzers':[random.choices(Players_List,k=3)],'26 Houston Rockets':[random.choices(Players_List,k=3)], 
'27 Denver Nuggets':[random.choices(Players_List,k=3)],'28 GoldenState Warriors':[random.choices(Players_List,k=3)], 
'29 Toronto Raptors':[random.choices(Players_List,k=3)],'30 Milwaukee Bucks':[random.choices(Players_List,k=3)] }

# Assigning k random team choices for each player

PlayerChoices = {
'Athony Edwards':[random.choices(NBA_Team_List,k=3)],'James Wiseman':[random.choices(NBA_Team_List,k=3)], 
'Jaden McDaniels':[random.choices(NBA_Team_List,k=3)], 'Cole Anthony':[random.choices(NBA_Team_List,k=3)], 
'LaMelo Ball':[random.choices(NBA_Team_List,k=3)], 'Vernon Carey':[random.choices(NBA_Team_List,k=3)],
'Theo Maledon':[random.choices(NBA_Team_List,k=3)], 'Deni Avdija':[random.choices(NBA_Team_List,k=3)], 
'Nico Mannion':[random.choices(NBA_Team_List,k=3)], 'Obi Toppin':[random.choices(NBA_Team_List,k=3)], 
'Isaiah Stewart':[random.choices(NBA_Team_List,k=3)], 'NFaly Dante':[random.choices(NBA_Team_List,k=3)],
'Zeke Nnaji':[random.choices(NBA_Team_List,k=3)], 'Tyrese Haliburton':[random.choices(NBA_Team_List,k=3)], 
'Killian Hayes':[random.choices(NBA_Team_List,k=3)], 'Ochai Agbaji':[random.choices(NBA_Team_List,k=3)], 
'Bryan Antoine':[random.choices(NBA_Team_List,k=3)], 'Onyeka Okongwu':[random.choices(NBA_Team_List,k=3)],
'Precious Achiuwa':[random.choices(NBA_Team_List,k=3)], 'Tyrese Maxey':[random.choices(NBA_Team_List,k=3)], 
'RJ Hampton':[random.choices(NBA_Team_List,k=3)],'Jordan Nwora':[random.choices(NBA_Team_List,k=3)], 
'Aaron Henry':[random.choices(NBA_Team_List,k=3)], 'Steve Enoch':[random.choices(NBA_Team_List,k=3)],
'Charles Bassey':[random.choices(NBA_Team_List,k=3)], 'Omer Yurtseven':[random.choices(NBA_Team_List,k=3)], 
'Ashton Hagans':[random.choices(NBA_Team_List,k=3)], 'Jay Scrubb':[random.choices(NBA_Team_List,k=3)], 
'Tyler Bey':[random.choices(NBA_Team_List,k=3)], 'Jalen Smith':[random.choices(NBA_Team_List,k=3)] }


"""
If the developer is using jupyter notebook to dynamically check if the code is working 
they can simple check the values assigned to each key as below.
"""
# Dynamically checking for a desired player's choice
PlayerChoices['Jalen Smith']

#Dynamically checking for a desired team's choice
TeamChoices['1 New York Knicks']

TeamDraftPicks2 = sorted(TeamChoices.keys())
PlayerChoices2 = sorted(PlayerChoices.keys())

def checking(drafted):
    DraftedOrNot = dict((v,k) for k,v in drafted.items())
    for p, t in drafted.items():
        
        players_choice = PlayerChoices[p]
        players_best_choice = players_choice[:players_choice.index(t)]
        
        Team_choices = TeamChoices[t]
        Team_best_choices = Team_choices[:Team_choices.index(p)]       
        
        for NBA_Team in Players_Like_Better:
            Dream_Team = dream_pick[NBA_Team]
            Team_Likes = team_likes[NBA_Team]
            if Team_Likes.index(Dream_Team) > Team_Likes.index(p):
                print("%s and %s would been a better draft choice"
                      "While their current draft choice is: %s and %s "
                      % (p, NBA_Team, t, Dream_Team))
                return False
            
        for player in team_best_choice:
            DraftPick = DraftedOrNot[player]
            Player_likes = players_prefer[player]
            if Player_likes.index(DraftPick) > Player_likes.index(teams):
                print("%s and %s would have been a better draft choice"
                      "While their current draft choice is: %s and %s "
                      % (teams, player, p, DraftPick))
                return False
    return True

def makingmatches():
    freeteams = TeamDraftPicks2[:]
    drafted = {}
    TeamChoices_2 = copy.deepcopy(TeamChoices)
    PlayerChoices_2 = copy.deepcopy(PlayerChoices)
    
    while freeteams:
        NBA_Team = freeteams.pop(0)
        Teamlist = TeamChoices_2[NBA_Team]
        
        player = Teamlist.pop(0)
        Already_Drafted = drafted.get(tuple(player))
        if not Already_Drafted:
            # player is free
            drafted[tuple(player)] = NBA_Team
            print("  %s top player on list %s" % (NBA_Team, player[0]))
        else:
            playerslist = PlayerChoices_2[player]
            if playerslist.index(Already_Drafted) > playerslist.index(NBA_Team):
                drafted[player] = NBA_Team
                print("  %s changed teams after the draft and changed %s for %s" % (player[0], 
                                                    Already_Drafted, NBA_Team))
                if TeamChoices_2[Already_Drafted]:
                    freeteams.append(Already_Drafted)
            else:
                if guyslist:
                    freeteams.append(NBA_Team)
    return drafted

print('\nThe prefered pick for each team:')
drafted = makingmatches()

print('\n Players dream desitantions:')
print('  ' + ',\n  '.join('%s Would like to get draftd to -> %s' % x
                          for x in sorted(drafted.items())))



