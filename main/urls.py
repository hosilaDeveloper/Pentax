from django.urls import path
from .views import BlogView, BlogDetailView, AboutView, HappyClientsView, ProjectView, PriceView, TagView, CategoryView, \
    ServiceView

urlpatterns = [
    path('', BlogView.as_view(), name='post-list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('category/', CategoryView.as_view(), name='category-list'),
    path('tag/', TagView.as_view(), name='tags'),
    path('service/', ServiceView.as_view(), name='services'),
    path('project/', ProjectView.as_view(), name='projects'),
    path('about/', AboutView.as_view(), name='abouts'),
    path('happy/', HappyClientsView.as_view(), name='happy-clients'),
    path('price/', PriceView.as_view(), name='price')
]
