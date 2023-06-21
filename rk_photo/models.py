from django.db import models

# Create your models here.

class Wedding(models.Model):
    title  = models.TextField()
    fil = models.TextField()
    heading  = models.TextField()
    wedding  = models.ImageField(upload_to='images/weddingp/')

    def __str__(self):
        return self.title


class Boy(models.Model):
    title  = models.TextField()
    fil = models.TextField()
    heading  = models.TextField()
    boy  = models.ImageField(upload_to='images/boyp/')

    def __str__(self):
        return self.title

class Girls(models.Model):
    title  = models.TextField()
    fil = models.TextField()
    heading  = models.TextField()
    girls  = models.ImageField(upload_to='images/girlsp/')

    def __str__(self):
        return self.title

class Kids(models.Model):
    title  = models.TextField()
    fil = models.TextField()
    heading  = models.TextField()
    baby  = models.ImageField(upload_to='images/kidsp/')

    def __str__(self):
        return self.title

class Album(models.Model):
    title  = models.TextField()
    fil = models.TextField()
    heading  = models.TextField()
    album  = models.ImageField(upload_to='images/albump/')

    def __str__(self):
        return self.title

# ======================================team=======================


        # =================================contact==================================

class Team(models.Model):
    Name  = models.TextField()
    Profession  = models.TextField()
    Instagram_id  = models.TextField()
    Photo  = models.ImageField(upload_to='images/Team/')

    def __str__(self):
        return self.Name

class Contact(models.Model):
        Fullname = models.CharField(max_length=50)    
        Contact = models.CharField(max_length=50)
        Email = models.CharField(max_length=50)
        City = models.CharField(max_length=50)
        Budget= models.CharField(max_length=50)
        Service = models.CharField(max_length=50)
        Day = models.CharField(max_length=50)
        Date = models.CharField(max_length=50)


        # ==========================admin=================

class Admin_rk(models.Model):
    Admin = models.CharField(max_length=50) 

    def __str__(self):
        return self.Admin 

class Admin_ak(models.Model):
    Admin = models.CharField(max_length=50) 

    def __str__(self):
        return self.Admin

# ===============================bill==================================

import datetime
# Create your models here.
class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    date_created = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.customer)
    
    def get_status(self):
        return self.status

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.customer)
   
