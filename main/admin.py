from django.contrib import admin
from .models import Category, HappyClients, Project, Service, Price, Tag, About, Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title', 'category')
    filter_horizontal = ('tag',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(HappyClients)
admin.site.register(Price)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Tag)
admin.site.register(About)
