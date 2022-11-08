from random import choices
from django.utils.text import slugify
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=200)
    proficiency = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    street  = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)

    def __str__(self):
        return self.country + " | " + self.city

class Author(models.Model):
    name = models.CharField(max_length=220)
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " | " + self.company

# Create your models here.
class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ("Full time", "Full time"),
        ("Part time", "Part Time"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    type = models.CharField(max_length=200, null=False, choices=JOB_TYPE_CHOICES)
    expiry = models.DateField(null=True, blank=True)
    slug = models.SlugField(null=True, max_length=40, unique=True)
    
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    required_skills = models.ManyToManyField(Skill, blank=True)


    def __str__(self):
        return str(self.id) + "|" + self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)


