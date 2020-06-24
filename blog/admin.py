from django.contrib import admin
from . import models

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'status',
        'created',
        'updated'
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name'
    )

    list_filter = (
        'status',
        'topics',
    )

    prepopulated_fields = {'slug': ('title',)}

# Register the post models
admin.site.register(models.Post, PostAdmin) #admin.site.register function
