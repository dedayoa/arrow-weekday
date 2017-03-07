from .arrow_weekday import ArrowWeekday

_awd = ArrowWeekday()

def weekDays(*args, **kwargs):
    return _awd.weekDays(*args, **kwargs)
    

def weekendDays(*args, **kwargs):
    return _awd.weekendDays(*args, **kwargs)
    

def addWeekDays(*args, **kwargs):
    return _awd.addWeekDays(*args, **kwargs)
    

def subtractWeekDays(*args, **kwargs):
    return _awd.subtractWeekDays(*args, **kwargs)
    

def isWeekDay(*args, **kwargs):
    return _awd.isWeekDay(*args, **kwargs)
    

def isWeekendDay(*args, **kwargs):
    return _awd.isWeekendDay(*args, **kwargs)
    
