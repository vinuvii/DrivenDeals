from django.shortcuts import render


def terms_of_use(request):
    return render(request, 'terms_of_use.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')