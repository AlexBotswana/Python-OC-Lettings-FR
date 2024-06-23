# Views module for the lettings app
from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging


logger = logging.getLogger(__name__)


def index(request):
    try:
        """ Render the letting index page.
            Args:
                request: The HTTP request object
            Returns:
                HttpResponse: The rendered index page.
        """
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(f"Une erreur s'est produite dans lettings/view/index: {e}", exc_info=True)
        raise


def letting(request, letting_id):
    try:
        """ Render a letting page (title and adress) for a given letting.
        Args:
            request: The HTTP request object.
            letting_id (int): The letting_id  to retrieve.
        Returns:
            HttpResponse: The rendered letting page.
        """
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.error(f"Une erreur s'est produite dans lettings/view/letting: {e}", exc_info=True)
        raise
