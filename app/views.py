from django.shortcuts import render

# Create your views here.

def if_cond(request):
    d = {'a':10,'b':20,'c':30,'d':40}
    return render(request,'if_cond.html',d)