"""
Views module for the profiles app
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


def index(request):
    try:
        """ Render the profiles index page.
        Args:
            request: The HTTP request object
        Returns:
            HttpResponse: The rendered index page.
        """
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(f"Une erreur s'est produite dans profiles/view/index: {e}", exc_info=True)
        raise


def profile(request, username):
    try:
        """ Render a profile page for a given user.
        Args:
            request: The HTTP request object.
            username (str): The username of the profile to retrieve.
        Returns:
            HttpResponse: The rendered profile page.
        """
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.error(f"Une erreur s'est produite dans profiles/view/profile: {e}", exc_info=True)
        raise
