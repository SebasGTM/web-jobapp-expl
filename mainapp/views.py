from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader


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
    # ret_html = "<ul>"
    # for i in range(len(job_title)):
    #     job_url = reverse("job_detail", args=(i,))
    #     ret_html += f"<li><a href='{job_url}'>{i} - {job_title[i]}<a><p>{job_desc[i]}<p></li>"

    # ret_html += "<ul>"
    job_list = []
    for idx in range(len(job_title)):
        job_list.append({ "id":idx, "title":job_title[idx], "description": job_desc[idx] })

    context = {
        "joblist" : job_list
    }

    return render(request, "mainapp/job_list.html", context)


def job_detail(request, id):
    context = { "id":id, "job_title":job_title[id], "job_desc":job_desc[id] }

    return render(request, "mainapp/job_detail.html", context)