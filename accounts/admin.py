from django.contrib import admin
from accounts.models import User, Profile
# Register your models here.

class Userdmin(admin.ModelAdmin):
    list_filter = ["role"]
    search_fields = ('username','first_name','last_name')


admin.site.register(User,Userdmin)
admin.site.register(Profile)