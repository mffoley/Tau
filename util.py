import os
import random
from datetime import datetime

def generate_alg():
    #0: factoring
    #1: foiling
    random.seed(datetime.now())
    type = int(random.random()*2)

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

def generate_precalc():
    #0: circle
    #1: hyperbola
    #2: ellipse
    #3: parabola
    random.seed(datetime.now())
    type = int(random.random()*4)

    conic = 0
    a = 0
    c = 0
    d = int(random.random() * 20) - 10
    e = int(random.random() * 20) - 10
    f = int(random.random() * 20) - 10
    while a * c == 0:
        a = int(random.random() * 20) - 10
        c = int(random.random() * 20) - 10

    coefficients = [a,c,d,e,f]
    if a == c:
        return [0,0,coefficients]
    if a * c < 0:
        return [0,1,coefficients]
    if a * c > 0:
        return [0,2,coefficients]
    return [0,3,coefficients]

def generate_polynomial_derivative(seed, upper_limit):
    random.seed(seed)
    x = int(random.random()*6) + 2
    coefficients = []
    answers = []
    for i in range(x):
        temp = int(random.random()*upper_limit) + 1
        sign = int(random.random()*2)
        if sign == 0:
            temp *= -1
        coefficients.insert(0,temp)
        answers.insert(0, i * temp)
    return [0, answers[:-1], coefficients]

def product_rule_inner(derivative, normal):
    answer = []
    len_deriv = len(derivative)
    len_norm = len(normal)
    for i in range(len_deriv + len_norm - 1):
        answer.append(0)

    for i in range(len_deriv):
        coefficient_deriv = derivative[i]
        for j in range(len_norm):
            coefficient_norm = normal[j]
            new_coeff = coefficient_norm * coefficient_deriv
            answer[i+j] += new_coeff
    return answer

def generate_calc():
    #0: derivative - power rule
    #1: derivative - product rule
    #2: integrals - power rule
    random.seed(datetime.now())
    type = int(random.random()*3) #CHANGE THIS AS MORE RULES ARE ADDED


    if type == 0:
        return generate_polynomial_derivative(random.random(), 25)
    elif type == 1:
        function_one = generate_polynomial_derivative(random.random(), 11)
        function_two = generate_polynomial_derivative(random.random(), 11)
        first_part = product_rule_inner(function_one[1], function_two[2])
        second_part = product_rule_inner(function_two[1], function_one[2])
        answers = []
        for i in range(len(first_part)):
            answers.append(first_part[i] + second_part[i])
        return [1, answers , [function_one[2], function_two[2]]]
    elif type == 2:
        derivative = generate_polynomial_derivative(random.random(), 11)
        temp = derivative[1]
        derivative[1] = derivative[2]
        derivative[2] = temp
        derivative[1][-1] = 5
        derivative[0] = 2
        return derivative
