from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title= models.CharField(max_length=100)
    content=models.CharField(max_length=2000)
    hit=models.IntegerField(default=0)
    regdate=models.DateTimeField(auto_now=True)
    groupno=models.IntegerField(default=0)
    orderno=models.IntegerField(default=0)
    depth=models.IntegerField(default=0)
    delete=models.BooleanField(default=False)
    user=models.ForeignKey(User,to_field='id',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}/{self.content}/{self.hit} :hit/{self.groupno}:groupno /{self.orderno} :orderno/ {self.depth}/ {self.regdate}/{self.user}'
