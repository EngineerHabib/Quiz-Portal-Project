from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import *
from .forms import *
from django.forms import inlineformset_factory

def registerPage(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = RegisterForm()
    context = {
        'form':form,
        'title':'Register Here',
        'btn':'Register',
    }
    return render(request, 'auth/baseform.html',context)

def loginPage(request):

    if request.method == "POST":
        form = LoginForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('dashboard')
    form = LoginForm()
    context = {
        'form':form,
        'title':'Login Here',
        'btn':'Login',
    }
    return render(request, 'auth/baseform.html',context)


def logoutPage(request):
    logout(request)
    return redirect('login')

def profilePage(request):

    try:
        user = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        user = Profile.objects.create(user = request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    form = ProfileForm(instance = user)
    context = {
        'form':form,
        'title':'Update Profile',
        'btn':'Update',
    }
    return render(request, 'auth/baseform.html',context)

def dashboardPage(request):

    quiz = QuizModel.objects.all()

    context = {
        'quiz':quiz
    }

    return render(request, 'pages/dashboard.html',context)


def quizPage(request):

    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()

            return redirect('addQuestion', quiz_id = quiz.id)

    form = QuizForm()
    context ={
        'form':form,
        'title':"Add Quiz",
        'btn':"Add",
    }
    return render(request, 'pages/form.html',context)

def addQuestionPage(request, quiz_id):
    quiz = QuizModel.objects.get(id=quiz_id)
    optionFormSet = inlineformset_factory(QuestionModel, OptionModel, form=OptionForm, extra=4,can_delete=False)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz            
            option_form = optionFormSet(request.POST, instance = question)            
            if option_form.is_valid():
                print("saved")
                question.save()
                option_form.save()
                
                

                return redirect('addQuestion', quiz_id = quiz.id)


    
    question_form = QuestionForm()
    option_form = optionFormSet()
    questions = QuestionModel.objects.filter(quiz = quiz_id)
    context ={
        'question_form':question_form,
        'option_form':option_form,
        'questions': questions,
    }


    return render(request, 'pages/addQuestion.html',context)


def examPage(request,quiz_id):
    try:
        user = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        user = Profile.objects.create(user = request.user)
    quiz = QuizModel.objects.get(id = quiz_id)

    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        for ques in questions:
            option_id = request.POST.get(f'q_{ques.id}')
            if option_id:
                try:
                    option = OptionModel.objects.get(id=option_id)
                    if option.is_correct:
                        score += 1
                except OptionModel.DoesNotExist:
                    pass
                
        exam = ExamModel.objects.create(
            participant = user,
            quiz = quiz,
            score = score
        )   

        from django.http import HttpResponse
        return HttpResponse(f"Your Total Score is: {score}")



    context ={
        'questions':questions
    }
    return render(request, 'pages/exam.html',context)

