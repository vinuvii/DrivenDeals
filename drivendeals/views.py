from django.shortcuts import render

def terms_of_use(request):
    return render(request, 'terms_of_use.html')
