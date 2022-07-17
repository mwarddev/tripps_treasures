from django.db import models


class Contact(models.Model):
    """ A model for contacting the site owner """
    cust_name = models.CharField(max_length=100, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Order messages by date """
        ordering = ['-message_date']

    def __str__(self):
        return self.cust_name
