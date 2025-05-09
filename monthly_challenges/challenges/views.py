from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Practice mindfulness for 10 minutes every day!",
    "may": "Try a new vegetable recipe each week!",
    "june": "Read for at least 30 minutes every day!",
    "july": "Volunteer for a local charity once a week!",
    "august": "Start a journal and write daily!",
    "september": "Learn a new language for at least 15 minutes every day!",
    "october": "Participate in a daily gratitude challenge!",
    "november": "Limit screen time to 1 hour a day!",
    "december": "Reflect on your year and set goals for next year!"
}

# Create your views here.

def monthly_challenge_by_number(request,month):
    return HttpResponse(month)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    