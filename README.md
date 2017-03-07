# arrow-weekday
Utilities for work days in Arrow. Inspired by moment-business.

Utilities for working with week days and weekend days in Arrow. It assumes a Western
workweek, in which weekends are Saturday and Sunday.

*This module was inspired by arrowObj-business; https://github.com/jmeas/moment-business/*

### Motivation

[Arrow](http://arrow.readthedocs.io/en/latest/) is a Python library that offers a sensible, human-friendly approach to creating, manipulating, formatting and converting dates, times, and timestamps

This library supplies you with tools to work with/manipulate weekdays and weekends.

### Getting Started

Install this library through npm.

```py
pip install git+https://github.com/dedayoa/arrow-weekday
```

Next, import it into your project.

```py
from arrow_weekday import ArrowWeekday

ArrowWeekday.isWeekDay(arrowObj);
```

### Guides


#### Intervals

This library uses inclusive start, exclusive end intervals. What this means is
that the start day is included in the result, but the end day is not.

This is consistent with how Arrow's intervals work.

For example, the total number of days between March 1st, 2020 and March 2nd,
2020 will be computed as 1.

### API

##### `weekDays( startArrow, endArrow )`

Calculate the number of week days between `startArrow` and `endArrow`. Week days are Monday through Friday.

If `endArrow` comes before `startArrow`, then this function will return a negative value.

##### `weekendDays( startArrow, endArrow )`

Calculate the number of weekend days between the arrowObj and `otherArrow`. Weekend days are Saturday and Sunday.

If `endArrow` comes before `startArrow`, then this function will return a negative value.

##### `addWeekDays( arrowObj, amount )`

Add week days to a arrowObj, modifying the original arrowObj. Returns the arrowObj.

##### `subtractWeekDays( arrowObj, amount )`

Subtract week days from the arrowObj, modifying the original arrowObj. Returns the arrowObj.

##### `isWeekDay( arrowObj )`

Whether or not the Arrow is a week day (Monday - Friday).

##### `isWeekendDay( arrowObj )`

Whether or not the Arrow occurs on Saturday or Sunday.
