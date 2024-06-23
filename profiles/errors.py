# lettings/errors.py
from django.shortcuts import render


def handler404(request, exception):
    """ Custom handler for 404 errors """
    return render(request, '404.html', status=404)


def handler500(request):
    """ Custom handler for 500 errors """
    return render(request, '500.html', status=500)
