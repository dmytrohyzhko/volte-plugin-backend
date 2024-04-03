from django.db import models
from datetime import datetime, timedelta
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

class ModelUerxLog(models.Model):
    userx_id = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    sid = models.CharField(max_length=250)
    ua = models.CharField(max_length=250)
    ip = models.CharField(max_length=250)
    brandsrc = models.CharField(max_length=250)
    to = models.CharField(max_length=250)
    li = models.CharField(max_length=250)
    result = models.CharField(max_length=250)
    created_at = models.CharField(max_length=250)

    class Meta:
        db_table = "userx_log"

class ModelOptimHubAds(models.Model):
    ads_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    created_at = models.CharField(max_length=250)
    
    class Meta:
        db_table = "optimhub_daily_offers"