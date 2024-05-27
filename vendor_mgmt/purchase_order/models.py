from django.db import models

from vendor_profile.models import VendorProfile

# Create your models here.
STATUS_CHOICES = [('pending','PENDING'),('completed','COMPLETED'),('canceled','CANCELED')]

class PurchaseOrder(models.Model): 
    
    po_number=models.CharField(verbose_name='Purchase Order Number',max_length=20,unique=True) 
    vendor=models.ForeignKey(VendorProfile,on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(choices=STATUS_CHOICES,max_length=20)
    quality_rating=models.FloatField(null=True)
    issue_date=models.DateTimeField()
    acknowledgment_date=models.DateTimeField(null=True)
