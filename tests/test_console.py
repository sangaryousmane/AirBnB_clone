#!/usr/bin/python3
""" Defines test cases for the console module
Implement unit tests for console.py.
Handles as many commands as possible
"""

import json
from io import StringIO
import os
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestConsole_help(TestCase):
    """Test help messages for commands of the HBNB interpreter"""

    def test_help_EOF(self):
        """Test the correct output of the EOF
        command help documentation
        """
        msg = "Exits the program after receiving EOF signal.\n"
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help EOF")
        self.assertEqual(msg, cpt_out.getvalue())

    def test_help_all(self):
        """Test the correct output of the all
        command help documentation
        """
        msg = "Prints string representation of all instances\n"
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help all")
        self.assertEqual(msg, cpt_out.getvalue())

    def test_help_count(self):
        """Test the correct output of the count
        command help documentation
        """
        msg = "Retrieve the number of instances of a class\n"
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help count")
        self.assertEqual(msg, cpt_out.getvalue())

    def test_help_create(self):
        """Test the correct output of the create
        command help documentation
        """
        msg = "Creates a new instance.\n"
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help create")
        self.assertEqual(msg, cpt_out.getvalue())

    def test_help_destroy(self):
        """Test the correct output of the destroy
        command help documentation
        """
        msg = "Deletes an instance based on the class name and id.\n"
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help destroy")
        self.assertEqual(msg, cpt_out.getvalue())

    def test_help(self):
        """Tests Test the correct output of the help
        command help documentation.
        """
        with patch('sys.stdout', new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help")
        s = "\nDocumented commands (type help <topic>):\n"\
            "========================================\n"\
            "EOF  all  count  create  destroy  help  quit  show  update\n\n"
        self.assertEqual(s, cpt_out.getvalue())

    def test_help_quit(self):
        """Test the correct output of the quite
        command help documentation
        """
        msg = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(msg, cpt_out.getvalue().strip())

    def test_help_show(self):
        """Test the correct output of the show
        command help documentation
        """
        msg = "Prints string representation of an instance.\n"
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help show")
        self.assertEqual(msg, cpt_out.getvalue())

    def test_help_update(self):
        """Test the correct output of the update
        command help documentation
        """
        msg = "Updates an instance based on the class name and id.\n"
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("help update")
        self.assertEqual(msg, cpt_out.getvalue())


class TestConsole_prompt(TestCase):
    """Tests HBNB interpreter """

    def test_prompt(self):
        """test hbnb for correct prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """test empty line for correct output"""
        with patch("sys.stdout", new=StringIO()) as cpt_out:
            HBNBCommand().onecmd("")
            self.assertEqual("", cpt_out.getvalue().strip())


class TestBaseModel(TestCase):
    """ Test cases for the Base Model"""

    def test_basemodel_dot_create(self):
        """ Test BaseModel.create() case"""

        with patch('sys.stdout', new=StringIO()) as bc:
            HBNBCommand().onecmd(HBNBCommand().default(
                                 'BaseModel.create()'))
            self.assertIsInstance(bc.getvalue().strip(), str)
            self.assertIn("BaseModel.{}".format(
                bc.getvalue().strip()), storage.all().keys())


class User(TestCase):
    """ test cases for the User module"""

    def test_create_user(self):
        """Test create user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 'User.create()'))
            self.assertIsInstance(f.getvalue().strip(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_count_user(self):
        """Test count user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.count()'))
            count = 0
            for i in storage.all().values():
                if type(i) == User:
                    count += 1
            self.assertEqual(int(f.getvalue()), count)

    def test_all_user(self):
        """Test the all User case.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(HBNBCommand().precmd('User.all()'))
            for i in json.loads(f.getvalue()):
                self.assertEqual(i.split()[0], '[User]')

    def test_show_user(self):
        """Test show user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.eyes = "red"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.show({user.id})'))
            result = f"[{type(user).__name__}] ({user.id}) {user.__dict__}"
            self.assertEqual(f.getvalue().strip(), result)

    def test_update_user(self):
        """Test update user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.name = "Ousmane"
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({user.id}, name, "Ousmane")'))
            self.assertEqual(user.__dict__["name"], "Ousmane")

        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.age = 24
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.update({user.id}, age, 24)'))
            self.assertIn("age", user.__dict__.keys())
            self.assertEqual(user.__dict__["age"], 24)

        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.age = 24
            cmmd = f'User.update({user.id}, age, 10, color, green)'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertIn("age", user.__dict__.keys())
            self.assertNotIn("color", user.__dict__.keys())
            self.assertEqual(user.__dict__["age"], 24)

    def test_update_user_dict(self):
        """Test update user object.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            user = User()
            user.age = 24
            cmmd = f'User.update({user.id}, {{"age": 24,"color":"green"}})'
            HBNBCommand().onecmd(HBNBCommand().precmd(cmmd))
            self.assertEqual(user.__dict__["age"], 24)
            self.assertIsInstance(user.__dict__["age"], int)

    def test_destroy_user(self):
        """Test destroy user object.
        """
        with patch('sys.stdout', new=StringIO()):
            user = User()
            HBNBCommand().onecmd(HBNBCommand().precmd(
                                 f'User.destroy({user.id})'))
            self.assertNotIn("User.{}".format(
                user.id), storage.all().keys())

# class TestConsole(TestCase):
#     """Test case for the console module.
#     """
#
#     def setUp(self):
#         """ Setup all test cases"""
#         pass
#
#     def tearDown(self):
#         """Resets storage for the data in file."""
#         storage._FileStorage__objects = {}
#         if os.path.exists(storage._FileStorage__file_path):
#             os.remove(storage._FileStorage__file_path)
#
#     def test_commands1(self):
#         """Tests the following basic commands:
#         quit, EOF, ?, help, \n, create, ? create, all etc.
#         """
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("quit")
#             self.assertEqual(t.getvalue(), "")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("EOF")
#             self.assertEqual(t.getvalue(), "\n")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("\n")
#             self.assertEqual(t.getvalue(), "")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("?")
#             self.assertIsInstance(t.getvalue(), str)
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("help")
#             self.assertIsInstance(t.getvalue(), str)
#
#     def test_commands2(self):
#         """ Test additional commands for the console"""
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("? create")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(), "Creates a new instance.")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("help create")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(), "Creates a new instance.")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("? all")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              "Prints string representation of all instances")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("help all")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              "Prints string representation of all instances")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("? show")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              "Prints string representation of an instance.")
#
#     def test_commands3(self):
#         """ Tests more commands for the console."""
#
#         # with patch('sys.stdout', new=StringIO()) as t:
#         #     msg = "Prints string representation of an instance."
#         #     HBNBCommand().onecmd("help show")
#         #     self.assertIsInstance(t.getvalue(), str)
#         #     self.assertEqual(t.getvalue().strip(),
#         #                      msg)
#
#         # with patch('sys.stdout', new=StringIO()) as t:
#         #     msg = "Updates an instance based on the class name and id."
#         #     HBNBCommand().onecmd("? update")
#         #     self.assertIsInstance(t.getvalue(), str)
#         #     self.assertEqual(t.getvalue().strip(),
#         #                      msg)
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             msg = "Updates an instance based on the class name and id."
#             HBNBCommand().onecmd("help update")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              msg)
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             msg = "Deletes an instance based on the class name and id."
#             HBNBCommand().onecmd("? destroy")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              msg)
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             msg = "Deletes an instance based on the class name and id."
#             HBNBCommand().onecmd("help destroy")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(), msg)
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("? quit")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              "Quit command to exit the program.")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("help quit")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              "Quit command to exit the program.")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("? help")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              "To get help on a command, type help <topic>.")
#
#         with patch('sys.stdout', new=StringIO()) as t:
#             HBNBCommand().onecmd("help help")
#             self.assertIsInstance(t.getvalue(), str)
#             self.assertEqual(t.getvalue().strip(),
#                              "To get help on a command, type help <topic>.")
