from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=50,default="xyz")
    email=models.EmailField(max_length=254)
    role=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=800,blank=True)


class UserToken(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=500, unique=True)
    is_active = models.BooleanField(default=True)



class Role(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

class Menu(models.Model):
    menuItem=models.CharField(max_length=50)
    menuPath=models.CharField(max_length=50)
    parentID=models.IntegerField()
    menuIcon=models.CharField(max_length=500,default="xy")
    sortOrder=models.IntegerField()


class Permission(models.Model):
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    menu=models.ManyToManyField(Menu)

class Investor(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    mobile=models.BigIntegerField()



class Company(models.Model):
    company_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    mobile=models.BigIntegerField()
    gstin=models.CharField(max_length=15)
    balance=models.IntegerField()
    country=models.CharField(max_length=520)
    address=models.CharField(max_length=500)


class InflowTransaction(models.Model):
    investor=models.CharField(max_length=500)
    to_company=models.CharField(max_length=500)
    date=models.DateField(null=False)
    amount=models.IntegerField()
    description=models.CharField(max_length=500)



class OutflowTransaction(models.Model):
    company=models.CharField(max_length=500)
    to_company=models.CharField(max_length=500, null=True)
    date=models.DateField(null=False)
    amount=models.IntegerField()
    description=models.CharField(max_length=500)



class Country(models.Model):
    country_name=models.CharField(max_length=50)




class ApprovedInflowTransaction(models.Model):
    inflowtransaction = models.ForeignKey(InflowTransaction, on_delete=models.CASCADE)
    investor=models.CharField(max_length=500)
    to_company=models.CharField(max_length=500)
    date=models.DateField(null=False)
    amount=models.IntegerField()
    description=models.CharField(max_length=500)
    


class RejectedInflowTransaction(models.Model):
    inflowtransaction = models.ForeignKey(InflowTransaction, on_delete=models.CASCADE)
    investor=models.CharField(max_length=500)
    to_company=models.CharField(max_length=500)
    date=models.DateField(null=False)
    amount=models.IntegerField()
    description=models.CharField(max_length=500)



class ApprovedOutflowTransaction(models.Model):
    outflowtransaction = models.ForeignKey(OutflowTransaction, on_delete=models.CASCADE)
    company=models.CharField(max_length=500)
    to_company=models.CharField(max_length=500)
    date=models.DateField(null=False)
    amount=models.IntegerField()
    description=models.CharField(max_length=500)
    Return= models.BooleanField(default=False)
    Return_amount=models.IntegerField(null=True)
    Return_date=models.DateField(null=True)




class RejectedOutflowTransaction(models.Model):
    outflowtransaction = models.ForeignKey(OutflowTransaction, on_delete=models.CASCADE)
    company=models.CharField(max_length=500)
    to_company=models.CharField(max_length=500)
    date=models.DateField(null=False)
    amount=models.IntegerField()
    description=models.CharField(max_length=500)