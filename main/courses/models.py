from django.db import models

class CourseManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name must be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "course description must be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

# Create your models here.
