from django.contrib import admin

from .models import organizaations,Branches,users,co_relation

# Register your models here.

admin.site.register(organizaations)
admin.site.register(Branches)
admin.site.register(users)
admin.site.register(co_relation)
