from rest_framework import serializers
from .models import Listing, SlidePics

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'slug')

class listingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'

class SlidePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlidePics
        fields = '__all__'
