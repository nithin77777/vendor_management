from django.shortcuts import render,redirect
from .models import PurchaseOrder
from vendor_profile.models import VendorProfile

# Create your views here.




def create_order(request):
    
    if request.method =='POST':
        po = request.POST.get('po_number')
        vendor = request.POST.get('vendor')
        order_date=request.POST.get('order_date')
        delivery_date=request.POST.get('delivery_date')
        items=request.POST.get('items')
        quantity=request.POST.get('quantity')
        status=request.POST.get('status')
        quality_rating=request.POST.get('quality_rating')
        issue_date = request.POST.get('issue_date')
        acknowledgment_date=request.POST.get('acknowledgment_date')

        vendor = VendorProfile.objects.get(name=vendor)

        data = PurchaseOrder(
            po_number=po,
            vendor=vendor,
            order_date=order_date,
            delivery_date=delivery_date,
            items=items,
            quantity=quantity,
            quality_rating=quality_rating,
            status=status,
            issue_date=issue_date,
            acknowledgment_date=acknowledgment_date
        )
        
        data.save()
        return redirect("orders/")
    return render(request,'purchase_orders.html')

def all_orders(request):
    orders = PurchaseOrder.objects.all()
    return render(request,"all_orders.html",{'orders':orders})
