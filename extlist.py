
# Subclass of list which add2 2 useful methods
class ExtendedList(list):

	# Recoursive method able to return, of a given integers list, all the integers lesser
	# than or equal to a given number. If the list is already sorted, set the argument
	# 'already_sorted' to True, in order not to waste time sorting it again.
	def integers_lesser_or_equal(self, num, already_sorted = False):
		# The list will be sorted if it is not sorted yet.
		if not already_sorted:
			self.sort()
		# If the list is empty, an empty list will be returned.
		if len(self) == 0 or self[0] > num:
			return []
		# If the last item of the sorted list is lesser than or equal to the parameter, the entire list will be returned.
		if self[-1] <= num:
			return self
		# Otherwise the method will look for the item of the list situated in the middle.
		i = (len(self) - 1)  // 2
		# If such item is greater than the parameter, the method will return itself reiterated over the first half of the list
		# else, if it is lesser than or equal to the parameter and the following one is greater, the first hal of the list will be returned.
		# If, finally, both such item and the following one are lesser than or equal to the parameter
		# the return value will be the sum of the first half of the list and the return value of the method itself reiterated over the second half.
		if self[i] > num:
			return ExtendedList(self[:i+1]).integers_lesser_or_equal(num, True)
		else:
			if self[i+1] > num:
				return self[:i+1]
			else:
				return self[:i+1] + ExtendedList(self[i+1:]).integers_lesser_or_equal(num, True)

	# This method return a dictionary in which the keys are all the items in the list, repeated once,
	# whereas the values are integers which represent how many times those items appeared in the original list
	def count_items(self):
		counter = {}
		for item in self:
			if item in counter:
				counter[item] += 1
			else:
				counter[item] = 1
		return counter
