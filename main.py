
#basic setup
#The prisoner's dilemma is a game theory thought 
#experiment that involves two rational agents, each 
#of whom can COORPERATE for mutual benefit or betray 
#their partner ("defect") for individual reward.

#imports
import helper_functions
import contenders
#vars
#keeping track of the individual games
games=[]
#keeping track of the games scores for later analysis
scores=[]
nr_of_rounds=30
nr_of_games=300
function1=contenders.random_positive_leaner
function2=contenders.random_positive_leaner
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#                      Put YOUR function down below
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
for i in range(nr_of_games):
    helper_functions.play_game( games,function1,function2,nr_of_rounds)
    scores.append(helper_functions.analyze_results(games))
    games=[]
helper_functions.analyze_scores(scores)