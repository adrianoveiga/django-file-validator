# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.files import File
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from .models import FooModel
from django.conf import settings
 
class TestMaxSizeFileValidator(TestCase):
 
    def test_image_default_size_exceeds_limits(self):
        foomodel = FooModel(description="foomodeltest")
        file_path = "{}{}".format(settings.BASE_DIR, "/fooapp/sample_files/bigboard.bmp")
        foomodel.image = File(open(file_path))
        exceeds_limits = False
        try:
            foomodel.full_clean()
        except ValidationError as e:
            exceeds_limits = True
        self.assertEqual(exceeds_limits, True)

    def test_image_custom_size_exceeds_limits(self):
        foomodel = FooModel(description="foomodeltest")
        file_path = "{}{}".format(settings.BASE_DIR, "/fooapp/sample_files/board.jpg")
        foomodel.small_image = File(open(file_path))
        exceeds_limits = False
        try:
            foomodel.full_clean()
        except ValidationError as e:
            exceeds_limits = True
        self.assertEqual(exceeds_limits, True)

    def test_image_default_size_fit_limits(self):
        foomodel = FooModel(description="foomodeltest")
        file_path = "{}{}".format(settings.BASE_DIR, "/fooapp/sample_files/board.jpg")
        foomodel.image = File(open(file_path))
        exceeds_limits = False
        try:
            foomodel.full_clean()
        except ValidationError as e:
            exceeds_limits = True
        self.assertEqual(exceeds_limits, False)
        foomodel.save()
        self.assertEqual(default_storage.exists('uploads/foomodel/img/board.jpg'), True)

    def test_image_custom_size_fit_limits(self):
        foomodel = FooModel(description="foomodeltest")
        file_path = "{}{}".format(settings.BASE_DIR, "/fooapp/sample_files/bigboard.bmp")
        foomodel.big_image = File(open(file_path))
        exceeds_limits = False
        try:
            foomodel.full_clean()
        except ValidationError as e:
            exceeds_limits = True
        self.assertEqual(exceeds_limits, False)
        foomodel.save()
        self.assertEqual(default_storage.exists('uploads/foomodel/img/bigboard.bmp'), True)


