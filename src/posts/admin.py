from django.contrib import admin

# Register your models here.
# It's a relative import because the admin.py file is in same directory as models.py
# where Post() is defined. 
from .models import Post

admin.site.register(Post)