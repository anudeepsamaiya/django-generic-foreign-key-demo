from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class UserFollow(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING) 
    object_id = models.CharField(max_length=200)
    content_object = GenericForeignKey("content_type", "object_id")
