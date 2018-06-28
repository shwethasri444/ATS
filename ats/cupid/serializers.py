from rest_framework import serializers
from .models import jobd

class jdSerializer(serializers.ModelSerializer):

	class Meta:
		model=jobd
		fields='__all__'
