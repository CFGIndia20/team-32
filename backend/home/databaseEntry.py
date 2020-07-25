import json
import os

def addQuestions():
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	f = open(os.path.join(workpath,'data.json'))
	data = json.load(f)
	Questions = data["Question"]
	return Questions
    
def addFeedbacks():
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	f = open(os.path.join(workpath,'data.json'))
	data = json.load(f)
	Feedbacks = data["Feedback"]
	return Feedbacks

def addUsers():
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	f = open(os.path.join(workpath,'data.json'))
	data = json.load(f)
	Users = data["User"]
	return Users

def addData():
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	f = open(os.path.join(workpath,'data.json'))
	data = json.load(f)
	Questions = data["Question"]
	Feedbacks = data["Feedback"]
	Users = data["User"]
	Units = data["Unit"]
	Stays = data["Stay"]
	Donors = data["Donor"]
	Donates = data["Donates"]
	return Questions,Feedbacks,Users,Units,Stays,Donors,Donates