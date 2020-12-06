from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Detail(models.Model):
    name = models.CharField(max_length=100)
    Branch = models.CharField(max_length=5)
    Semester = models.IntegerField()
    Interests = models.TextField()
    cgpa = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_detail', kwargs={'pk': self.pk})

