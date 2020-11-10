##Generated file on own -Ayush Nanda

from django.http import HttpResponse          #while returning normal info return HttpResponse

from django.shortcuts import render           #while using templates

def index(request):
    return render(request, 'index.html')
   # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    #Check checkbox values
    removepunc=request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover=request.GET.get('newlineremover','off')
    spaceremover=request.GET.get('spaceremover','off')
    charactercount=request.GET.get('charactercount','off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)
    
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)

    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="/n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)
    
    elif(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyse.html', params)

    elif(charactercount=='on'):
        analyzed=0
        for char in djtext:
            if char != ' ': #not counting the space as a character
                analyzed +=1


        params = {'purpose':'charactercount', 'analyzed_text':analyzed}
        return render(request, 'analyse.html', params)




    else:
        return HttpResponse('Error')

def navigation(request):
    s= '''<h2> Navigation Bar </h2>
        <a href="https://www.youtube.com/">Youtube </a><br>
        <a href="https://www.google.com/webhp?authuser=3">Google </a><br>
        <a href="https://www.facebook.com/">Facebook</a> <br>'''
    return HttpResponse(s)
