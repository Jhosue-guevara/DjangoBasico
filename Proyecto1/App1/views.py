from django.shortcuts import render

def vista1(request):
    return render(request,"vista.html")
def vista2(request):
    return render(request,"vista2.html")