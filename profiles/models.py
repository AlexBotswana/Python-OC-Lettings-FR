# model of profiles application

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profil utilisateur contenant des informations supplémentaires.

    Attributes:
        user (User): L'utilisateur associé au profil.
        favorite_city (str): La ville préférée de l'utilisateur.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Renvoie le nom d'utilisateur associé au profil.

        Returns:
            str: Nom d'utilisateur.
        """
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"
