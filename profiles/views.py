from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User


def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profiles/profile.html', {'profile': profile})
