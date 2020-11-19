from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""
    list_display = ("name", "used_by",)

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        ("Basic Info",
         {"fields": ("name", "description", "country", "address", "price")}
         ),
        ("Times",
         {"fields": ("check_in", "check_out", "instant_book")}
         ),
        ("Spaces",
         {"fields": ("beds", "bedrooms", "baths")}
         ),
        ("More About Spaces",
         {"fields": ("amenities", "facilities", "house_rules",)}
         ),
        ("Last Details",
         {"fields": ("host",)}
         ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    list_filter = ("instant_book",
                   "room_type",
                   "amenities",
                   "facilities",
                   "house_rules",
                   "city",
                   "country",
                   )

    search_fields = ("city", "host__username",)
    filter_horizontal = ("amenities", "facilities", "house_rules",)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""
    pass
