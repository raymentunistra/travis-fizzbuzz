#!/usr/bin/env python

from unittest import TestCase
from mock import patch
from solver import ProblemSolver
from fizzbuzz import FizzBuzz


mock_convert = FizzBuzz.convert


def mock_display(s):
    print(s)  # pragma: no cover


class ProblemSolverTest(TestCase):

    def setUp(self):
        with patch('solver.Int2String') as mock:
            mock.convert = mock_convert
            converter = mock
        with patch('solver.Displayer') as mock:
            mock.display = mock_display
            displayer = mock
        self.solver = ProblemSolver(converter, displayer)

    def tearDown(self):
        self.solver = None

    def test_foo(self):
        self.assertEqual(True, self.solver.solve())
