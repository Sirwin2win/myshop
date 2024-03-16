from django.shortcuts import render, redirect
import json
from django.urls import reverse
import requests
from django.conf import settings
from django.shortcuts import get_object_or_404
from orders.models import Order

# create the Paystack instance
api_key = settings.PAYSTACK_SECRET_KEY
url = settings.PAYSTACK_INITIALIZE_PAYMENT_URL

###previous code###

def payment_process(request):
    # retrive the payment_id we'd set in the djago session ealier
    order_id = request.session.get('order_id', None)
    # using the payment_id, get the database object
    order = get_object_or_404(Order, id=order_id)
    # retrive payment amount 
    amount = order.get_total_cost() * 100

    if request.method == 'POST':
        success_url = request.build_absolute_uri(
            reverse('payment:payment_success'))
        cancel_url = request.build_absolute_uri(
            reverse('payment:payment_canceled'))

        # metadata to pass additional data that 
        # the endpoint doesn't accept naturally.
        metadata= json.dumps({"order_id":order_id,  
                              "cancel_action":cancel_url,   
                            })

        # Paystack checkout session data
        session_data = {
            'email': order.email,
            'amount': int(amount),
            'callback_url': success_url,
            'metadata': metadata
            }

        headers = {"authorization": f"Bearer {api_key}"}
        # API request to paystack server
        r = requests.post(url, headers=headers, data=session_data)
        response = r.json()
        if response["status"] == True :
            # redirect to Paystack payment form
            try:
                redirect_url = response["data"]["authorization_url"]
                return redirect(redirect_url, code=303)
            except:
                pass
        else:
            return render(request, 'payment/process.html')
    else:
        return render(request, 'payment/process.html')
    



###previous code###

def payment_success(request):
    return render(request, 'payment/success.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')


