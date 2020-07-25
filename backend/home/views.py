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

# Create your views here.

def questions(request,phone_no):
    user = User.objects.filter(phone_no = phone_no)[0]
    lang = user.language

    jsonResponse = {}
    questionList = []
    
    questions = Question.objects.all()
    for question in questions:
        json = {
            'Id':question.id,
            'Question':question.question,
            'LangQuestionText': translate(),
        }
        questionList.append(json)
    
    jsonResponse['Questions'] = questionList
    return JsonResponse(jsonResponse)

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
    
def loadData(request):
    if request.method != "POST":
        return JsonResponse({"data":"use post"})

    questions,feedbacks,users,units,stays,donors,donates = addData()
    for question in questions:
        temp = Question(id = question["id"],question = question["Question"])
        temp.save()

    
    for user in users:
        temp = User(id = user["id"],name = user["Name"],age = user["Age"],address = user["Address"],phone_no = user["Phone no"],language = user["Language"])
        temp.save()

    for feedback in feedbacks:
        user = User.objects.filter(id = int(feedback["User id"]))[0]
        question = Question.objects.filter(id = int(feedback["Qid"]))[0]
        temp = Feedback(id = feedback["id"],question_id = question,user_id = user,unit_no = feedback["Unit no."],response = feedback["Response"] )
        temp.save()

    for unit in units:
        temp = Unit(id =int(unit["id"]),location = unit["location"])
        temp.save()
    
    for stay in stays:
        StDate = stay["startDate"]
        date1 = datetime.strptime(StDate,'%d/%m/%y')
        EdDate = stay["endDate"]
        date2 = datetime.strptime(EdDate,'%d/%m/%y')
        user = User.objects.filter(id = int(stay["User id"]))[0]
        unit_no = Unit.objects.filter(id = int(stay["Unit id"]))[0]
        temp = Stay(UserID = user,UnitID = unit_no,members = int(stay["members"]),startDate = date1,endDate = date2)
        temp.save()
    
    for donor in donors:
        temp = Donor(id =int(donor["id"]),phone_no = donor["phoneNo"])
        temp.save()

    for donate in donates:
        unit_no = Unit.objects.filter(id = int(donate["unitId"]))[0]
        donor_id = Donor.objects.filter(id = int(donate["donorId"]))[0]
        temp = Donate(unit_no = unit_no,donor_id = donor_id)
        temp.save()
        
    return JsonResponse({"success":"True"})

@csrf_exempt    
def loadQuestions(request):
    if request.method != "POST":
        return JsonResponse({"data":"use post"})

    questions = addQuestions()
    for question in questions:
        temp = Question(id = question["id"],question = question["Question"])
        temp.save()

    return JsonResponse({"success":"True"})

@csrf_exempt    
def loadFeedback(request):
    if request.method != "POST":
        return JsonResponse({"data":"use post"})

    feedbacks = addFeedbacks()
    for feedback in feedbacks:
        user = User.objects.filter(id = int(feedback["User id"]))[0]
        question = Question.objects.filter(id = int(feedback["Qid"]))[0]
        temp = Feedback(id = feedback["id"],question_id = question,user_id = user,unit_no = feedback["Unit no."],response = feedback["Response"] )
        temp.save()

    return JsonResponse({"success":"True"})

@csrf_exempt    
def loadUser(request):
    if request.method != "POST":
        return JsonResponse({"data":"use post"})

    users = addUsers()

    for user in users:
        temp = User(id = user["id"],name = user["Name"],age = user["Age"],address = user["Address"],phone_no = user["Phone no"],language = user["Language"])
        temp.save()

    return JsonResponse({"success":"True"})

@csrf_exempt
def loadStays(request):
    if request.method != "POST":
        return JsonResponse({"data":"use post"})

    stays = addStays()
    for stay in stays:
        StDate = stay["startDate"]
        date1 = datetime.strptime(StDate,'%d/%m/%y')
        EdDate = stay["endDate"]
        date2 = datetime.strptime(EdDate,'%d/%m/%y')
        temp = Stays(UserID = stay["UserID"],UnitID = stay["UnitID"], members = stay["members"], startDate = date1, endDate = date2)
        temp.save()

    return JsonResponse({"success":"True"})

def translate(sourceText, targetLanguage):
    client = translate_v2.Client()
    response = client.translate(sourceText,target_language=targetLanguage)
    return response["translatedText"]

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

