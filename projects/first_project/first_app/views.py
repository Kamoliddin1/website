from django.shortcuts import render


def index(request):
    return render(request, 'first_app/homePage.html')


def contact(request):
    my_dict = {'content': ["If you have questions please call me", '(97)777-77-77']}
    return render(request, 'first_app/base.html', my_dict)
