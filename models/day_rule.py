#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time_interval import TimeInterval
from datetime import datetime
import calendar
import ConfigParser
import os


class DayRule(object):

    date_format = "%Y-%m-%d"

    def __init__(self, date):
        week_day_number = datetime.strptime(date, self.date_format).date().weekday()
        week_day = calendar.day_name[week_day_number].lower()
        self.day = week_day
        self.rules = self._load_rules()
    
    def _load_rules(self):
        config_file = '%s/rules.ini' % os.getcwd()
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        return {s:dict(config.items(s)) for s in config.sections()}

    def digits(self):
        return self.rules['DigitRules'][self.day].split(',')
    
    def intervals(self):
        intervals = []
        intervals_names = self.rules['IntervalRules'][self.day].split(',')
        for interval_name in intervals_names:
            hours = self.rules['Intervals'][interval_name].split('-')
            intervals.append(TimeInterval(*hours))
        return intervals

    def is_broken_by_digit(self, digit):
        return digit in self.digits()

    def is_broken_by_time(self, time_str):
        return reduce(lambda x,y: x or y,
                      map(lambda x: x.is_containing(time_str), self.intervals()))

