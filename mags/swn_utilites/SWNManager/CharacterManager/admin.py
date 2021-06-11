from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Pronouns, Background, Skill, Character, SkillLevel, CharClass, ClassAbility

admin.site.register(Pronouns)
admin.site.register(Skill)
admin.site.register(Character)
admin.site.register(SkillLevel)
# admin.site.register(CharClass)
# admin.site.register(ClassAbility)