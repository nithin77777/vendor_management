from django.db import models

from vendor_profile.models import VendorProfile
# Create your models here.


class PerformanceModel(models.Model):
    vendor = models.ForeignKey(VendorProfile,on_delete=models.CASCADE)
    date = models.DateTimeField(name="Performance Date")
    on_time_delivery_rate=models.FloatField(name="quality rating average")
    average_response_time=models.FloatField("Response Time Average")
    fulfillment_rate=models.FloatField(name="fulfilment rate")

    def __str__(self):
        return self.vendor
    


# class PerformanceMetrics:
#     def __init__(self):
#         super().__init__(self,PerformanceModel)
        
        
