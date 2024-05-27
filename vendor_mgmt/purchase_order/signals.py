from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import VendorProfile,PurchaseOrder
from django.utils import timezone
# importing Average from db.models
from django.db.models import Avg

@receiver(post_save,sender=PurchaseOrder)
def update_on_time_delivery_rate(sender,instance,**kwargs):
    if instance.status =='COMPLETED':
        completed_date = timezone.now()
        total_completed_po = PurchaseOrder.objects.filter(vendor=instance.vendor,status='COMPLETED')
        total_completed_po_count = total_completed_po.count()

        on_time_delivery = total_completed_po.filter(delivery_date__gte=completed_date).count()
        if total_completed_po_count>0:
            ontime_delivery_rate= on_time_delivery/total_completed_po_count
        else:
            ontime_delivery_rate=0

        vendor_profile_model = instance.vendor
        vendor_profile_model.on_time_delivery_rate = ontime_delivery_rate
        vendor_profile_model.save()

@receiver(post_save,sender=PurchaseOrder)
def quality_rating_avg(sender,instance,**kwargs):
    if instance.quality_rating is not None:
        quality_rating = PurchaseOrder.objects.filter(vendor=instance.vendor,status='COMPLETED',quality_rating__isnull=False)

        '''quality_rating__avg is the average key in the dictionary thats returned'''

        quality_rating_average = quality_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] 

        '''
        saving a model(instance) in a variable 
            - Making sure that quality_rating_average is going into the model VendorProfile
            - Saving the model
        '''
        vendor_profile_model = instance.vendor
        vendor_profile_model.quality_rating_avg = quality_rating_average
        vendor_profile_model.save()

        