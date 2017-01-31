#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from models.time_interval import TimeInterval
from models.exceptions import InvalidInitTime
from ddt import ddt, unpack, data

@ddt
class TestTimeInterval(unittest.TestCase):

    def setUp(self):
        pass
    

    @data(('13:30:00', False), ('14:00:00', True), ('14:30:00', True), 
          ('15:00:00', True), ('15:30:00', False))
    @unpack
    def test_is_containing(self, time_value, expected_result):
        time_interval = TimeInterval('14:00:00', '15:00:00')
        self.assertEqual(time_interval.is_containing(time_value), 
                         expected_result)


    def test_doesnt_allow_init_time_greater_than_end_time(self):
        with self.assertRaises(InvalidInitTime) as context:
            time_interval = TimeInterval('14:00:00', '13:00:00')