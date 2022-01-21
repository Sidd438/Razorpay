from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import context
import razorpay
from allauth.socialaccount.models import SocialAccount

from user.utils import handle_payment
# Create your views here.
def home(request):
    actual_amount = 100
    current_user = request.user
    if(current_user.is_anonymous):
        return redirect('/accounts/google/login')
    email = SocialAccount.objects.get(user=request.user).extra_data['email']
    if "@pilani.bits-pilani.ac.in" not in email:
        current_user.delete()
        return render(request, 'error.html')
    if(request.POST.get('amount')):
        handle_payment(request)
    client = razorpay.Client(auth=("rzp_test_WuHOZ859u5douX", "nQhtnn82KImexidSzUJrXWVC"))
    if(request.POST.get("amount")):
        actual_amount = request.POST.get("amount")
    amount = int(actual_amount)*100
    DATA = {
        "amount": (amount),
        "currency": "INR",
        "payment_capture":1,
        "amount":amount
    }
    order=client.order.create(data=DATA)
    order_id = order['id']

    context = {
        "amount": actual_amount,
        "currency": "INR",
        "api_key": "rzp_test_WuHOZ859u5douX",
        "id":order_id,
        "user":current_user,
        "email": email
    }
    return render(request, 'checkout.html', context)
