import os
import time
import json

from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render

from .agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
from pusher import Pusher


# Instantiate a Pusher Client
# pusher_client = Pusher(app_id=os.environ.get('PUSHER_APP_ID'),
#                        key=os.environ.get('PUSHER_KEY'),
#                        secret=os.environ.get('PUSHER_SECRET'),
#                        ssl=True,
#                        cluster=os.environ.get('PUSHER_CLUSTER')
#                        )

pusher_client = Pusher(app_id='1706831',
                       key='b078517087452a8bc4ce',
                       secret='33d3d79227d0b026fc91',
                       ssl=True,
                       cluster='eu'
                       )


@login_required()
def index(request):
    all_users = User.objects.exclude(id=request.user.id).only('id', 'username').filter(is_staff=True)
    return render(request, 'agora/index.html', {'allUsers': all_users})


def pusher_auth(request):
    payload = pusher_client.authenticate(
        channel=request.POST['channel_name'],
        socket_id=request.POST['socket_id'],
        custom_data={
            'user_id': request.user.id,
            'user_info': {
                'id': request.user.id,
                'name': request.user.username
            }
        })
    return JsonResponse(payload)


def generate_agora_token(request):
    # appID = os.environ.get('AGORA_APP_ID')
    appID = '59a36a4eac7c4f05b2f7dcc074aded53'
    # appCertificate = os.environ.get('AGORA_APP_CERTIFICATE')
    appCertificate = '3d9a7b9617674556a1455a6e5769cc1d'
    channelName = json.loads(request.body.decode(
        'utf-8'))['channelName']
    userAccount = request.user.username
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds
    print(appID)

    token = RtcTokenBuilder.buildTokenWithAccount(
        appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

    return JsonResponse({'token': token, 'appID': appID})


def call_user(request):
    body = json.loads(request.body.decode('utf-8'))

    user_to_call = body['user_to_call']
    channel_name = body['channel_name']
    caller = request.user.id

    pusher_client.trigger(
        'presence-online-channel',
        'make-agora-call',
        {
            'userToCall': user_to_call,
            'channelName': channel_name,
            'from': caller
        }
    )
    return JsonResponse({'message': 'call has been placed'})