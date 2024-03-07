from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
import secrets
# Create your models here.
User    = settings.AUTH_USER_MODEL



    

class Payment(models.Model):
    #name = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    ticket_type = models.CharField(max_length=40,default="all" , blank=False, null=False)
    #contact       = PhoneNumberField(blank=False)
    amount = models.PositiveIntegerField()
    ref =models.CharField(max_length=200)
    email = models.CharField(max_length=200,blank=False,null=False)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(blank=True,default=1)
    class Meta:
        ordering=("-date_created",)
  
    def __str__(self) -> str:
        return f"Payment: {self.amount}"
    def save(self , *args,**kwargs) -> None:
        while not self.ref :
            ref = (secrets.token_urlsafe(4)).upper() #create a reference code to make transaction unique
            object_with_similar_ref  = Payment.objects.filter(ref=ref) 
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args,**kwargs)

    def amount_value(self) -> int:
        return self.amount*100*self.quantity # This is used to to call the actual price since paystack caculate in kobo
    def amount_norm(self) -> int:
        return self.amount*self.quantity
     
    
            
            
      
    
    
