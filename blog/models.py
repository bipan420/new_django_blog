from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#reverse will return the string of the url, unlike redirect which sends you to specific url
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# This method is for grabbing the url after the Post button is pressed
    def get_absolute_url(self):
        return reverse('post-detail', kwargs ={'pk':self.pk})
