from extlist import ExtendedList

# This class has two functions: producing a sequence of prime numbers
# through a generator and factorizig integers.
class PrimeNumbers:

	# FACTORIZE INTEGERS

	# Method that factorizes an integer, returning a dictionary where keys are
	# the factors and values are their exponents. If the input is 0 or 1,
	# an empty dictionary is returned, whereas if the integer is negative, its
	# absolute value is factorized.
	# A loop looks for prime factors through a prime numbers generator obtained
	# using the 'prime_numbers' method of this class. Each time a prime factor
	# is found the number to factorize is divided by it. When such number
	# becomes one, the loop is broken and the list of factors, before being
	# returned, is converted to a dictionary using a method of ExtendedList from
	# the module 'extlist' .
	def factorize (self, num):
		num = abs(num)
		if num == 0 or num == 1:
			return {}
		prime_factors = []
		for p_n in self.prime_numbers():
			while num % p_n == 0:
				prime_factors.append(p_n)
				num /= p_n
			if num == 1:
				break
		return ExtendedList(self.factorize_ls(num)).count_items()

	# FIND PRIME NUMBERS

	# Method that returns a generator of prime numbers.
	# An infinite loop checks one number at a time verifing if it has prime
	# divisors or not. If it hasn't, it is prime, so it is stored in a list and yielded:
	# such list is used to determine whether the following numbers are prime or not.
	def prime_numbers(self):
		stored_prime_nums = []
		i = 2
		while True:
			if not self.__check_divisibility(i, stored_prime_nums):
				stored_prime_nums.append(i)
				yield i
			i += 1

	# Method that iterates through a list of integers to check if they are
	# divisors of the first paramether. If no one of them is,
	# False is returned
	@staticmethod
	def __check_divisibility(num, divs):
		for div in divs:
			if num % div == 0:
				return True
		return False
