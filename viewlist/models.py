from django.db import models
from django.utils import timezone

class Country(models.Model):
    code = models.CharField(max_length=3, blank=False, unique=True)
    name = models.CharField(max_length=60, blank=False)
    is_under_represented = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
    def set_is_under_represented(self, val):
        self.is_under_represented = val

class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=True)
    webpage = models.URLField(blank=True)
    institution = models.CharField(max_length=100, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    position = models.CharField(max_length=30, blank=False)
    grad_date = models.DateField(null=True, blank=True)
    brain_structure = models.CharField(max_length=80, blank=True)
    modalities = models.CharField(max_length=80, blank=True)
    methods = models.CharField(max_length=80, blank=True)
    domain = models.CharField(max_length=80, blank=True)
    keywords = models.CharField(max_length=250, blank=True)
    publish_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ' - '.join([self.name, self.position, self.institution])

class Recommendation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100, blank=False)
    reviewer_email = models.EmailField(blank=False)
    reviewer_position = models.CharField(max_length=30, blank=False)
    reviewer_institution = models.CharField(max_length=100, blank=False)
    seen_at_conf = models.BooleanField()
    comment = models.CharField(max_length=500, blank=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s said '%s' to %s" % (self.reviewer_name, self.comment, self.profile.name)