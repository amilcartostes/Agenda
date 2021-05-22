from django.contrib import admin

# Register your models here.
# Importing Models classes
from .models import Contact, Category


# To list more fields in Contacts.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'telephone', 'email', 'category', 'creation_date', 'show')
    list_display_links = ('id', 'name', 'surname', 'email')
    list_filter = ('category',)
    list_per_page = 12
    list_editable = ('telephone', 'show')
    search_fields = ('name', 'surname', 'telephone', 'email')
    sortable_by = ('id', 'name', 'surname', 'telephone', 'email', 'category', 'creation_date')




# Registering the Category model on the site
admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
