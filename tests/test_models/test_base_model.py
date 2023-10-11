#!/usr/bin/python3
"""This module defines tests for the BaseModel class"""

from datetime import datetime
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

    def test_new_instance_stored_in_obj(self):
        """Test new instance in storage"""
        self.assertIn(self.obj, models.storage.all().values())

    def test_attr_types(self):
        """Test public instance attributes type"""
        self.assertEqual(datetime, type(self.obj.updated_at))
        self.assertEqual(datetime, type(self.obj.created_at))
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

    def test_to_dict_expected_attr(self):
        """Test dictionary(__dict__) contains
           all expected attributes
        """
        self.assertIn("id", self.obj.__dict__)
        self.assertIn("updated_at", self.obj.__dict__)
        self.assertIn("created_at", self.obj.__dict__)

        # check the __class__ key in the to_dict method
        self.assertEqual("BaseModel", (self.obj.to_dict())["__class__"])

    def test_to_dict_added_attr_check(self):
        """Test dictionary(__dict__) contains added attribute(s)"""
        self.obj.name = "Genesis"
        self.obj.fav_num = 22
        self.assertIn("name", self.obj.__dict__)
        self.assertIn("fav_num", self.obj.__dict__)

    def test_compare_instances_to_dict_values(self):
        """Test instances dict attribute values if they
           are different or are the same
        """
        # same
        obj_dict = self.obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        new_obj_dict = new_obj.to_dict()
        self.assertEqual(obj_dict, new_obj_dict)

        # different
        new_obj = BaseModel(obj_dict)
        self.assertNotEqual(self.obj, new_obj)

    def test_attr_type_in_to_dict(self):
        """Test instance attributes type in a dictionary"""
        test__obj = self.obj.to_dict()
        self.assertEqual("<class 'str'>", str(type((self.obj.
                                                    to_dict())["updated_at"])))
        self.assertEqual("<class 'str'>", str(type(test__obj["created_at"])))

    def test_to_dict_type(self):
        """Test the type return from the to_dict method"""
        self.assertTrue(dict, type(self.obj.to_dict()))

    def test_to_dict_output(self):
        """Test the to_dict return dictionary output """
        dict_time = datetime.today()
        self.obj.created_at = self.obj.updated_at = dict_time
        output = {
            'id': self.obj.id,
            '__class__': self.obj.__class__.__name__,
            'created_at': dict_time.isoformat(),
            'updated_at': dict_time.isoformat()
        }
        self.assertDictEqual(self.obj.to_dict(), output)
