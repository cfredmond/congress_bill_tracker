from rest_framework import serializers
from .models import Bill
        
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'title', 'number', 'bill_type', 'url')