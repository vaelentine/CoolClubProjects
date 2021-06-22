from django.urls import path
from . import views
from .views import ModelsDropDown, index, CharacterList, CharacterDelete, CharacterUpdate, CharacterCreate, CharacterDetail

urlpatterns = [
    path('', index.index, name='index'),
    # path('CharacterCreation/', views.CharacterCreation, name='character_creation'),
    path('models/',
         ModelsDropDown.models_choice,
         name='models'),

    path('characters',
         views.CharacterList.as_view(),
         name='character_list'),

    path('character/create',
         CharacterCreate.as_view(),
         name='character_create'),

    path('character/<int:pk>',
         CharacterDetail.as_view(),
         name='character_detail'),

    path('character/update/<int:pk>',
         CharacterUpdate.as_view(),
         name='character_update'),

    path('character/delete/<int:pk>',
         CharacterDelete.as_view(),
         name='character_delete')
]
