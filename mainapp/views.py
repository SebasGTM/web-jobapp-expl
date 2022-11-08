from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader

from mainapp.models import JobPost


# Create your views here.

job_title = [
    "first job",
    "second job",
    "third job",
]

job_desc = [
    "first job descrition",
    "second job descrition",
    "third job descrition",
]


def hello(request):
    # template = loader.get_template("mainapp/hello.html")

    items_list = ["comment", "post", "remark", "option"]
    context = { "name": "django", "age": "33", "is_auth": True, "sections":items_list }
    return render(request, "mainapp/hello.html", context)
    # return HttpResponse(template.render(context, request))

def job_list(request): 
    jobs = JobPost.objects.all()
    context = {
        "joblist" : jobs
    }

    return render(request, "mainapp/job_list.html", context)


def job_detail(request, id):
    job = JobPost.objects.get(id=id)
    context = { "job": job }

    return render(request, "mainapp/job_detail.html", context)