from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib import messages
from .
from .models import   Payment
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User 
from django.urls import reverse
# Create your views here.
import requests


PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY # Pass your secreet key in settings file
base_url = "https://api.paystack.co"
header = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "content-type": "application/json",
    }


# in your paystack window code add your redirect to this view

def verify_payment(request):
    global status  # variable to hold transaction status if need i any other view
    transacrions = Payment.objects.all()
    try:
            #owner = Payment.objects.get(name=request.user)
            for obj in transactions :
                if obj.verified == False:
                    ref=obj.ref
                    path = f"/transaction/verify/{obj.ref}"
                    url = base_url + path
                    response = requests.get(url,headers=header)
                    if response.status_code == 200:
                        obj.verified = True
                        obj.save()
                        status = "verified"
                        return redirect("home")
                    else:
                        status = "failed"
                else:
                    pass
    except Payment.DoesNotExist:
        pass
    except Payment.MultipleObjectsReturned:
         return redirect("verify")
    except requests.ConnectionError:
        messages.success(request,"network error")
        return redirect('error')
    
    return render(request,"home.html",{})
