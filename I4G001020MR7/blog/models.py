from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=now, editable=True)
    published_date = models.DateTimeField(default=now, editable=True)

