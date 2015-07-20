from rest_framework import serializers
from myapp.models import Item


		
class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model=Item
		fields=('id','name_text')