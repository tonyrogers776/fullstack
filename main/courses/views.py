from django.shortcuts import render, redirect
from courses.models import *
from django.contrib import messages


def index(request):
    courses_info = Course.objects.all()
    context = {
        'courses': courses_info
    }
    return render(request, 'index.html', context)

def remove(request, course_id):
    view_course = Course.objects.get(id=course_id)
    context = {
        'course': view_course
    }
    return render(request, 'remove.html', context)

def delete(request, course_id):
    delete_course = Course.objects.get(id=course_id)
    delete_course.delete()
    return redirect('/')

def create(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Course.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
        )
    return redirect('/')

# Create your views here.
