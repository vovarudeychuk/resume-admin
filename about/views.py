from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import About, Client, Service, Testimonial
from .serializers import AboutSerializer



class AboutListView(generics.ListAPIView):
    queryset = About.objects.all()  # Adjust the queryset as needed
    serializer_class = AboutSerializer

    def get(self, request, *args, **kwargs):
        # Filter only the active CV
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
 
        return Response(serializer.data)



# class AboutView(generics.RetrieveAPIView):
#     queryset = About.objects.all()
#     serializer_class = AboutSerializer

# class ClientListView(generics.ListAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# class ServiceListView(generics.ListAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer

# class TestimonialListView(generics.ListAPIView):
#     queryset = Testimonial.objects.all()
#     serializer_class = TestimonialSerializer

# class CombinedDataAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         about_instance = About.objects.first()
#         client_instance = Client.objects.first()
#         service_instance = Service.objects.first()
#         testimonial_instance = Testimonial.objects.first()

#         about_serializer = AboutSerializer(about_instance)
#         client_serializer = ClientSerializer(client_instance)
#         service_serializer = ServiceSerializer(service_instance)
#         testimonial_serializer = TestimonialSerializer(testimonial_instance)

#         combined_data = {
#             'about': about_serializer.data,
#             'client': client_serializer.data,
#             'service': service_serializer.data,
#             'testimonial': testimonial_serializer.data,
#         }

#         return Response(combined_data, status=status.HTTP_200_OK)