from django.db import models
from django.forms import ModelForm
from django.utils import timezone

class jobd(models.Model):
    jd_id =models.AutoField(primary_key=True)
    company = models.CharField(
		max_length=100
	)
    field = models.CharField(
		max_length=100
	)
    designation = models.CharField(
		max_length=100
	)
    skills = models.CharField(
    	max_length =100
    )
    education = models.CharField(
    	max_length =100
    )
    experience = models.CharField(
    	max_length =100
    )

# def my_function(self):
#     return self.company
# Create your models here.
