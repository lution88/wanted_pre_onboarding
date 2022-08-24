from django.contrib import admin

from employment.models import Company, Employment, User

# Register your models here.

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Employment)