from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string 

import challenges
# Create your views here.

monthly_challenges = {
    'january' : "Eat no meat for entire month. JAN",
    'february': "This is february URL",
    'march' : "Eat meat for entire month. MAR",
    'april' : None,
    'may' : "Eat no meat for entire month. MAY",
    'june' : "This is june URL",
    'july' : "Eat meat for entire month. JULY",
    'august' : "Eat no meat for entire month AUG.",
    'september' : None,
    'octobar' : "This is octobar URL",
    'november' : "Eat meat for entire month. NOV",
    'december' :"This is december URL"
}

# def january(request):
#     return HttpResponse("Eat no meat for entire month.")

# def monthly_challenges_by_number(request,month):
#     challenge_text = None

#     if month == 1:
#         challenge_text = "Eat no meat for entire month.";
#     elif month == 2:
#         challenge_text = "This is february URL"
#     elif month == 3:
#         challenge_text = "Eat meat for entire month.";
#     else:
#         return HttpResponseNotFound("This month is not supported.")
#     return HttpResponse(challenge_text);

def get_months():
    return list(monthly_challenges.keys())

def index(request):
    list_items = ""
    months = get_months()
    return render(request,"challenges/index.html",{
        'months':months
    })
    # for month in months:
    #     captilised_month = month.capitalize()
    #     month_path = reverse("monthly_challen",args=[month,])
    #     list_items += f'<li><h3><a href="{month_path}">{captilised_month}</a></h3></li>'
    
    # response_data = f'<ul>{list_items}</ul>'
    # return HttpResponse(response_data)

def monthly_challenges_by_number(request,month):    
    months = get_months()
    if month > len(months) :
        return HttpResponseNotFound("Invalid month.")
    
    redirect_month = months[month-1]
    redirect_path = reverse("monthly_challen",args=[redirect_month,])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            'text':challenge_text,
            'month':month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data);
    except:
        raise Http404()  # it search 404.html file in ur templates.
        # response_data =  render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
    # response_data = f'<h1>{challenge_text}</h1>'
    