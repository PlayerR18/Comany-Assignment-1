from django.db import models

class Order(models.Model):
    user = models.CharField(max_length=100)
    order_date = models.DateField()
    company_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    weight = models.FloatField()
    shipment_request = models.CharField(max_length=100)
    tracking_id = models.CharField(max_length=100)
    length = models.IntegerField()
    breadth = models.IntegerField()
    height = models.IntegerField()
    box_count = models.IntegerField()
    specification = models.CharField(max_length=100)
    quality_checklist = models.CharField(max_length=100)
    

