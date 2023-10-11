#!/usr/bin/python3
"""This module defines tests for the BaseModel class"""

import datetime
from models.base_model import BaseModel
import models
import unittest


class TestBaseModel_init(unittest.TestCase):
    """Defines test cases for BaseModel class instantiation"""

    def setUp(self):
        """sets up an instance for testing"""
        self.obj = BaseModel()

    def tearDown(self):
        """clean up, delete an instance after testing"""
        del self.obj

    def test_init_with_no_args(self):
        """instantiate base model with no args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_kwargs_init(self):
        """Test instantiation with key value pair."""
        obj_dict = self.obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(self.obj.id, new_obj.id)
        self.assertEqual(self.obj.created_at, new_obj.created_at)
        self.assertEqual(self.obj.updated_at, new_obj.updated_at)

    def test_obj_is_instance(self):
        """Test new instance is an instance of BaseModel"""
        self.assertIsInstance(self.obj, BaseModel)

    def test_new_instance_in_stored_in_obj(self):
        """Test new instance in storage"""
        self.assertIn(self.obj, models.storage.all().values())

    def test_attr_types(self):
        """Test public instance attributes type"""
        self.assertEqual(datetime.datetime, type(self.obj.updated_at))
        self.assertEqual(datetime.datetime, type(self.obj.created_at))
        self.assertEqual(str, type(self.obj.id))

    def test_uniq_ids(self):
        """Test instances unique ids"""
        new_obj = BaseModel()
        self.assertNotEqual(self.obj.id, new_obj.id)


class TestBase_to_dict(unittest.TestCase):
    """Defines tests cases for the to_dict method"""

    def setUp(self):
        """sets up an instance for testing"""
        self.obj = BaseModel()

    def tearDown(self):
        """clean up, delete an instance after testing"""
        del self.obj

    def test_dict_expected_attr(self):
        """Test dictionary(__dict__) contains
           all expected attributes
        """
        self.assertIn("id", self.obj.__dict__)
        self.assertIn("updated_at", self.obj.__dict__)
        self.assertIn("created_at", self.obj.__dict__)

        # check the __class__ key in the to_dict method
        self.assertEqual("BaseModel", (self.obj.to_dict())["__class__"])

    def test_compare_instances_to_dict_values(self):
        """Test instances dict attribute values if they
           are different or are the same
        """
        # same
        obj_dict = self.obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        new_obj_dict = new_obj.to_dict()
        self.assertEqual(obj_dict, new_obj_dict)

        # difference
        new_obj = BaseModel(obj_dict)
        self.assertNotEqual(self.obj, new_obj)

    def test_attr_type_in_dict(self):
        """Test instance attributes type in a dictionary"""
        test__obj = self.obj.to_dict()
        self.assertEqual("<class 'str'>", str(type((self.obj.
                                                    to_dict())["updated_at"])))
        self.assertEqual("<class 'str'>", str(type(test__obj["created_at"])))
