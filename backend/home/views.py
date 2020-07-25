from django.shortcuts import render
from django.http import JsonResponse
from .models import Question,Feedback,User,Unit,Stay,Donor,Donate
import json
from .databaseEntry import addQuestions,addUsers,addFeedbacks,addData
import datetime
from .databaseEntry import addQuestions
from django.views.decorators.csrf import csrf_exempt
from google.cloud import translate_v2
from gtts import gTTS
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import soundfile
from .report import send_message
import threading

# Create your views here.

def questions(request,phone_no):
    user = User.objects.filter(phone_no = phone_no)[0]
    lang = user.language

    jsonResponse = {}
    questionList = []
    
    questions = Question.objects.all()
    for question in questions:

        langQuestionText = translate(question.question, lang)
        langQuestionAudio = translate(langQuestionText,lang)
        json = {
            'Id':question.id,
            'Question':question.question,
            'LangQuestionText': langQuestionText,
            'LangQuestionAudio': langQuestionAudio,
        }
        questionList.append(json)
    
    jsonResponse['Questions'] = questionList
    return JsonResponse(jsonResponse)

def reports():
    string = ""
    units = Unit.objects.all()
    for unit in units:
        users = Stay.objects.filter(UnitID = unit.id)
        print(unit.id)
        for user in users:
            currentUser = User.objects.filter(id = user.UserID.id)[0]
            string += "Age = "+str(currentUser.age)+ "  Number of people = "+str(user.members)+"  Duration: "+ str(user.startDate)+ " - "+ str(user.endDate)+ "\n"

        donors = Donate.objects.filter(unit_no = unit.id)
        for donor in donors:
            currentDonor = Donor.objects.filter(id = donor.donor_id.id)[0]
            phoneNumber = "whatsapp:+91" + currentDonor.phone_no
            send_message(string,phoneNumber)

@csrf_exempt 
def feedback(request):
    obj = json.load(request.POST)
    phone_no = obj["phone_no"]
    user = User.objects.filter(phone_no = phone_no)[0]
    feedbacks = obj["Feedback"]
    f = Feedback.objects.all().order_by('id')
    last_id = len(f)+1
    
    for feedback in feedbacks:
        question = Question.objects.filter(feedback["id"])[0]
        temp = Feedback(id = last_id,question_id = question,user_id = user,unit_no = int(feedback["unit_no"]),response = int(feedback["Response"]))
        temp.save()       

@csrf_exempt 
def loadData(request):
    if request.method != "POST":
        return JsonResponse({"data":"use post"})
    
    questions,feedbacks,users,units,stays,donors,donates = addData()

    for question in questions:
        temp = Question(id = question["id"],question = question["question"])
        temp.save()

    for user in users:
        temp = User(id = user["id"],name = user["name"],age = user["age"],address = user["address"],phone_no = user["phone"],language = user["langauge"])
        temp.save()

    for feedback in feedbacks:
        user = User.objects.filter(id = int(feedback["userid"]))[0]
        question = Question.objects.filter(id = int(feedback["qid"]))[0]
        temp = Feedback(id = feedback["id"],question_id = question,user_id = user,unit_no = feedback["unitid"],response = feedback["response"] )
        temp.save()
    
    for unit in units:
        temp = Unit(id =int(unit["id"]),location = unit["location"])
        temp.save()
    
    for stay in stays:
        StDate = stay["startDate"]
        date1 = datetime.date(int(StDate[6:]),int(StDate[3:5]),int(StDate[:2]))
        EdDate = stay["endDate"]
        date2 = datetime.date(int(EdDate[6:]),int(EdDate[3:5]),int(EdDate[:2]))
        user = User.objects.filter(id = int(stay["useriD"]))[0]
        unit_no = Unit.objects.filter(id = int(stay["unitid"]))[0]
        temp = Stay(UserID = user,UnitID = unit_no,members = int(stay["members"]),startDate = date1,endDate = date2)
        temp.save()

    for donor in donors:
        temp = Donor(id =int(donor["id"]),phone_no = donor["phone"])
        temp.save()

    for donate in donates:
        unit_no = Unit.objects.filter(id = int(donate["unitid"]))[0]
        donor_id = Donor.objects.filter(id = int(donate["userid"]))[0]
        temp = Donate(unit_no = unit_no,donor_id = donor_id)
        temp.save()
        
    return JsonResponse({"success":"True"})

def translate(sourceText, targetLanguage):
    client = translate_v2.Client()
    response = client.translate(sourceText,target_language=targetLanguage)
    return format(response["translatedText"])

def textToSpeech(sourceText, sourceLanguage):
    obj = gTTS(text=sourceText, slow= False, lang=sourceLanguage)
    return obj

def speechToText(local_file_path, language):
    audio_samples, sample_rate = soundfile.read(local_file_path, dtype='int16')
    client = speech_v1.SpeechClient()

    # local_file_path = 'resources/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = language

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = sample_rate
    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    resultString=""
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        resultString = resultString + format(alternative.transcript)

    return resultString

t = threading.Timer(10.0, reports)
t.start()