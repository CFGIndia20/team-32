from django.shortcuts import render
from django.http import JsonResponse
from .models import Question,Feedback,User
import json
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from google.cloud import translate_v2
from gtts import gTTS
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import soundfile

# Create your views here.
def questions(request):
    jsonResponse = {}
    questionList = []
    questions = Question.objects.all()
    for question in questions:
        json = {
            'Id':question.id,
            'Question':question.question
        }
        questionList.append(json)
    
    jsonResponse['Questions'] = questionList
    return JsonResponse(jsonResponse)

def translate(sourceText, targetLanguage):
    client = translate_v2.Client()
    response = client.translate(sourceText,target_language=target_language)
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
