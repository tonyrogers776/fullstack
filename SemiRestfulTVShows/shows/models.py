from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['title']) <2:
            errors['title'] = 'Title field should be at least 2 characters.'
        if len(form['network']) <3:
            errors['network'] = 'Network field should be at least 3 characters.'
        if form['description'] != '' and len(form['description']) < 10:
            errors['description'] = 'Description should be at least 10 characters'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

# Create your models here.
