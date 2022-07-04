from django.db import models


class Banner(models.Model):
    """ A model for the info banner """
    info = models.TextField(blank=False, default='Info Banner')

    def __str__(self):
        return self.info
