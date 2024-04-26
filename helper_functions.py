def analyze_results(game_data):
    defect_str="X "
    coorperate_str="O "
    spacer_str="___"*len(game_data)
    lines=["These are the results",spacer_str]
    str1="Player 1: "
    str2="Player 2: "
    p_1_points=0
    p_2_points=0
    for i in game_data:
        #visualize
        if i[0]:
            str1+=coorperate_str
        elif not i[0]:
            str1+=defect_str
        if i[1]:
            str2+=coorperate_str
        elif not i[1]:
            str2+=defect_str
        #award points
        if i[0] and i[1]:
            p_1_points+=3
            p_2_points+=3
        elif i[0] and i[1]==False:
            p_1_points+=5
            p_2_points+=0
        elif i[1] and i[0]==False:
            p_1_points+=0
            p_2_points+=5
        elif i[0]==False and i[1]==False:
            p_1_points+=1
            p_2_points+=1
    lines.append(str1+"  Points:"+str(p_1_points))
    lines.append(str2+"  Points:"+str(p_2_points))
    lines.append(spacer_str)
    #print the results
    for i in lines:
        print(i)

def play_game(games_array,func1,func2,how_many_times):
    for i in range(how_many_times): 
        choice_1=func1(games_array,0)
        choice_2=func2(games_array,1)
        games_array.append([choice_1,choice_2])
    
def random_choice(game_data,player_nr):
    ret=True
    return ret