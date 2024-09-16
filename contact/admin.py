from django.contrib import admin
from .models import Contact, ContactInfo


# Register your models here.


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'phone')
    list_display_links = ('id', 'address', 'phone')
    search_fields = ('phone', 'email')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    list_display_links = ('id', 'name', 'email', 'subject')
    search_fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
