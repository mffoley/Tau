import os
import random
from datetime import datetime

def generate_alg():
    #0: factoring
    #1: foiling
    random.seed(datetime.now())
    type = int(random.random()*2)
    #type=0

    x = int(random.random()*20) + 1
    y = int(random.random()*20) + 1
    if x > 10:
        y = int(y/2)

    signs = [[1,1],[1,-1],[-1,1],[-1,-1]]
    random_sign = int(random.random()*4)
    x *= signs[random_sign][0]
    y *= signs[random_sign][1]
    a = 1
    b = -1 * (x + y)
    c = x * y

    if type == 0:
        return [0, [x,y],[a,b,c]]
    else:
        return [1, [a,b,c], [x,y]]

def generate_trig():
    return []

def generate_calc():
    #0: power rule
    random.seed(datetime.now())
    x = int(random.random()*6) + 1
    coefficients = []
    answers = []
    for i in range(x):
        temp = int(random.random()*25)
        coefficients.insert(0,temp)
        answers.insert(0, i * temp)
    return [0, answers[:-1], coefficients]

def generate_question(type):
    '''
    0: Algebra
    1: Trigonometry
    2: Calculus
    '''
    subject = [generate_alg, generate_trig, generate_calc]
    return subject[type]()
