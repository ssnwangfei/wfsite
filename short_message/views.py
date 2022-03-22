from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from os import environ

a = 0


def index(request):
    global a
    a = a + 1
    content = f"""
    <html>
    <head>
        <title>
            main page
        </title>
    </head>
    <body background-color=red>
        <font color=blue>
            this is a test page<br/>
            global variable a is: {str(a)}
        </font>

    </body>
</html>


    """
    return HttpResponse(content)


#    return HttpResponse("Hello, world. You're at the polls index.")


from .models import Message
from .models import AppTag
from main.models import UserProfile
from main.models import UserProfile
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User


def send(request):
    """
    :param request:
        from = name
        to   = name
        tag  = ""
        message = ""
    :return:
    """
    context = {}
    return render(request, 'short_message/send.html', context)


def recv(request):
    """
    :param request:
        to = name
        delete_before_date = “”
    :return:
    """
    context = {}
    return render(request, 'short_message/recv.html', context)


def send_action(request):
    #   user_from = request.POST["user_from"]
    #    user_to = request.POST["user_to"]
    #    tag = request.POST["tag"]
    #    message = request.POST["message"]

    user_from = "wf"
    user_to = "wangfei"
    tag = "command"
    message = "hello"

    date = timezone.now()
    response = {}
    error_messages = {}

    ok = True
    try:
        u_from = UserProfile.objects.get(name=user_from)
    except(KeyError, UserProfile.DoesNotExist):
        error_messages["user_from"] = "User not exist"
        ok = False
    else:
        try:
            u_to = UserProfile.objects.get(name=user_to)
        except(KeyError, UserProfile.DoesNotExist):
            error_messages["user_to"] = "User not exist"
            ok = False
        else:
            try:
                apptag = AppTag.objects.get(name=tag)
            except(KeyError, AppTag.DoesNotExist):
                error_messages["tag"] = "Application tag not exist"
                ok = False
            else:
                msg = Message(user_from=u_from.user, user_to=u_to.user, tag=apptag, message=message, date=date)
                msg.save()

    response["error_messages"] = error_messages
    if ok:
        response["status"] = "True"
    else:
        response["status"] = "False"
    return JsonResponse(response)


def recv_action(request):
    response = {"status": 'ok'}

    return JsonResponse(response)


def delete_action(request):
    """
    :param request:
        to = name
        delete_before_date = “”
    :return:
    """
    response = {"status": 'ok'}

    return JsonResponse(response)
