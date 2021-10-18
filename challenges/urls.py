from django.urls import path
from . import views

urlpatterns = [
    # path("january",views.january),
    path("",views.index,name="index"),
    path('<int:month>',views.monthly_challenges_by_number),  # sequence matter here, int:-> function execute on int value.
    path("<str:month>",views.monthly_challenge,name="monthly_challen") # name is use to get root URL.   
]