from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer
    
class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer