from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()



category_choices= (
    ("Data Structure and Algorithms","Data Structure and Algorithms"),
    ("Programming Languages","Programming Languages"),
    ("Web Development","Web Development"),
)
# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='books/pdfs/')
    category=models.CharField(max_length=30,choices=category_choices,default="")
    fav_of_users=models.ManyToManyField(User,blank=True)


    def __str__(self):
        return self.title 


