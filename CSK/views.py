from django.shortcuts import render

# Create your views here.


def Dhoni(request):
    d={'Player':'Dhoni','Jersey_No': 7}
    return render(request,'Sample1.html',context=d)