from django.db import models
import json
import uuid
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import django.core.serializers
from django.utils import timezone

# Create your models here.
class ModelUserx(models.Model):

    extension_id = models.CharField(max_length=250)
    project_id = models.CharField(max_length=250)
    ip = models.CharField(max_length=250)
    user_agent = models.CharField(max_length=250)
    installed_at = models.DateTimeField(default=timezone.now)
    uninstalled_at = models.DateTimeField(blank=True, null=True)
    lastseen_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "userx"

# Create your models here.
class ModelProject(models.Model):

    title = models.CharField(max_length=250)
    # is_epic = models.CharField(max_length=250)
    # short_description = models.DateTimeField(max_length=250)
    # long_description = models.DateTimeField(max_length=250)
    # image = models.DateTimeField(max_length=250)
    # home_image = models.DateTimeField(max_length=250)
    status = models.IntegerField()

    class Meta:
        db_table = "projects"