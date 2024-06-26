from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .models import VendorProfile

# Create your views here.
'''
 name= models.CharField(max_length=50,verbose_name='Vendor Name')
    contact_details=models.TextField(verbose_name='Contact Information of Vendor')
    address=models.TextField(verbose_name="Vendor address")
    vendor_code=models.CharField(primary_key=True,max_length=10)
    on_time_delivery_rate=models.FloatField(blank=True,default=0)
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()
'''
def create_vendor(request):

    if request.method=='POST':
        print(request.POST)
        name = request.POST.get("name")
        contact_details = request.POST.get('contact_details')
        address=request.POST.get('address')
        vendor_code = request.POST.get('vendor_code')
        data = VendorProfile(
            name=name,
            contact_details=contact_details,
            address=address,
            vendor_code=vendor_code
        )
        data.save()
        return redirect('vendors/')
    return render(request,'create_vendor.html')


def all_data(request):
    data = VendorProfile.objects.all()
    return render(request,'all_vendors.html',context={'data':data})


def specific_vendor(request,v_id):
    vendor_code = str(v_id).upper()

    data = VendorProfile.objects.filter(vendor_code=vendor_code)
    
    return render(request,'vendor_specific.html',context={'data':data})



def put_vendor(request,vendor_id):

    v_code = str(vendor_id).upper()
    
    data  = VendorProfile.objects.filter(vendor_code=v_code).first()
    # print(data.vendor_code)
    
    if request.method == 'POST':
        name = request.POST.get("name")
        contact_details = request.POST.get("contact_details")
        address=request.POST.get('address')
        vendor_code = data.vendor_code#request.POST.get('vendor_code')
        data = VendorProfile(name=name, contact_details=contact_details, address=address)
        data.save()
        messages.success(request,"Updated {vendor_id} Successfully")
        return redirect(reverse("put_vendor",kwargs={"vendor_id":vendor_id}))
    messages.success(request,f"Updated {vendor_id} Successfully")
    return render(request,"update_vendor.html",context={"updated_data":data})
