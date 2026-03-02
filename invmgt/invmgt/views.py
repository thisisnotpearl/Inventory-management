from django.http import HttpResponse

def homepage(request):
    return HttpResponse('This is home page')