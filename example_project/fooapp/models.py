from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_file_validator.validators import MaxSizeValidator

# Create your models here.
class FooModel(models.Model):
    description = models.CharField(verbose_name=_(u"Description"),  max_length=200)
    image = models.FileField(verbose_name=_(u"Image"),upload_to='uploads/foomodel/img/', null=True, blank=True, validators=[MaxSizeValidator()])
    big_image = models.ImageField(verbose_name=_(u"Big Image"), null=True, blank=True, upload_to='uploads/foomodel/img/', validators=[MaxSizeValidator(1024)])
    small_image = models.ImageField(verbose_name=_(u"Small Image"), null=True, blank=True, upload_to='uploads/foomodel/img/', validators=[MaxSizeValidator(60)])