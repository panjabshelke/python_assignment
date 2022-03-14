from django.db import models
from macaddress.fields import MACAddressField


# Create your models here. 
class RouterDetails(models.Model):
    # loop_back = models.CharField(primary_key=True, max_length=100, blank=False, default="", unique=True)
    loop_back = models.GenericIPAddressField(unique=True)
    sap_id = models.CharField(max_length=18, blank=False, default="", unique=True)
    host_name = models.CharField(max_length=14, blank=False, default="", unique=True)
    mac_address = MACAddressField(null=True, blank=True, default="", max_length=17, unique=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["loop_back"]
