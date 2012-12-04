from django.db import models
from content.models import Content
from users.models import UserProfile
import datetime
from django.utils import timezone

# Create your models here.

class Cdr(models.Model):
	from_phone_no = models.CharField(max_length=12)
	to_phone_no = models.CharField(max_length=12)
	status = models.BooleanField(default=0) #0 not connected and 1 connected
	start_of_call = models.DateTimeField() 
	duration_of_call = models.IntegerField()

	def __unicode__(self):
		return self.from_phone_no

