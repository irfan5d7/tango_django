from django.contrib import admin
from rango.models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','views','likes']
    prepopulated_fields = {'slug':('name',)}
    class Meta:
        model = Category

class PageAdmin(admin.ModelAdmin):
    list_display = ['title','category','url']
    class Meta:
        model = Page

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)