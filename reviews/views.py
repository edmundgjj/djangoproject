from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Reviews app")
    return render(request, 'reviews/index.template.html')