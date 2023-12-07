from rest_framework import generics
from rest_framework.response import Response
from .models import Account 
from .serializers import CombinedAccountSerializer 
    
class CombinedAccountDataAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = CombinedAccountSerializer

    def get(self, request, *args, **kwargs):

        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
 
        return Response(serializer.data)
