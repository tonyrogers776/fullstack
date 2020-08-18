from django.shortcuts import render, redirect
from django.contrib import messages
from shows.models import *

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'create.html')

def create(request):
    errors = Show.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
        
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect('/shows')

def delete(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')

def show(request, show_id):
    view_show = Show.objects.get(id=show_id)
    context = {
        'show': view_show
    }
    return render(request, 'show.html', context)

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    errors = Show.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
        
    to_update = Show.objects.get(id=show_id)
    to_update.title = request.POST['title']
    to_update.network = request.POST['network']
    to_update.release_date = request.POST['release_date']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/shows/')
