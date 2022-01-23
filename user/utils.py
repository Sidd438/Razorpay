from .models import Payment


def handle_payment(request):
    current_user = request.user
    current_user.profile.Payments += 1
    current_user.profile.total_amount += int(request.POST.get('amount'))
    current_user.profile.save()
    if(request.POST.get('status')=="true"):
        status = True
    else:
        status = False
    print(status)
    payment = Payment.objects.create( user=current_user, amount=request.POST.get('amount'),order_id=request.POST.get('order_id'),signature=request.POST.get('signature'),    payment_id=request.POST.get('payment_id'), status=status)
