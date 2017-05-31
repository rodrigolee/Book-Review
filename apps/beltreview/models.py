from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
class UserManager(models.Manager):
    def register(self, postdata):
        errormsg = []
        emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        nameregex = re.compile(r'^[a-zA-Z]\w+$')
        if postdata['email'] < 0:
            errormsg.append('emails')
        if not emailregex.match(postdata['email']):
            errormsg.append('Incorrect email format')
        if not nameregex.match(postdata['name']):
            errormsg.append('Not a real name')
        if len(postdata['name']) < 2:
            errormsg.append('First name is too short')
        if len(postdata['password']) < 8:
            errormsg.append('Has to be more than 8 characters')
        if not postdata['password'] == postdata['pw_confirm']:
            errormsg.append('password does not match password confirm')
        if errormsg:
            return{
            'errors': errormsg
            }
        else:
            created_person = Users.objects.create(
            name=postdata['name'],
            email=postdata['email'],
            password=postdata['password'],
            confirm=postdata['pw_confirm'])
            bcrypt_password = postdata['password'].encode()
            hashed = bcrypt.hashpw(bcrypt_password, bcrypt.gensalt())
            return {
            'the_person' : created_person
            }
    def login(self, postData):
        errormsg = []
        emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailregex.match(postdata['email']):
            errormsg.append('email not validated')
        if not postdata['email'] == Users.objects.get(email=postdata['email']):
            errormsg.append('Incorrect email')
        if errormsg:
            return{
            'errors' : errormsg
            }
        else:
                errormsg.append('greatjob')
# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    pw_confirm = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
class Author(models.Model):
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id= models.ForeignKey(Users, default =1)
class Book(models.Model):
    title = models.CharField(max_length=45)
    review = models.TextField(max_length=255)
    rating= models.IntegerField(default=1, max_length=5)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
