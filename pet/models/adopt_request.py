from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

from .user import User
from .pet import Pet


class AdoptRequest(models.Model):
    adopt = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    pet = models.ForeignKey(Pet, null=True, on_delete=models.SET_NULL)
    adopter_first_name = models.CharField(max_length=100, null=True, blank=True)
    adopter_last_name = models.CharField(max_length=100, null=True, blank=True)
    adopter_age = models.IntegerField(null=True, blank=True)
    adopter_address = models.CharField(max_length=100, null=True, blank=True)
    adopt_reason = models.CharField(max_length=1000, null=True, blank=True)
    accept_for_interviewing = models.BooleanField(default=False)
    request_date = models.DateTimeField(default=timezone.now)
    
