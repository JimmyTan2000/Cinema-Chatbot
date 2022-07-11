# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Description links for movies
descriptionLinks = [
    {"Avengers": "https://en.wikipedia.org/wiki/The_Avengers_(2012_film)", 
    "Jumanji":"https://en.wikipedia.org/wiki/Jumanji:_Welcome_to_the_Jungle",
    "No Time To Die":"https://en.wikipedia.org/wiki/No_Time_to_Die",
    "Batman":"https://en.wikipedia.org/wiki/The_Batman_(film)"}
]

@app.get("/descriptionLinks")
def get_descriptionLinks():
    return jsonify(descriptionLinks)

@app.post("/descriptionLinks")
def add_descriptionLink():
    if request.is_json:
        descriptionLink = request.get_json()
        descriptionLinks.append(descriptionLink)
        return descriptionLink, 201
    return {"error": "Request must be JSON"}, 415

# Schedules for movies
schedules = [
     {"Date" : "Today", "Name": ["Avengers,No Time To Die"], "Time":{"Avengers":"12:00, 15:30, 17:00","No Time To Die":"22:00"}},
     {"Date" : "Tomorrow", "Name": ["Jumanji,Batman"], "Time":{"Jumanji":"12:30, 14:30, 18:00","Batman":"17:35,22:30"}},
     {"Date" : "29/11", "Name": ["Avengers,Batman"], "Time":{"Avengers":"12:30, 14:30, 18:00","Batman":"17:35,22:30"}},
     {"Date" : "30/11", "Name": ["Jumanji,No Time To Die"], "Time":{"Jumanji":"12:30, 14:30, 18:00","No Time To Die":"17:35,22:30"}},
     {"Date" : "Others", "Name": ["Avengers,Batman"], "Time":{"Avengers":"13:00, 15:00, 19:00","Batman":"12:35,21:30"}}
 ]

@app.get("/schedules")
def get_schedules():
    return jsonify(schedules)

@app.post("/schedules")
def add_schedule():
    if request.is_json:
        schedule = request.get_json()
        schedules.append(schedule)
        return schedule, 201
    return {"error": "Request must be JSON"}, 415 

# Sitting plan of movies
sittingPlans = [
    {"Date" : "Today", "Schedules" : [{"AVENGERS":[{"12:00": "G35,G36,G38,S25,S26", "17:30":"S80,E27,G54,G56"}], 
    "NO TIME TO DIE":[{"13:00": "G65,G16,Z78,P95,F66", "16:30":"H81,Z67,P84,U25"}]}] },
    {"Date" : "Tomorrow", "Schedules" : [{"JUMANJI":[{"15:00": "T23,J67,I12,P09,Q38", "20:45":"P90,N89,P33,Y21"}], 
    "BATMAN":[{"10:00": "L90,R45,O78,W23,Q23", "14:30":"K12,Q50,A89,M12"}]}] },
    {"Date" : "29/11", "Schedules" : [{"AVENGERS":[{"12:00": "G36,G37,G38,S25,S26", "17:30":"S80,E27,G54,G55"}], 
    "BATMAN":[{"12:00": "G35,G36,G38,S25,S26", "17:30":"S80,E27,G54,G10"}]}] },
     {"Date" : "30/11", "Schedules" : [{"JUMANJI":[{"13:00": "A45,A30,B28,G25,F26", "16:50":"G/0,F17,R14,F25"}],
    "NO TIME TO DIE":[{"13:00": "G37,P35,U56,I25,B81", "16:30":"P90,S10,G19,S83"}]}] },
    {"Date" : "Others", "Schedules" : [{"AVENGERS":[{"12:00": "D35,H36,A38,S25,F26", "17:30":"Z80,E40,G10,G20"}], 
    "BATMAN":[{"12:00": "G30,G31,G32,S20,S23", "17:30":"S80,E27,G54,G30"}]}] }
]

@app.get("/sittingPlans")
def get_sittingPlans():
    return jsonify(sittingPlans)

@app.post("/sittingPlans")
def add_sittingPlans():
    if request.is_json:
        sittingPlan = request.get_json()
        sittingPlans.append(sittingPlan)
        return sittingPlan, 201
    return {"error": "Request must be JSON"}, 415 