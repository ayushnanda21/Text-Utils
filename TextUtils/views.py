##Generated file on own -Ayush Nanda

from django.http import HttpResponse          #while returning normal info return HttpResponse

from django.shortcuts import render           #while using templates

def index(request):
    return render(request, 'index.html')
   # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)

    else:
        return HttpResponse('Error')