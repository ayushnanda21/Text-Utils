##Generated file on own -Ayush Nanda

from django.http import HttpResponse          #while returning normal info return HttpResponse

from django.shortcuts import render           #while using templates

def index(request):
    return render(request, 'index.html')
   # return HttpResponse("Home")

def analyse(request):

    # Get the text
    djtext = request.GET.get('text', 'default')
    analysed=djtext
    params = {'purpose': "Removing Punctuations", 'analysed_text': analysed}
    return render(request,'analyse.html',params)