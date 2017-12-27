from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Post, Tag, Catalog

admin.site.site_header = '核心操作流程'
admin.site.site_title = '核心操作流程Admin'


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_time', 'modified_time', 'category', 'author')
    list_filter = ['created_time']
    search_fields = ['title']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'menu_level')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Catalog, CatalogAdmin)
