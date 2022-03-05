from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from os import environ


#global a
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
            this is a test page {str(a)}
        </font>

    </body>
</html>


    """
    return HttpResponse(content)
#    return HttpResponse("Hello, world. You're at the polls index.")