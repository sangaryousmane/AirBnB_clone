#!/usr/bin/env python3
"""
Unit tests for the Amenity class in the amenity.py module.
"""

import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        pass

    def tearDown(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for public class attributes"""

        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        amenity3 = Amenity("hello", "wait", "in")

        key = "{}.{}".format(type(amenity1).__name__, amenity1.id)
        self.assertIsInstance(amenity1.name, str)
        self.assertIn(key, storage.all())
        self.assertEqual(amenity3.name, "")

    def test_init(self):
        """Test method for public instances"""

        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        self.assertIsInstance(amenity1.id, str)
        self.assertIsInstance(amenity1.created_at, datetime)
        self.assertIsInstance(amenity1.updated_at, datetime)
        self.assertEqual(amenity1.updated_at, amenity2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        amenity = Amenity()
        str_ = f"[{type(amenity).__name__}] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(amenity.__str__(), str_)

    def test_save(self):
        """Test case for the save method"""
        amenity = Amenity()
        old_update = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        amenity1 = Amenity()
        amenity2 = Amenity(**amenity1.to_dict())
        a_dict = amenity2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(amenity2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(amenity1, amenity2)


if __name__ == "__main__":
    unittest.main()
