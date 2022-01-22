from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import context
from django.contrib.auth import logout
import razorpay
from allauth.socialaccount.models import SocialAccount
from django.views.generic import TemplateView

from user.utils import handle_payment
# Create your views here.

class Main(TemplateView):
    template_name = "main.html"

def logoutA(request):
    logout(request)
    return redirect('/accounts/google/login')

def home(request):
    actual_amount = 100
    current_user = request.user
    if(request.POST.get("number")):
        current_user.profile.phone_number = request.POST.get("number")
        current_user.profile.save()
    if(current_user.is_anonymous):
        return redirect('/accounts/google/login')
    email = SocialAccount.objects.get(user=request.user).extra_data['email']
    if "@pilani.bits-pilani.ac.in" not in email:
        current_user.delete()
        return render(request, 'error.html')
    if(request.POST.get('order_id')):
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
        "email": email,
        "number":current_user.profile.phone_number
    }
    return render(request, 'checkout.html', context)

def profile(request):
    current_user = request.user
    payments = current_user.payment_set.filter().order_by("-id")
    data = SocialAccount.objects.get(user=current_user).extra_data
    data['user'] = current_user
    data['payments'] = payments
    return render(request, "profile.html", data)