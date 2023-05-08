from django.contrib import admin
from .models import(
    Users,Category,Item
)


admin.site.register(
    [Users,Category,Item]
)