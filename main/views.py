from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275771',
        'name': 'Valentino Kim Fernando',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)