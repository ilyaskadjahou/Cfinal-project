from django.shortcuts import render
from .models import Question, Choice, Submission


def submit(request, course_id):
    questions = Question.objects.all()
    context = {
        'questions': questions,
        'course_id': course_id
    }
    return render(request, 'onlinecourse/course_details_bootstrap.html', context)


def show_exam_result(request, course_id):
    score = 100
    context = {
        'score': score,
        'course_id': course_id
    }
    return render(request, 'onlinecourse/exam_result.html', context)
