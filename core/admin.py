from django.contrib import admin

from .models import Item, UserProfile


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user'
                    ]
    list_display_links = [
        'user'
    ]
    search_fields = [
        'user__username'
    ]


admin.site.register(Item)
admin.site.register(UserProfile)
