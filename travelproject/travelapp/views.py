from django.http import HttpResponse
from django.shortcuts import render

from .models import places


# Create your views here.
def demo(request):
    obj = places.objects.all()
    return render(request, "index.html", {'result': obj})

# def addition(request):
#   a = int(request.GET['num1'])
#   b = int(request.GET['num2'])
#   res = a*b
#   return render(request,"result.html",{'result':res})
