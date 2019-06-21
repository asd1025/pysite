from django.db import models


# Create your models here.
# VO 같은 느낌
class Guestbook(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Guestbook({self.name} /{self.password} /{self.content}/ {self.regdate})'
