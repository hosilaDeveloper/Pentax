from rest_framework import generics
from .models import Category, HappyClients, Project, Service, Price, Tag, About, Blog
from .serializer import TagSerializer, AboutSerializer, CategorySerializer, ServiceSerializer, ProjectSerializer, \
    BlogSerializer, PriceSerializer, HappyClientsSerializer


# Create your views here.

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class HappyClientsView(generics.ListAPIView):
    queryset = HappyClients.objects.all()
    serializer_class = HappyClientsSerializer


class PriceView(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogView(generics.ListAPIView):
    queryset = (Blog.objects.all())
    serializer_class = BlogSerializer

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')

        if tag:
            return Blog.objects.filter(tags__name=tag)
        if category:
            return Blog.objects.filter(category__name=category)
        if q:
            return Blog.objects.filter(title__icontains=q)
