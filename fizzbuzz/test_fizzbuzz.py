#!/usr/bin/env python

from unittest import TestCase
from fizzbuzz import FizzBuzz


class FizzBuzzTest(TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def tearDown(self):
        self.fizzbuzz = None

    def test_returns_number_for_input_not_divisible_by_3_or_5(self):
        for i in range(1, 100):
            if i % 3 == 0 or i % 5 == 0:
                continue
            self.assertEqual(str(i), self.fizzbuzz.convert(i))

    def test_returns_fizzbuzz_for_input_divisible_by_3_and_5(self):
        for i in range(1, 100):
            if i % 3 != 0 or i % 5 != 0:
                continue
            self.assertEqual('FizzBuzz', self.fizzbuzz.convert(i))

    def test_returns_fizz_for_input_divisible_by_3(self):
        for i in range(1, 100):
            if i % 3 != 0 or i % 5 == 0:
                continue
            self.assertEqual('Fizz', self.fizzbuzz.convert(i))

    def test_returns_buzz_for_input_divisible_by_5(self):
        for i in range(1, 100):
            if i % 5 != 0 or i % 3 == 0:
                continue
            self.assertEqual('Buzz', self.fizzbuzz.convert(i))
