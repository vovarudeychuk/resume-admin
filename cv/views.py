from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Cv
from .serializers import CvSerializerList

class CvApiView(generics.ListCreateAPIView):
    queryset = Cv.objects.all()
    serializer_class = CvSerializerList

    def get(self, request, *args, **kwargs):
        # Filter only the active CV
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
 
        return Response(serializer.data)
