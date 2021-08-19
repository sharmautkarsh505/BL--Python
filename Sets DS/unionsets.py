"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 13:34:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to create a union of sets.
"""

usa_basketball_rio2016_players={'Jimmy Butler','Kevin Durant','DeAndre Jordan','Kyle Lowry','Harrison Barnes',
                        'DeMar DeRozan','Kyrie Irving','Klay Thompson','DeMarcus Cousins',
                        'Paul George','Draymond Green','Carmelo Anthony'}  

usa_basketball_tokyo2020_players={'Bam Adebayo','Devin Booker','Kevin Durant','Jerami Grant','Draymond Green',
                            'Drew Holiday','Keldon Johnson','Zach Lavine','Damian Lillard','Javale McGee',
                            'Khris Middleton','Jayson Tatum'}

rio2016_or_tokyo_2020=usa_basketball_rio2016_players.union(usa_basketball_tokyo2020_players)
print(rio2016_or_tokyo_2020)