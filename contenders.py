import random

random.seed()

def my_winning_function(game_data,player_nr):
    #game_data is the array of games so far, either empty(first round) or formatted like this: player_nr [[False, False],[False, False]] (2 rounds of only defections)
    #player_nr is this players index, so whether they are the first(0) or the second(1) value in a round
    opponent_nr=1-player_nr
    #for ease of use this is index of the opponents value
    choice=False
    #this function should return either true(coorperate) or false(defect)

    #your cool code goes here
    if len(game_data)>0:
        #what to do if this is NOT the first round
        choice=not game_data[len(game_data)-1][opponent_nr]
        #this example always does the opposite of what the opponent did last round
    else:
        #what to do in the first round
        choice=True
        #this example starts with a cooperation
    
    #your cool code ended here
    return choice

def random_positive_leaner(game_data,player_nr):
    #game_data is the array of games so far, either empty(first round) or formatted like this: player_nr [[False, False],[False, False]] (2 rounds of only defections)
    #player_nr is this players index, so whether they are the first(0) or the second(1) value in a round
    opponent_nr=1-player_nr
    #for ease of use this is index of the opponents value
    choice=False
    #this function should return either true(coorperate) or false(defect)

    #your cool code goes here
    if random.randint(0,10)<6:
        choice=True
    #your cool code ended here
    return choice