from django.db import models

# Create your models here.
class Person(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fullname 

class Experience(models.Model):
    job_title = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    end_date= models.DateField(null=True)
    information = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.job_title

class About(models.Model):
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class Education(models.Model):
    field = models.CharField(max_length=100,null=True)
    start_date = models.DateField(null=True)
    end_date= models.DateField(null=True)
    information = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.field

class Interest(models.Model):
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return self.description

   
