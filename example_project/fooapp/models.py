from django.db import models
from django_file_validator.validators import MaxSizeValidator

# Create your models here.
class FooModel(models.Model):
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to='uploads/foomodel/img/', null=True, blank=True, validators=[MaxSizeValidator()])
    big_image = models.ImageField( null=True, blank=True, upload_to='uploads/foomodel/img/', validators=[MaxSizeValidator(1024)])
    small_image = models.ImageField( null=True, blank=True, upload_to='uploads/foomodel/img/', validators=[MaxSizeValidator(60)])