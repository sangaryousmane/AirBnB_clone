#!/usr/bin/env python3
"""Unit tests for the User class in the user.py module.
"""
import os
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class.
    """

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets the file storage data. checks if the file path exists
        and remove it if it does exist do nothing otherwise.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """ Test all the parameters of the User class"""

        user = User()
        key = "{0}.{1}".format(type(user).__name__, user.id)
        self.assertIn(key, storage.all())
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_init(self):
        """Test all public instances of the User class"""

        user = User()
        user2 = User(**user.to_dict())
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertEqual(user.updated_at, user2.updated_at)

    def test_str(self):
        """Test method for the str representation"""

        user = User()
        str_ = f"[{type(user).__name__}] ({user.id}) {user.__dict__}"
        self.assertEqual(user.__str__(), str_)

    def test_save(self):
        """Test method for the save() method"""

        user = User()
        old_update = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, old_update)

    def test_todict(self):
        """Test method for the to_dict() method"""

        user = User()
        user2 = User(**user.to_dict())
        a_dict = user2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(user2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(user, user2)


if __name__ == "__main__":
    unittest.main()
