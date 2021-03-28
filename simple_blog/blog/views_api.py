from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters


from .serializers import BlogModelSerializer


from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']


class BlogListAPIView(APIView) : 
    def get(self, request, *args, **kwargs) : 
        blogs = Blog.objects.all()
        serializer = BlogModelSerializer(blogs, many=True)
        return Response(serializer.data)

class BlogListAPIGenericView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer


class BlogInstantAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
