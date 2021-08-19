"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 13:47:00
Last Modified by:----
Last Modified time:----
Title : Find the factors of the given number
"""
usa_basketball_rio2016_players={'Jimmy Butler','Kevin Durant','DeAndre Jordan','Kyle Lowry','Harrison Barnes',
                        'DeMar DeRozan','Kyrie Irving','Klay Thompson','DeMarcus Cousins',
                        'Paul George','Draymond Green','Carmelo Anthony'}  

usa_basketball_tokyo2020_players={'Bam Adebayo','Devin Booker','Kevin Durant','Jerami Grant','Draymond Green',
                            'Drew Holiday','Keldon Johnson','Zach Lavine','Damian Lillard','Javale McGee',
                            'Khris Middleton','Jayson Tatum'}

players_only_played_rio=usa_basketball_rio2016_players.difference(usa_basketball_tokyo2020_players)
print(players_only_played_rio)