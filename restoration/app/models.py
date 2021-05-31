from django.db import models
from django.utils.translation import ugettext_noop

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=200, help_text="Save the name of the input image.")
    datetime = models.DateTimeField(auto_now_add=True)
    input_img = models.ImageField(upload_to="input_image")
    output_img = models.ImageField(upload_to="output_image", blank=True, null=True)