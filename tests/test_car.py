#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from models.car import Car
from models.day_rule import DayRule
from mock import patch, Mock
from ddt import ddt, data, unpack

@ddt
class TestCar(unittest.TestCase):
    def setUp(self):
        plate_number = 'PCO-5649'
        self.car = Car(plate_number)

    def test_last_digit(self):
        self.assertEqual(self.car.last_digit(), '9')

    @patch.object(DayRule, '_load_rules', return_value={})
    @patch.object(DayRule, 'is_broken_by_digit')
    @patch.object(DayRule, 'is_broken_by_time')
    @data((True, False, False), (False, False, False), (False, True, False), 
          (True, True, True))
    @unpack
    def test_is_breaking_the_rule(self, is_broken_by_time_return_value, 
                                  is_broken_by_digit_return_value , 
                                  expected_result, is_broken_by_time_mock, 
                                  is_broken_by_digit_mock, mocked_rules):
        """
        @data: contains the values for the patched methods
        """
        is_broken_by_time_mock.return_value = is_broken_by_time_return_value
        is_broken_by_digit_mock.return_value = is_broken_by_digit_return_value
        any_rule = DayRule('2017-01-01')
        any_time = '00:00:00'
        self.assertEqual(self.car.is_breaking_the_rule(any_rule, any_time), 
                         expected_result)
