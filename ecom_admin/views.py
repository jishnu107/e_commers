from django.shortcuts import render,redirect
from common.models import Customer,Seller
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def adminhome_page(request):
    return render(request,'ecomadmin/adminhome.html')
def custview_page(request):

    customers = Customer.objects.all()
    
    return render(request,'ecomadmin/custview.html',{'customer_list':customers})

def sellview_page(request):
    sellers = Seller.objects.filter(approved=True)

    return render(request,'ecomadmin/sellerview.html',{'seller_list':sellers})
def sellapprove_page(request):
    sellers = Seller.objects.filter(approved = False)

    return render(request,'ecomadmin/sellapprove.html',{'seller_app':sellers})
def pass_page(request):
    return render(request,'ecomadmin/pass.html')

def approve(request,sid):
    seller=Seller.objects.get(id=sid)
    message = 'you are now approved to login'
    send_mail(
        'Login approved',
        message,
        settings.EMAIL_HOST_USER,
        [seller.seller_email,], 
    )
    seller.approved=True
    seller.save()
    return redirect('ecome_admin:sellerview')

def delete_seller(request,sid):
    seller_list = Seller.objects.get(id = sid)
    seller_list.delete()
    return redirect('ecome_admin:sellerview')
    


