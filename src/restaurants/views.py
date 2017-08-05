from django.shortcuts import render

def home(request):
    itemslist = [
        "eggs",
        "cornflakes",
        "coke",
        "toothpaste",
        "brush",
        "spinach"
    ]
    context = {
        "bool_item": False,
        "itemslist": itemslist,
    }

    return render(request,"base.html",context)


