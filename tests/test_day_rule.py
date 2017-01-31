#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from models.day_rule import DayRule
from models.time_interval import TimeInterval
from mock import patch
from ddt import ddt, unpack, data

@ddt
class TestDayRule(unittest.TestCase):

    def setUp(self):
        with patch.object(DayRule, '_load_rules', return_value={}):
            self.rule = DayRule('2017-01-01')


    @data(('5', True), ('7', False))
    @unpack
    def test_is_broken_by_digit(self, digit_to_test, expected_result):
        with patch.object(DayRule, 'digits') as mock:
            mock.return_value = ['5','6']
            self.assertEqual(self.rule.is_broken_by_digit(digit_to_test), 
                             expected_result)


    @patch.object(DayRule, 'intervals')
    @data(['11:00:00', False], ['13:00:00', True], ['14:00:00', True], 
          ['15:00:00', True], ['15:30:00', False], ['16:00:00', True],
          ['16:30:00', True])
    @unpack
    def test_is_broken_by_time(self, time_to_test, expected_result, 
                               intervals_mock):
        intervals_mock.return_value = [TimeInterval('13:00:00', '15:00:00'),
                                       TimeInterval('16:00:00', '17:00:00')]
        self.assertEqual(self.rule.is_broken_by_time(time_to_test),
                               expected_result)


    @patch.object(DayRule, '_load_rules')
    def test_digits(self, rules_mock):
        rules_mock.return_value = {'DigitRules': {'monday': '3,4'}}
        rule = DayRule('2017-01-02')
        self.assertEqual(rule.digits(), ['3','4'])


    @patch.object(DayRule, '_load_rules')
    def test_intervales(self, rules_mock):
        rules_mock.return_value = {'IntervalRules': 
                                    {'monday': 'morning,afternoon'},
                                   'Intervals': 
                                    {'morning': '07:00:00-09:00:00',
                                     'afternoon': '16:00:00-19:30:00'}}
        rule = DayRule('2017-01-02')
        intervals = rule.intervals()
        for interval in intervals:
            self.assertEqual(type(interval), TimeInterval)
        self.assertEqual(str(intervals[0].init_time.time()), '07:00:00')
        self.assertEqual(str(intervals[0].end_time.time()), '09:00:00')
        self.assertEqual(str(intervals[1].init_time.time()), '16:00:00')
        self.assertEqual(str(intervals[1].end_time.time()), '19:30:00')


