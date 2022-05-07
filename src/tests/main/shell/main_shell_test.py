from unittest import TestCase
from shell.main_shell import MainShell


class MainShellTest(TestCase):
    def setUp(self):
        self.target = MainShell()

    def test_execute(self):
        self.target.execute()
        self.assertEqual(1, 1)
