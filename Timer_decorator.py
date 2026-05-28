#simple decorator to time that how long any function takes to run
import time
def timer(func):
	def wrapper():
		start = time.time()
		func()
		stop = time.time()
		print(f"{func.__name__} took {stop-start} seconds")
	return wrapper
		
@timer
def slow_function():
	print("Sleeping")
	time.sleep(1)
@timer
def fast_function():
	pass

fast_function()
slow_function()
