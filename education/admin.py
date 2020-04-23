from django.contrib import admin
from .models import Education

# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Education, EducationAdmin)