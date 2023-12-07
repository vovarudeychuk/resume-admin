from rest_framework import generics
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()  # Adjust the queryset as needed
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        # Filter only the active CV
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
 
        return Response(serializer.data)

    