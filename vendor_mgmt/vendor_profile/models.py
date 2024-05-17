from django.db import models

# Create your models here.

class VendorProfile(models.Model):

    name= models.CharField(max_length=50,verbose_name='Vendor Name')
    contact_details=models.TextField(verbose_name='Contact Information of Vendor')
    address=models.TextField(verbose_name="Vendor address")
    vendor_code=models.CharField(primary_key=True,max_length=10)
    on_time_delivery_rate=models.FloatField(blank=True,default=0)
    quality_rating_avg=models.FloatField(default=0)
    average_response_time=models.FloatField(default=0)
    fulfillment_rate=models.FloatField(default=0)
