from django.shortcuts import render, redirect
from dn_template import models

# from .models import Dojo, Ninja


def index(request):

    context = {
        "dojos": models.getAllDojos(),
    }

    return render(request, "index.html", context)


def addDojo(request):

    models.createDojo(request)

    return redirect("/")


def addNinja(request):

    models.createNinja(request)

    return redirect("/")
