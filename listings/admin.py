from django.contrib import admin
from listings.models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'realtor')
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'state', 'zipcode', 'city')
    list_per_page = 20


admin.site.register(Listing, ListingAdmin)
