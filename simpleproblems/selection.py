def selection(current_teamsize, input_score , team_size,k):
        new_team = []
        if len(input_score) > 10**9 or  team_size > 10**5 or k > 10**5:
            print("not possible")
            return 0
        while len(new_team) < team_size:
            if k >= current_teamsize:
                new_team.append(input_score.pop((input_score.index(max(input_score)))))
            else:
                print(input_score)
                temp_team1 = input_score[0:k]
                temp_team2 = input_score[-k:]
                print(temp_team1, temp_team2)
                if max(temp_team1) >= max(temp_team2):
                    new_team.append(input_score.pop(input_score.index(max(temp_team1))))
                else:
                    
                        print(input_score.index(max(temp_team2)))
                        input_score.reverse()
                        print(input_score)
                        new_team.append(input_score.pop(input_score.index(max(temp_team2))))
                        print(input_score)
                        input_score.reverse()
   
                
        print('newteam')
        print(new_team)
        
        return sum_score(new_team)
    

def sum_score(team_score):
    sum_score = 0
    for key in range(len(team_score)):
        sum_score += team_score[key]
    print(sum_score)
    return sum_score

if __name__ == "__main__":
    selection(7,[10,20,10,15,5,30,20],2,3)
    selection(8,[18,5,15,18,11,15,9,7],5,1)
    selection(8,[6,18,8,14,10,12,18,9],8,3)