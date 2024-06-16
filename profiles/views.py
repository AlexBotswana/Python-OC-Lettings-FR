# Views module for the profiles app

from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User


def index(request):
    """ Render the profiles index page.
    Args:
        request: The HTTP request object
    Returns:
        HttpResponse: The rendered index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """ Render a profile page for a given user.
    Args:
        request: The HTTP request object.
        username (str): The username of the profile to retrieve.
    Returns:
        HttpResponse: The rendered profile page.
    """
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profiles/profile.html', {'profile': profile})
