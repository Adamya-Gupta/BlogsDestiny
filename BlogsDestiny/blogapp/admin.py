from django.contrib import admin
from .models import Category , Post

# Register your models here.

#for configuration of Category admin
class Categoryadmin(admin.ModelAdmin):
    list_display=( 'image_tag' ,'title', 'description' ,'url' ,'add_date' )
    search_fields=('title' ,)
    
class Postadmin(admin.ModelAdmin):
    list_display=('title' ,)
    search_fields=('title' ,)
    list_filter=('cat',)
    list_per_page = 50
    
    class Media:
        js = ( 'https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.8.2/tinymce.min.js','js/script.js' ,)
    


admin.site.register(Category, Categoryadmin)
admin.site.register(Post,Postadmin)
