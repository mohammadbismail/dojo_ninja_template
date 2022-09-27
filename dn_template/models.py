from django.db import models


class Dojo(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    # ninjas=[]


class Ninja(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)

    # this function will return all instances of class Dojo
    # input none
    # output all instances of class Dojo


def getAllDojos():
    return Dojo.objects.all()

    # this function will return the ninjas for specific dojo
    # input: dojo_id
    # output: ninja list for specific dojo id


def getAllNinjas(dojo_id):
    return Dojo.objects.get(id=dojo_id).ninjas.all()

    # this function will recieve input from Dojo HTML form and render it in html
    # input: request from webpage after user input
    # output: instance for Dojo class

def createDojo(request):
    Dojo.objects.create(
        name=request.POST["name"],
        city=request.POST["city"],
        state=request.POST["state"],
    )

def createNinja(request):
    Ninja.objects.create(
        first_name=request.POST["firstname"],
        last_name=request.POST["lastname"],
        dojo=Dojo.objects.get(id=int(request.POST["select"])),
    )
