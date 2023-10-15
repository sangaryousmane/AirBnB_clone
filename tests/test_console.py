#!/usr/bin/python3
""" Test class for the console module
"""
from unittest import TestCase
from models import storage
from os import path, remove
from unittest import mock.patch
from console import HBNBCommand as hbnb


class TestConsole(TestCase):
    """ Test case for the console module
    """

    def setUp(self):
        """ set up all test cases"""
        pass


    def tearDown(self):
        """unit test to reset the storage file
        """
        storage._FileStorage__objects = {}
        if path.exists(storage._FileStorage__objects):
            remove(storage._FileStorage__objects)

    def test_commands(self):
        """ Test the following console commands:
        ?, \n, EOF, and the quit command"""

        with mock.patch('sys.stdout', new=StringIO()) as t:
            hbnb.onecmd("EOF")
            self.assertEqual(t.getValue(), "\n")

        with mock.path('sys.stdout', new=StringIO()) as t:
            hbnb.onecmd("\n")
            self.assertEqual(t.getValue(), "")

        with mock.path('sys.stdout', new=StringIO()) as t:
            hbnb.onecmd("?")
            self.assertIsInstance(t.getValue(), str)

        with mock.path('sys.stdout', new=StringIO()) as t:
            hbnb.onecmd("quit")
            self.assertEqual(t.getValue(), "")

    def test_commands2(self):
        """ Test commands to handle create, destroy and show
        """

        with mock.patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("? create")
            self.assertIsInstance(t.getValue(), str)
            self.assertEqual(t.getValue().strip(), "Create a new instance")

        with mock.patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("help create")
            self.assertIsInstance(t.getValue(), str)
            self.assertEqual(t.getValue(), "Create a new instance")

        with mock.patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("? show")
            self.assertIsInstance(t.getValue(), str)
            self.assertEqual(t.getValue().strip(), "Prints the string rep of an instance")

        with mock.patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("help show")
            self.assertIsIntance(t.getValue(), str)
            self.assertEqual(t.getValue().strip, "Prints the string rep of an instance")

        with mock.patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("? destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(),
                             "Deletes an instance based on the class name and id")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("help destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(f.getvalue().strip(), 
                             "Deletes an instance based on the class name and id")
