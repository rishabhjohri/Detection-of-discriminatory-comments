from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
import requests
url = 'https://1c40-34-124-128-64.ngrok.io/get_prediction'

def home(request):
    return render(request, 'home.html')
def detect(request):
    text = request.GET['text']
    input_data_for_model = {'text' : text }
    input_json = json.dumps(input_data_for_model)
    response = requests.post(url, data=input_json)
    x = response.json()
    Y = json.loads(x)
    not_bodyshaming = float(Y['not_bodyshaming'])
    bodyshaming = float(Y['bodyshaming'])
    not_hatespeech = float(Y['not_hatespeech'])
    hatespeech = float(Y['hatespeech'])
    not_racism = float(Y['not_racism'])
    racism = float(Y['racism'])
    not_sexism = float(Y['not_sexism'])
    sexism = float(Y['sexism'])
    Flag = ["-","-","-","-"]
    if(bodyshaming > 0.5 and not_bodyshaming < 0.5):
        Flag[0] = 1
    elif(bodyshaming < 0.5 and not_bodyshaming > 0.5):
        Flag[0] = 0
    else :
        Flag[0] = "Inconclusive : body shaming probablity : " + bodyshaming*100 + "percent , non body shaming probablity : " + not_bodyshaming*100
    if(hatespeech > 0.5 and not_hatespeech < 0.5):
        Flag[1] = 1
    elif(hatespeech < 0.5 and not_hatespeech > 0.5):
        Flag[1] = 0
    else :
        Flag[1] = "Inconclusive : hate speech probablity : " + hatespeech*100 + "percent , non hate speech probablity : " + not_hatespeech*100
    if(racism > 0.5 and not_racism < 0.5):
        Flag[2] = 1
    elif(racism < 0.5 and not_racism > 0.5):
        Flag[2] = 0
    else :
        Flag[2] = "Inconclusive : racism probablity : " + racism*100 + "percent , non racism probablity : " + not_racism*100
    if(sexism > 0.5 and not_sexism < 0.5):
        Flag[3] = 1
    elif(sexism < 0.5 and not_sexism > 0.5):
        Flag[3] = 0
    else :
        Flag[3] = "Inconclusive : sexism probablity : " + sexism*100 + "percent , non sexism probablity : " + not_sexism*100
    if 1 in Flag :
        result = "Discriminatory"
    if not 1 in Flag :
        result = "Not Discriminatory"
    if(Flag[0] == 1 ):
        R1 = "Body shaming detected"
    elif(Flag[0] == 0):
        R1 = "Body shaming NOT detected"
    else:
        R1 = Flag[0]
    if(Flag[1] == 1 ):
        R2 = "Hate speech detected"
    elif(Flag[1] == 0):
        R2 = "Hate speech NOT detected"
    else:
        R2 = Flag[1]
    if(Flag[2] == 1 ):
        R3 = "Racism detected"
    elif(Flag[2] == 0):
        R3 = "Racism NOT detected"
    else:
        R3 = Flag[2]
    if(Flag[3] == 1 ):
        R4 = "Sexism detected"
    elif(Flag[3] == 0):
        R4 = "Sexism NOT detected"
    else:
        R4 = Flag[3]
    return render(request, 'result.html' , {'result' : result ,'R1' : R1 ,'R2' : R2 ,'R3' : R3 ,'R4' : R4})