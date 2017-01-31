#!/usr/bin/env python
# -*- coding: utf-8 -*-

class  Car(object):
    def __init__(self, plate_number):
        self.plate_number = plate_number
    
    def last_digit(self):
        """
        Returns the last digit of the car's plate number
        """
        return self.plate_number[-1]

    def is_breaking_the_rule(self, day_rule, time_str):
        """
        Returns True or False if the the car is breaking the rule
        for the given time.
        """
        return (day_rule.is_broken_by_digit(self.last_digit()) and
               day_rule.is_broken_by_time(time_str))