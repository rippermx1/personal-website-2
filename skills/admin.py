from django.contrib import admin
from .models import Skill, SkillCategory

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class SkillCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)