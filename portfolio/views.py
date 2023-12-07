from rest_framework.response import Response
from rest_framework import generics

from portfolio.serializers import PortfolioSerializer, PortfolioSerializerList

from .models import Portfolio


class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializerList
    
    def get(self, request, *args, **kwargs):
        # Filter only the active CV
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
 
        return Response(serializer.data)

    