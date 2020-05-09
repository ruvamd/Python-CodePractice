from django.db import models

category=('animals,items,wantWork,giveWork')

class city(models.Model):
    sellBuyChoice=['sell','buy']
    name=models.CharField(max_length=100)
    submitter=models.CharField(max_length=100)
    description=models.TextField()
    sbc=models.CharField(choices=sellBuyChoice,max_length=1,blank=True)
    submissionDate=models.DateTimeField()
    sellBuyAny=models.ManyToManyField('sellBuy',blank=True)
class sellBuy(models.Model):
    category=models.CharField(max_length=50,)
    name=models.CharField(max_length=50)
    
