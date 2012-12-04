from random import randrange,choice,randint
from datetime import timedelta, datetime
from cdr.models import Cdr
import random


stst = [0,1,2]
def random_with_N_digits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return (start + timedelta(seconds=random_second))


d1 = datetime.strptime('12/1/2012 05:01 AM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('12/30/2012 11:59 PM', '%m/%d/%Y %I:%M %p')

for i in range(1000000):
	start_of_call = random_date(d1, d2)
	from_phone_no = random_with_N_digits(12)
	to_phone_no = random_with_N_digits(12)
	call_connect = random.choice(stst)
	duration = randint(1,100)
	cdr = Cdr(from_phone_no = from_phone_no,to_phone_no = to_phone_no,status = call_connect,start_of_call = start_of_call,duration_of_call = duration)
	cdr.save()
