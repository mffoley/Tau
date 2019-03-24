import os
import random
import datetime
import util

from flask import Flask, redirect, url_for, render_template, session, request, flash, get_flashed_messages


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/conic")
def conic():
    data=util.generate_precalc()
    print(data)
    return render_template("conic.html",data=data)

@app.route("/checkConic", methods=['POST'])
def checkConic():
    print(request.form)
    print(request.form["answer"])
    print(request.form["firstPoly"])
    print(request.form["shape"])
    answer=request.form["firstPoly"][1:][:-1].split(", ")
    answers=[]
    for i in answer:
        answers.append(int(i))
    print(answers)
    c=0
    if int(request.form["shape"]) == int(request.form["answer"]):
        c=1
    return(render_template("conicResponse.html",data=[c,int(request.form["answer"]),answers]))

@app.route("/algebra")
def algebra():
    data=util.generate_alg()
    print(data)
    return render_template("alg.html",data=data)
    #render_template is also useful

@app.route("/checkAlgebra", methods=['POST'])
def checkAlg():
#try:
    print(request.form["type"])
    print(request.form["r1C"])
    print(request.form["r2C"])
    print(request.form["r1"])
    print(request.form["r2"])
    correct=[int(request.form["r1C"]),int(request.form["r2C"])]
    given=[int(request.form["r1"]),int(request.form["r2"])]
    print(correct)
    print(given)
    correctQ=0
    if given[0] == correct[0]:
        if given[1]==correct[1]:
            correctQ=1
    elif given[0] == correct[1]:
        if given[1] == correct[0]:
            correctQ=1
    if correctQ == 1:
        return(render_template("algResponse.html",h=[1,[int(request.form["og1"]),int(request.form["og2"])],correct]))
    else:
        return(render_template("algResponse.html",h=[0,[int(request.form["og1"]),int(request.form["og2"])],correct]))
#except Exception as e:
#    return redirect(url_for("home"))

@app.route("/calculus")
def calc():
    data=util.generate_calc()
    print(data)
    return render_template("calc.html",data=data)
    #render_template is also useful

@app.route("/checkCalculus", methods=['POST'])
def checkCalc():
#try:
    print(request.form)
    if int(request.form["type"])==0:
        correct=[]
        given=[]
        correct.append(int(request.form["r0C"]))
        given.append(int(request.form["r0"]))
        for i in range(int(request.form["len"])-1):
            correct.append(int(request.form["r"+str(i+1)+"C"]))
            given.append(int(request.form["r"+str(i+1)]))
        print(correct)
        print(given)
        correctQ=1
        og=[]
        for i in range(int(request.form["len"])+1):
            og.append(int(request.form["og"+str(i)]))
        for i in range(int(request.form["len"])):
            if int(correct[i]) != int(given[i]):
                correctQ=0
        if correctQ == 1:
            return(render_template("calcResponse.html",data=[1,og,correct,0],h=[1,og,correct,0]))
        else:
            return(render_template("calcResponse.html",data=[0,og,correct,0],h=[0,og,correct,0]))
    elif int(request.form["type"])==1:
        given=[]
        given.append(int(request.form["r0"]))
        for i in range(int(request.form["len"])-2):
            given.append(int(request.form["r"+str(i+1)]))
        firsts=request.form["firstPoly"][1:][:-1].split(", ")
        first=[]
        for i in firsts:
            first.append(int(i))
        second=[]
        seconds=request.form["secondPoly"][1:][:-1].split(", ")
        for i in seconds:
            second.append(int(i))
        answer=request.form["answers"][1:][:-1].split(", ")
        answers=[]
        for i in answer:
            answers.append(int(i))
        correctQ=1
        for i in range(len(given)):
            if given[i] != int(answers[i]):
                correctQ=0
        if correctQ == 1:
            print([1,answers,[[first],[second]],1])
            return(render_template("calcResponse.html",data=[1,answers,[first,second],1],h=[1,answers,[[first],[second]],1]))
        else:
            print([1,answers,[[first],[second]],1])
            return(render_template("calcResponse.html",data=[0,answers,[first,second],1],h=[0,answers,[[first],[second]],1]))
    else:
        given=[]
        given.append(int(request.form["r0"]))
        for i in range(int(request.form["len"])-2):
            given.append(int(request.form["r"+str(i+1)]))
        ogs=request.form["og"][1:][:-1].split(", ")
        og=[]
        for i in ogs:
            og.append(int(i))
        answer=request.form["answers"][1:][:-1].split(", ")
        answers=[]
        for i in answer:
            answers.append(int(i))
        correctQ=1
        for i in range(len(given)):
            if given[i] != int(answers[i]):
                correctQ=0
        if correctQ == 1:
            print([1,answers,og,2])
            return(render_template("calcResponse.html",data=[1,answers,og,2],h=[1,answers,og,2]))
        else:
            print([1,answers,og,2])
            return(render_template("calcResponse.html",data=[0,answers,og,2],h=[0,answers,og,2]))
#except Exception as e:
#    return redirect(url_for("home"))


if __name__ == "__main__":
    app.debug = True

app.run()
