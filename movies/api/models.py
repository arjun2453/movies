from django.db import models

# Create your models here.

Movies=[
    {"id":1,"name":"Sphadikam","year":1996,"direction":"Bhadran","gener":"action/drama"},
    {"id":2,"name":"Dhrishyam","year":2013,"direction":"Jithu Jospeph","gener":"crime/thriller"},
    {"id":3,"name":"Romancham","year":2023,"direction":"Jithu Madhavan","gener":"comedy/horror"},
    {"id":4,"name":"Titanic","year":1997,"direction":"James Cameran","gener":"Romance/Drama"},
    {"id":5,"name":"CID moosa","year":2003,"direction":"Johny Antony","gener":"comedy/action"},
]

class MoviesList(models.Model):
    name=models.CharField(max_length=200)
    year=models.IntegerField()
    direction=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    
    