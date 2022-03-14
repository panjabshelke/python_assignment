from django.contrib import admin
from api.models import RouterDetails
# Register your models here.
@admin.register(RouterDetails)
class RouterDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'loop_back', 'host_name')
    list_filter = ('loop_back', 'host_name',)
    search_fields = ('loop_back', 'host_name',)
