from django.db import models


class sqlserverconn(models.Model):
	brand_id=models.IntField()
	brand_name=models.CharField(max_length=255)