from django.db import models


class Contact(models.Model):
    """ A model for contacting the site owner """
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField()

    def __str__(self):
        return self.email_address
