from django.urls import path
from . import views
from .views import ModelsDropDown, index, CharacterList, CharacterDelete, CharacterUpdate, CharacterCreate, CharacterDetail, PartyCreate, PartyUpdate, PartyCharacters


urlpatterns = [
    path('', index.index, name='index'),
    # path('CharacterCreation/', views.CharacterCreation, name='character_creation'),
    path('models/',
         ModelsDropDown.models_choice,
         name='models'),

    path('character/list/',
         views.CharacterList.as_view(),
         name='character_list'),

    path('character/create/',
         CharacterCreate.as_view(),
         name='character_create'),

    path('character/<int:pk>/detail/',
         CharacterDetail.as_view(),
         name='character_detail'),

    path('character/<int:pk>/update/',
         CharacterUpdate.as_view(),
         name='character_update'),

    path('character/<int:pk>/delete/',
         CharacterDelete.as_view(),
         name='character_delete'),

    path('party/create/',
         PartyCreate.as_view(),
         name='party_create'),

    path('party/<int:pk>/update/',
         PartyUpdate.as_view(),
         name='party_update'),

    path('party/list/',
         PartyCharacters.as_view()),

    # path('party/add/',
    #      )
]
