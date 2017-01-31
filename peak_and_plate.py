#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.car import Car
from models.day_rule import DayRule
import sys
params = sys.argv

plate_numer = params[1]
date_str = params[2]
time_str = params[3]

car =  Car(plate_numer)
day_rule = DayRule(date_str)
allowed_to_transit = 'No' if car.is_breaking_the_rule(day_rule, time_str) else 'Yes'
print allowed_to_transit

