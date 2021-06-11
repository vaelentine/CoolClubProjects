from django.urls import path

from . import views



urlpatterns = [
    path('', views.index),
    path('pronouns/', views.pronouns),
    path('pronouns/upload/', views.pronouns_bulk_upload),
    path('background/upload/', views.background_upload),
    path('skill/upload/', views.skill_upload),
    path('species/upload/', views.species_upload),
    path('CharClass/upload', views.char_class_upload),
    path('ClassAbility/upload', views.class_ability_upload),
    path('Character/upload', views.character_upload)
]

