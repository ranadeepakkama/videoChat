from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse 
from agora_token_builder import RtcTokenBuilder
from .models import NewMember
import random
import time
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return render(request,'indx.html')
   

def room(request):
    return render(request,'room.html')

def video(request):
    return render(request,'video.html')

def getToken(request):
    appId = '2484384339cf4d0eb635c99e1bc78a5a'
    appCertificate = 'abd9043c4c1e40e1ad01ea68e21520f7'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds

    role = 1
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token': token, 'uid': uid}, safe=False)

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)

    member, created = NewMember.objects.get_or_create(
        name = data['name'],
        uid = data['uid'],
        room_name=data['room_name']
    )
    return JsonResponse({'name': data['name']},safe=False)

def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = NewMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

def delete(request,id):
    data = get_object_or_404(NewMember, id=id)
    data.delete()
    return redirect('home')

def listItems(request):
    data = NewMember.objects.all()
    context = {'data': data}
    return render(request,'list.html',context)