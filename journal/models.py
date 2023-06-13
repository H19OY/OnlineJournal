import datetime
from django.db import models
from django.utils import timezone


class JournalEntry(models.Model):
    date = models.DateField(default=datetime.date.today)

    time = models.TimeField(default=timezone.now().astimezone(timezone.pytz.timezone('Asia/Dhaka'))
)
    


    content = models.TextField()
