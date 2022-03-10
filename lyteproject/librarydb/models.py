from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField('year published')
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    def __str__(self):
        return f"{self.title} ({self.pub_date.year})"

class CustomerExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    #used in borrow book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


def get_expiry():
    return datetime.today() + timedelta(days=15)
class BorrowedBook(models.Model):
    #moved this in forms.py
    #book = models.ForeignKey(Book)
    enrollment=models.CharField(max_length=30)
    borrowdate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.enrollment

