from django.contrib import admin
from .models import Post
# Register your models here.


class postAdmin(admin.ModelAdmin):
    list_display = ['user','slug','update']
    search_fields = ('slug','body')
    list_filter = ['update']
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)



#@admin.register(post)
#or
admin.site.register(Post,postAdmin)

