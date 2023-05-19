from django.contrib import admin
from .models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'phone_number', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'phone_number')
    list_editable = ('is_published',)


admin.site.register(Contacts, ContactsAdmin)
