from django.db import models
from django.contrib.auth.models import User

class Job(models.Model): #company, title, location, date range
    user = models.ForeignKey(User)
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_start = models.DateField(auto_now=False)
    date_end = models.DateField(auto_now=False)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username