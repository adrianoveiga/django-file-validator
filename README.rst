
django-file-validator
------------------------

 Simple project to validate FileFields/ImageFields, like max size of uploaded file.
 Until now, there is only one validator: max_size_validator.


Dependencies
------------

- Django 1.8 or higher (not tested on previous versions)


Installation
------------

.. code-block:: python

   pip install django-file-validator


Usage
-----

In your models, import and use max_size_validator:

.. code-block:: python

    from django_file_validator.validators import max_size_validator

    class YourModle(models.Model):
        
        . . .

        image = models.ImageField( null=True, blank=True, upload_to='uploads/mymodel/img/', validators=[max_size_validator()])

        . . . 


You can change the max size value passing a parameter on each attibute:

.. code-block:: python

    from django_file_validator.validators import max_size_validator

    class YourModle(models.Model):
        
        . . .

        default_image = models.ImageField( null=True, blank=True, upload_to='uploads/mymodel/img/', validators=[max_size_validator()])
        big_image = models.ImageField( null=True, blank=True, upload_to='uploads/mymodel/img/', validators=[max_size_validator(2048)])
        small_image = models.ImageField( null=True, blank=True, upload_to='uploads/mymodel/img/', validators=[max_size_validator(256)])

        . . . 



Configurations
--------------

- FILE_SIZE_LIMIT_IN_KILOBYTES
    You can change the default max size limit of uploaded files, just putting this variable on settings.py. 

    .. code-block:: python
        
        FILE_SIZE_LIMIT_IN_KILOBYTES=512

