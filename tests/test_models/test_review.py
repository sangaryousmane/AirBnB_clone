#!/usr/bin/python3
"""Unit tests for the Review class in the review.py module
"""
import os
import unittest
from models.review import Review
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        pass

    def tearDown(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        review = Review()
        review2 = Review("hello", "wait", "in")
        key = f"{type(review).__name__}.{review.id}"
        self.assertIsInstance(review.text, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.place_id, str)
        self.assertEqual(review2.text, "")

    def test_init(self):
        """Test method for public instances"""
        review = Review()
        review2 = Review(**review.to_dict())
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertEqual(review.updated_at, review2.updated_at)

    def test_str(self):
        """Test method for str representation"""
        review = Review()
        str_ = f"[{type(review).__name__}] ({review.id}) {review.__dict__}"
        self.assertEqual(review.__str__(), str_)

    def test_save(self):
        """Test method for save"""
        review = Review()
        old_update = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        review = Review()
        review2 = Review(**review.to_dict())
        a_dict = review2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(review2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(review, review2)


if __name__ == "__main__":
    unittest.main()
