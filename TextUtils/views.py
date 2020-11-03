##Generated file on own -Ayush Nanda

from django.http import HttpResponse

##def index(request):
  ##  return HttpResponse('''<h1>Connect us on Github</h1> <a href="https://github.com/"> GITHUB <a/>''')

##def about(request):
 ##   return HttpResponse("about us")

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("captialize first")