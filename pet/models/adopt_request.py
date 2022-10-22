from email.policy import default
from django.db import models
from django.utils import timezone

from .user import User
from .pet import Pet


class AdoptRequest(models.Model):
    adopt = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    pet = models.ForeignKey(Pet, null=True, on_delete=models.SET_NULL)
    accept_for_interviewing = models.BooleanField(default=False)
    request_date = models.DateTimeField(default=timezone.now)
    
