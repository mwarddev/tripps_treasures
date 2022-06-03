from django.db import models


class Newsletter(models.Model):
    """ A model for newsletter registration """
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    agree_policy = models.BooleanField(default=False, null=True, blank=True)
