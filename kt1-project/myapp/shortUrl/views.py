import datetime
import random
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

def createShortUrl(request):
    if request.method == "GET":
        return render(request,"shortUrl/create.html",{"form":UrlCreationForm()})
    elif request.method == "POST":
        try:
            data_list = "abcdefghijklmnopqrstuvwxyz1234567890"
            form_data = UrlCreationForm(request.POST).data
            
            url = form_data["url"]
            shortCode = "".join(random.choices(data_list, k=5))
            ShortenUrl.objects.create(url=url,shortCode=shortCode)
            return HttpResponse("201 Created "+url)
        except:
            return HttpResponse("400 Bad Request")

def getUrl(request,shortCode):
    try:
        shortenUrl = ShortenUrl.objects.get(shortCode=shortCode)
        shortenUrl.accessCount+=1
        shortenUrl.save()
        return HttpResponse("200 OK "+shortenUrl.url)
    except:
        return HttpResponse("404 Not Found")
        
    
    

def UpdateShortUrl(request,shortCode):
    try:
        shortenUrl = ShortenUrl.objects.filter(shortCode=shortCode)
    except:
        return HttpResponse("404 Not Found")
    
    if request.method == "GET":
        return render(request,"shortUrl/update.html",{"form":UrlUpdateForm()})
    
    elif request.method == "POST":
        try:
            form_data = UrlCreationForm(request.POST).data
            
            url = form_data["url"]
            shortenUrl.update(url=url,updatedAt=datetime.datetime.now())
            return HttpResponse("200 OK Updated "+url)
        except:
            return HttpResponse("400 Bad Request")

def DeleteShortUrl(request,shortCode):
    try:
        shortenUrl = ShortenUrl.objects.get(shortCode=shortCode)
    except:
        return HttpResponse("404 Not Found")
        
    if request.method == "GET":
        return render(request,"shortUrl/delete.html",{"url":shortenUrl.url})
    
    elif request.method == "POST":
        try:
            shortenUrl.delete()
            return HttpResponse("204 No Content")
        except:
            return HttpResponse("400 Bad Request")

def ShortUrlStats(request,shortCode):
    try:
        shortenUrl = ShortenUrl.objects.get(shortCode=shortCode)
    except:
        return HttpResponse("404 Not Found")
    
    if request.method == "GET":
        return render(request,"shortUrl/stats.html",{"shortenUrl":shortenUrl})