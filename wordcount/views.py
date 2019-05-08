from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    text = request.POST['texttocount']
    wordlist = text.split()
    wrddict ={}
    for word in wordlist:
        if word in wrddict:
            wrddict[word] +=1
        else:
            wrddict[word] =1
    return render(request, 'count.html',{'text':text,'length':len(text),'worddict':wrddict})

def about(request):
    return render(request,'about.html')
