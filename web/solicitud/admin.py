from django.contrib import admin
from .models import Category, GameImage, Comment

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class GameImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','user','published')
    ordering = ('user','published')
    search_fields = ('title','user__username')
    date_hierarchy = ('published')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'game', 'created')
    search_fields = ('author_name', 'text')
    list_filter = ('created',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(GameImage, GameImageAdmin)
admin.site.register(Comment, CommentAdmin)