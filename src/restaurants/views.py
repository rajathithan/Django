from django.shortcuts import render

def home(request):
    context = {
            }
    return render(request,"home.html",context)

def works(request):
    context = {
            }
    return render(request,"works.html",context)

def cities(request):
    context = {
            }
    return render(request,"cities.html",context)

def plans(request):
    context = {
            }
    return render(request,"plans.html",context)
