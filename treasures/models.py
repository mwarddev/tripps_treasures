from django.db import models


class Category(models.Model):
    """ Product category model """
    class Meta:

        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Treasure(models.Model):
    """ Products model """
    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    description = models.TextField()
    sizable = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    personalise = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    """ Image model to allow multiple images per Treasure (product) """
    treasure = models.ForeignKey(Treasure,
                                 on_delete=models.CASCADE,
                                 related_name='images')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.image
