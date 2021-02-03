from django.contrib import admin

# Register your models here.
# from django_rest_blog.apps.users.models import User
from apps.users.models import User

admin.site.register(User)
