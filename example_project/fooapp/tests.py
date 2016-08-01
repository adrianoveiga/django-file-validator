# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.files import File
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from .models import FooModel
 
class TestMaxSizeFileValidator(TestCase):
 
    def test_image_default_size_exceeds_limits(self):
        foomodel = FooModel(description="foomodeltest")
        foomodel.image = File(open("fooapp/sample_files/bigboard.bmp"))
        exceeds_limits = False
        try:
            foomodel.full_clean()
        except ValidationError as e:
            exceeds_limits = True
        self.assertEqual(exceeds_limits, True)

    def test_image_custom_size_exceeds_limits(self):
        foomodel = FooModel(description="foomodeltest")
        foomodel.small_image = File(open("fooapp/sample_files/board.jpg"))
        exceeds_limits = False
        try:
            foomodel.full_clean()
        except ValidationError as e:
            exceeds_limits = True
        self.assertEqual(exceeds_limits, True)

    def test_image_default_size_fit_limits(self):
        foomodel = FooModel(description="foomodeltest")
        foomodel.image = File(open("fooapp/sample_files/board.jpg"))
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
        foomodel.big_image = File(open("fooapp/sample_files/bigboard.bmp"))
        exceeds_limits = False
        try:
            foomodel.full_clean()
        except ValidationError as e:
            exceeds_limits = True
        self.assertEqual(exceeds_limits, False)
        foomodel.save()
        self.assertEqual(default_storage.exists('uploads/foomodel/img/bigboard.bmp'), True)


