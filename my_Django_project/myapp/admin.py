from django.contrib import admin
from myapp.models import student

# Register your models here.

class studentAdmin(admin.ModelAdmin):
	list_display = ('title','email','content', 'image','status')
	list_filter = ('created','updated','author')
	search_fields = ('author','title','email')
	prepopulated_fields = {'slug':('title',)}
	list_editable = ('status',)
	date_hierarchy = ('created')

admin.site.register(student,studentAdmin)