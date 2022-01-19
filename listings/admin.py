from django.contrib import admin
from .models import Listing
from .models import SlidePics

class ListingAdmin(admin.ModelAdmin):
    model = Listing
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    prepopulated_fields = {'slug': ('title',), }
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25


class SlidePicAdmin(admin.ModelAdmin):
    model = SlidePics
    list_display = ('image', 'alt')
    list_display_links = ('image', 'alt')
    list_per_page = 5


admin.site.register(Listing, ListingAdmin)
admin.site.register(SlidePics, SlidePicAdmin)
