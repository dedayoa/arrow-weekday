import arrow, math
from decimal import Decimal, ROUND_HALF_UP


def nearestPeriodicValue(point, value, period):
	
	relation = (value - point) / period
	
	equidistant = not(relation % 0.5) and relation % 1
	
	mod = period if equidistant else 0
	
	return mod + value - int(period * Decimal(str(relation)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

	
def containedPeriodicValues(start, end, value, period):

	# This is how I understood contained periodic values...
	# imagine a line, then params will be (starting point, total number of points, point of interest we would like to count in each cycle, number of cycles)
	
	if start == end:
		return 0
		
	if start > end:
		new_end = start
		start = end
		end = new_end
		
	end = end - 1
	
	nearest = nearestPeriodicValue(start, value, period)
	
	if (nearest - start) < 0:
		nearest += period
		
	if (nearest - start) > (end -start):
		return 0
	else:
		return 1 + int((end - nearest) / period)
	

class ArrowWeekday(object):
	
	def _determineSign(self, x):
		x = +x;
		return 1 if x > 0 else -1
		
	@classmethod
	def weekDays(self, startArrow, endArrow):
		start = None
		end = None
		reverse = endArrow < startArrow
		if reverse:
			start = endArrow
			end = startArrow
		else:
			start = startArrow
			end = endArrow
		
		startDay = start.weekday()
		totalDays = abs((end-start).days)
		
		# in momentjs, sunday is 0. in arrow, monday is 0
		containedSundays = containedPeriodicValues(startDay, totalDays + startDay, 6, 7)
		containedSaturdays = containedPeriodicValues(startDay, totalDays + startDay, 5, 7)
		
		coefficient = -1 if reverse else 1
		
		return coefficient * (totalDays - (containedSaturdays + containedSundays))
		
	@classmethod
	def weekendDays(self, startArrow, endArrow):
		totalDaysDiff = (endArrow-startArrow).days
		weekDays = self.weekDays(startArrow, endArrow);

		return totalDaysDiff - weekDays
	
	@classmethod
	def addWeekDays(self, arrowObj, amount):
		if (amount == 0 or not isinstance(amount, int)):
			return arrowObj
		
		sign = self._determineSign(self, amount);
		day = arrowObj.weekday();
		absIncrement = abs(amount);
		
		days = 0

		if (day == 0 and sign == -1):
			days = 1
		elif (day == 6 and sign == 1):
			days = 1
		paddedAbsIncrement = absIncrement;
		if (day != 0 and day != 6 and sign > 0):
			paddedAbsIncrement += day
		elif (day != 0 and day != 6 and sign < 0):
			paddedAbsIncrement += 6 - day
		
		weekendsInbetween = max(math.floor(paddedAbsIncrement / 5) - 1, 0) + (1 if paddedAbsIncrement > 5 and paddedAbsIncrement % 5 > 0 else 0)
		
		days += (absIncrement + (weekendsInbetween * 2))

		res = arrowObj.replace(days = sign * days)
		return res

	def subtractWeekDays(self, arrowObj, amount):
		return self.addWeekDays(arrowObj, -amount)
	
	def isWeekDay(self, arrowObj):
		return arrowObj.isoweekday() < 6
	
	def isWeekendDay(self, arrowObj):
		return arrowObj.isoweekday() > 5
