
#basic setup
#The prisoner's dilemma is a game theory thought 
#experiment that involves two rational agents, each 
#of whom can COORPERATE for mutual benefit or betray 
#their partner ("defect") for individual reward.

#imports
import helper_functions
import contenders
#vars
games=[]
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#                      Put YOUR function down below
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

helper_functions.play_game( games,contenders.random_positive_leaner ,         contenders.my_winning_function            ,30)
helper_functions.analyze_results(games)
