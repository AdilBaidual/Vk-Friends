from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse


@csrf_exempt
def createUser(request, userName):
    if request.method == 'POST':
        mas = User.objects.filter(userName=userName)
        if len(mas) == 0:
            User.objects.create(userName=userName)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)


@csrf_exempt
def createApplication(request, userName1, userName2):
    if request.method == 'POST':
        tmp1 = User.objects.filter(userName=userName1)
        tmp2 = User.objects.filter(userName=userName2)
        if len(tmp1) == 0 or len(tmp2) == 0:
            return HttpResponse(status=400)
        user1 = User.objects.get(userName=userName1)
        user2 = User.objects.get(userName=userName2)
        friendList = user1.friendList.all()
        for i in friendList:
            if user2 == i.friend:
                return HttpResponse(status=401)
        applications = user1.outgoing.all()
        for i in applications:
            if user2 == i.user2:
                return HttpResponse(status=402)
        applications = user1.incoming.all()
        for i in applications:
            if user2 == i.user1:
                FriendList.objects.create(user=user1, friend=user2)
                FriendList.objects.create(user=user2, friend=user1)
                i.delete()
                return HttpResponse(status=200)
        Application.objects.create(user1=user1, user2=user2)
        return HttpResponse(status=200)


@csrf_exempt
def acceptApplication(request, application_id):
    if request.method == 'POST':
        tmp = Application.objects.filter(pk=application_id)
        if len(tmp) == 0:
            return HttpResponse(status=400)
        application = tmp[0]
        user1 = application.user1
        user2 = application.user2
        application.delete()
        FriendList.objects.create(user=user1, friend=user2)
        FriendList.objects.create(user=user2, friend=user1)
        return HttpResponse(status=200)


@csrf_exempt
def refuseApplication(request, application_id):
    if request.method == 'POST':
        tmp = Application.objects.filter(pk=application_id)
        if len(tmp) == 0:
            return HttpResponse(status=400)
        application = tmp[0]
        application.delete()
        return HttpResponse(status=200)


@csrf_exempt
def incomingApplication(request, userName):
    if request.method == 'GET':
        tmp = User.objects.filter(userName=userName)
        if len(tmp) == 0:
            return HttpResponse(status=400)
        user = User.objects.get(userName=userName)
        applications = user.incoming.all()
        mas = []
        for i in applications:
            mas.append([i.pk, i.user1.userName])
        return JsonResponse(mas, safe=False)


@csrf_exempt
def outgoingApplication(request, userName):
    if request.method == 'GET':
        tmp = User.objects.filter(userName=userName)
        if len(tmp) == 0:
            return HttpResponse(status=400)
        user = User.objects.get(userName=userName)
        applications = user.outgoing.all()
        mas = []
        for i in applications:
            mas.append([i.pk, i.user2.userName])
        return JsonResponse(mas, safe=False)


@csrf_exempt
def friendList(request, userName):
    if request.method == 'GET':
        tmp = User.objects.filter(userName=userName)
        if len(tmp) == 0:
            return HttpResponse(status=400)
        user = User.objects.get(userName=userName)
        friendList = user.friendList.all()
        mas = []
        for i in friendList:
            mas.append([i.friend.pk, i.friend.userName])
        return JsonResponse(mas, safe=False)

@csrf_exempt
def status(request, userName1, userName2):
    if request.method == 'GET':
        tmp1 = User.objects.filter(userName=userName1)
        tmp2 = User.objects.filter(userName=userName2)
        if len(tmp1) == 0 or len(tmp2) == 0:
            return HttpResponse(status=400)
        user1 = User.objects.get(userName=userName1)
        user2 = User.objects.get(userName=userName2)
        friendList = user1.friendList.all()
        for i in friendList:
            if user2 == i.friend:
                return JsonResponse("friends", safe=False)
        applications = user1.outgoing.all()
        for i in applications:
            if user2 == i.user2:
                return JsonResponse("outgoing application", safe=False)
        applications = user1.incoming.all()
        for i in applications:
            if user2 == i.user1:
                return JsonResponse("incoming application", safe=False)
        return JsonResponse("nothing", safe=False)


@csrf_exempt
def deleteFriend(request, userName1, userName2):
    if request.method == 'POST':
        tmp1 = User.objects.filter(userName=userName1)
        tmp2 = User.objects.filter(userName=userName2)
        if len(tmp1) == 0 or len(tmp2) == 0:
            return HttpResponse(status=400)
        user1 = User.objects.get(userName=userName1)
        user2 = User.objects.get(userName=userName2)
        friendList = user1.friendList.all()
        for i in friendList:
            if user2 == i.friend:
                i.delete()
                tmp = user2.friendList.all()
                for j in tmp:
                    if user1 == j.friend:
                        j.delete()
                        break
                return HttpResponse(status=200)
        return HttpResponse(status=401)