from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='follower')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='followin')

    def __str__(self):
        return f'{self.from_user}following{self.to_user}'