from django.contrib import admin
from Blog.models import POST
# Register your models here.


class POSTAdmin(admin.ModelAdmin):
    list_display = ['title','content','date_posted','author']


admin.site.register(POST,POSTAdmin)


