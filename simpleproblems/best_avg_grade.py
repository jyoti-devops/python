"""
 Best Avg grade
"""
import math

def best_avg_grade(scores):
    """
    find the best avg grade for given students marks
    """
    students = {}
    for i in enumerate(len(scores)):
        if scores[i][0] in students:
            students[scores[i][0]] = math.floor(float((students[scores[i][0]] + float(scores[i][1])) / 2))
            print(students[scores[i][0]])
        else:
            students[scores[i][0]] = float(scores[i][1])
    print(students)
    return max(students.values())


if __name__ == "__main__":
    tc1 = [["st1", "87"], ["st2", "100"], ["st3", "64"], ["st2", "22"]]
    tc2 = [["st1", "81"], ["st2", "92"], ["st3", "93"], ["st3", "95"], ["st2", "94"], ["st1", "93"]]
    tc3 = [["st1", "-66"], ["st1", "-65"], ["st3", "-122"]]
    print(best_avg_grade(tc1))
    print(best_avg_grade(tc2))
    print(best_avg_grade(tc3))
