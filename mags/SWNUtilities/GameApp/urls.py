from django.urls import path
from . import views
from GameApp.views import ModelsDropDown, index

urlpatterns = [
    path('', index.index, name='index'),
    # path('CharacterCreation/', views.CharacterCreation, name='character_creation'),
    path('models/', ModelsDropDown.models_choice, name='models'),
]
