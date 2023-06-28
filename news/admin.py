from django.contrib import admin
from .models import Articles, Category


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'full_text', 'is_published', 'cat', 'date',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'full_text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'date')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'full_text', 'is_published', 'cat', 'date')
    readonly_fields = ('date', 'cat')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.site_title = 'Только для крутых'
admin.site.site_header = 'Админка для крутых'