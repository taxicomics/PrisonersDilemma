import statistics

def analyze_results(game_data,game_nr):
    defect_str="X "
    coorperate_str="O "
    spacer_str=""*len(game_data)
    lines=["Game "+str(game_nr)+":",spacer_str]
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
            p_1_points+=0
            p_2_points+=5
        elif i[1] and i[0]==False:
            p_1_points+=5
            p_2_points+=0
        elif i[0]==False and i[1]==False:
            p_1_points+=1
            p_2_points+=1
    lines.append(str1+"  Points:"+str(p_1_points))
    lines.append(str2+"  Points:"+str(p_2_points))
    lines.append(spacer_str)
    #print the results
    for i in lines:
        print(i)
    return p_1_points,p_2_points

def play_game(games_array,func1,func2,how_many_times):
    for i in range(how_many_times): 
        choice_1=func1(games_array,0)
        choice_2=func2(games_array,1)
        games_array.append([choice_1,choice_2])
    
def analyze_scores(score_table):
    average_score_p_1=0
    all_p1_scores=[]
    all_p2_scores=[]
    average_score_p_2=0
    p1_sum=0
    p2_sum=0
    for i in score_table:
        p1_sum+=i[0]
        all_p1_scores.append(i[0])
        p2_sum+=i[1]
        all_p2_scores.append(i[1])


    average_score_p_1=p1_sum/len(score_table)  
    average_score_p_2=p2_sum/len(score_table)  
    print(str(average_score_p_1)+" AVG Player 1 Score |"+str(statistics.median(all_p1_scores))+" Median Player 1 Score")
    print(str(average_score_p_2)+" AVG Player 2 Score |"+str(statistics.median(all_p2_scores))+" Median Player 1 Score")
    print(str(round(p1_sum/(p1_sum+p2_sum),2))+ " Player 1 Percent of Points")
    print(str(round(p2_sum/(p1_sum+p2_sum),2))+ " Player 2 Percent of Points")