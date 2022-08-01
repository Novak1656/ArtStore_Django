from django.contrib import admin
from .models import Art, Genre, Gallery


class ArtAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'prise',)
    list_display_links = ('id', 'title',)
    list_filter = ('author', 'genre', 'prise',)
    search_fields = ('title', 'author',)


admin.site.register(Art, ArtAdmin)
admin.site.register(Genre)
admin.site.register(Gallery)
