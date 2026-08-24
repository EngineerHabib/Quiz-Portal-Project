from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logout'),
    path('', loginPage, name='login'),
    path('dashboard/', dashboardPage, name='dashboard'),
    path('profile/', profilePage, name='profile'),
    path('quiz/', quizPage, name='quiz'),
    path('addQuestion/<str:quiz_id>/', addQuestionPage, name='addQuestion'),
    path('exam/<str:quiz_id>/', examPage, name='exam'),
]
