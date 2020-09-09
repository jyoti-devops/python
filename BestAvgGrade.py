'''
Bets Avg grade 
'''
import math 
def BestAvgGrade(scores):
    students = {}
    for i in range(0,len(scores)):
        if scores[i][0] in students:
            students[scores[i][0]] =  math.floor(float((students[scores[i][0]]+  float(scores[i][1])) /2))
            print(students[scores[i][0]])
        else:
            students[scores[i][0]] = float(scores[i][1])
    print(students)
    return max(students.values())

if __name__ == "__main__":
    tc1 = [["st1","87"],["st2","100"],["st3","64"],["st2","22"]]
    tc2 = [["st1","81"],["st2","92"],["st3","93"],["st3","95"],["st2","94"],["st1","93"]]
    tc3 = [["st1","-66"],["st1","-65"],["st3","-122"]]
    print(BestAvgGrade(tc1))
    print(BestAvgGrade(tc2))
    print(BestAvgGrade(tc3))