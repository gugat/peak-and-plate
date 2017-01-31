#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from exceptions import InvalidInitTime

class TimeInterval(object):
    
    time_format = '%H:%M:%S'

    def __init__(self, init_time_str, end_time_str):
        self.init_time = datetime.strptime(init_time_str, self.time_format)
        self.end_time = datetime.strptime(end_time_str, self.time_format)
        if self.end_time <= self.init_time:
            raise InvalidInitTime('The init time string should be less than end time')

    def is_containing(self, time_str):
        """
        Returns True or False if the interval contains the given time
        """
        inner_time = datetime.strptime(time_str, self.time_format)
        return (self.init_time <= inner_time and 
                self.end_time >= inner_time)

    def __str__(self):
        return 'Init time %s - End time %s' % (self.init_time, self.end_time)