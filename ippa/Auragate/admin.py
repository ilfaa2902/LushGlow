from django.contrib import admin
from .models import blog, contact, tips, rekomendation
# Register your models here.
admin.site.register(blog) 
admin.site.register(contact)
admin.site.register(tips)
admin.site.register(rekomendation)