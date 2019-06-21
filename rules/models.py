from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from rest_auth.models import UserFollow

class Rule(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    follower = GenericRelation(UserFollow, related_query_name="rules")
