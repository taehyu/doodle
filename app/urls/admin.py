from django.contrib import admin

# Register your models here.
from urls.models import Parent, Child, Url


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid',)


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'parent', 'user')
    # list_select_related = False
    list_select_related = ('parent', 'user')

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('id',)