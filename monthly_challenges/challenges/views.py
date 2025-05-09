from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def monthly_challenge(request,month):
    challenge_text = None
    if month == "jan":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "feb":
        challenge_text = "walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for atleast 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)