from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
# Create your models here.
class TODO(models.Model):
   user = models.ForeignKey(User, null=True,on_delete=models.SET_NULL)
   text = models.TextField()
   date_created = models.DateTimeField(default=datetime.datetime.now)
   completed = models.BooleanField(default=False)
   deadline =models.DateTimeField()

   @property
   def check_rem(self):
      time_rem_checker = None
      time_left = self.deadline - datetime.datetime.now()
      if (time_left.days >= 1):
         if (time_left.days == 1):
            time_rem_checker = f'{time_left.days} day'
         else:
            time_rem_checker = f'{time_left.days} days'
      elif(time_left.total_seconds() >= 3600 ):
         time_rem_checker = f'{int(int(time_left.seconds)/3600)} hours'
      elif(time_left.total_seconds() <= 0 ):
         time_rem_checker = 'dealine reached'.replace('left', '')
      else:
         time_rem_checker = f'{int((time_left.seconds)/60)} minutes'
      
      return time_rem_checker



         

   
   

