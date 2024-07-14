from django.shortcuts import render


def index(request):
    """ Render the  index page.
            Args:
                request: The HTTP request object
            Returns:
                HttpResponse: The rendered index page.
        """
    return render(request, 'index.html')
