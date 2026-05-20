from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('leaderboard/',
         views.leaderboard,
         name='leaderboard'),

    path('submit/<int:problem_id>/',
         views.submit_solution,
         name='submit'),
]