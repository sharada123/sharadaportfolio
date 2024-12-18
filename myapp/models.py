from django.db import models

# Create your models here.
class Project(models.Model):
    cat=(('front end','Front End Project'),('back end' , 'Back End Project'),('full stack','Full Stack Web Project'))
    title=models.CharField(max_length=100, verbose_name="Project Name")
    desc=models.TextField(verbose_name="Description of project")
    img=models.ImageField(upload_to="image",verbose_name="image")
    srclink=models.CharField(max_length=200,verbose_name="Source code link")
    cat=models.CharField(max_length=200,choices=cat,verbose_name="Type of project")
    tech=models.TextField(verbose_name="Technologies used",default="Python")

class Contact(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.CharField(max_length=300)
    mob=models.BigIntegerField()
    msg=models.TextField()