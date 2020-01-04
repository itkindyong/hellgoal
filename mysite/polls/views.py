from django.shortcuts import render

# Create your views here.

# 장고 뷰 코드

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

