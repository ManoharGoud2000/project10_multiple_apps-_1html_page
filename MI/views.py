from django.shortcuts import render

# Create your views here.


def Rohit(request):
    d={'Player':'Rohit','Jersey_No': 45 }
    return render(request,'Sample1.html',context=d)