#!/usr/bin/python3
""" Defines test cases for the console module
Implement unit tests for console.py.
Handles as many commands as possible
"""

from io import StringIO
import os
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand as hbnb
from models import storage


class TestConsole(TestCase):
    """Test case for the console module.
    """

    def setUp(self):
        """ Setup all test cases"""
        pass

    def tearDown(self):
        """Resets storage for the data in file."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_commands1(self):
        """Tests the following basic commands:
        quit, EOF, ?, help, \n, create, ? create, all etc.
        """
        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("quit")
            self.assertEqual(t.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("EOF")
            self.assertEqual(t.getvalue(), "\n")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("\n")
            self.assertEqual(t.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("?")
            self.assertIsInstance(t.getvalue(), str)

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("help")
            self.assertIsInstance(t.getvalue(), str)

    def test_commands2(self):
        """ Test additional commands for the console"""

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("? create")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("help create")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(), "Creates a new instance.")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("? all")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             "Prints string representation of all instances")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("help all")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             "Prints string representation of all instances")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("? show")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             "Prints string representation of an instance.")

    def test_commands3(self):
        """ Tests more commands for the console."""

        with patch('sys.stdout', new=StringIO()) as t:
            msg = "Prints string representation of an instance."
            hbnb().onecmd("help show")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as t:
            msg = "Updates an instance based on the class name and id."
            hbnb().onecmd("? update")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as t:
            msg = "Updates an instance based on the class name and id."
            hbnb().onecmd("help update")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as t:
            msg = "Deletes an instance based on the class name and id."
            hbnb().onecmd("? destroy")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             msg)

        with patch('sys.stdout', new=StringIO()) as t:
            msg = "Deletes an instance based on the class name and id."
            hbnb().onecmd("help destroy")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(), msg)

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("? quit")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("help quit")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             "Quit command to exit the program.")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("? help")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             "To get help on a command, type help <topic>.")

        with patch('sys.stdout', new=StringIO()) as t:
            hbnb().onecmd("help help")
            self.assertIsInstance(t.getvalue(), str)
            self.assertEqual(t.getvalue().strip(),
                             "To get help on a command, type help <topic>.")
