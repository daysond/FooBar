from math import sqrt

def solution(num):
    panels = []
    while num != 0:
        root = int(sqrt(num))
        sq = root * root 
        panels.append(sq)
        num = num - sq
        
    return panels
