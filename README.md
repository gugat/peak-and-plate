# Peak and Plate

Validates if a car is allowed to transit at peak hours according to the last digit in its plate number, the date and time.

## Requirements

* Python [2.7.10](https://www.python.org/download/releases/2.7/)
* [pip](https://pypi.python.org/pypi/pip)

## Setup

Install dependencies

`pip install -r requirements.txt`

## How to use

Execute the script `peak_and_plate.py` passing three arguments, the first argument is the plate number, the second argument is the date and the third argument is the time. For example:

```
python peak_and_plate.py GSC-6839 2017-01-27 10:00:30
> No

python peak_and_plate.py GSC-6834 2017-01-31 08:00:30
> Yes

```


The script returns 'Yes' or 'No' if the car is allowed or not to transit for the given date and hour.

The rules are defined in the file `rules.ini`

### rules.ini

The `[DigitRules]` section defines the digits per weekdays for which the Peak and Plate restriction is applied. Digits should be separated by comma without spaces. Week days without restrictions must be left in blank.

```
[DigitRules]
monday = 1,2
tuesday = 3,4
wednesday = 5,6
thursday = 7,8
friday = 9,10
saturday =
sunday =
```

The `[Intervals]` section defines the time intervals, each interval has a name, e.g. `morning` , the init time and end time separated by a dash.

```
[Intervals]
morning = 07:00:00-09:00:00
afternoon = 16:00:00-19:30:00
```

The `[IntervalRules]` sections associates the intervals with the weekday. Days without interval restrictions should be left empty.


```
[IntervalRules]
monday = morning,afternoon
tuesday = morning,afternoon
wednesday = morning,afternoon
thursday = morning,afternoon
friday = morning,afternoon
saturday =
sunday =
```


## Tests

`python -m unittest discover`