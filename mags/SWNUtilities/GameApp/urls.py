from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.index, name='index'),
    # path('CharacterCreation/', views.CharacterCreation, name='character_creation'),
    path('models/',
         views.ModelsDropDown.models_choice,
         name='models'),

    path('character/list/',
         views.CharacterList.as_view(),
         name='character_list'),

    path('character/create/',
         views.CharacterCreate.as_view(),
         name='character_create'),

    path('character/<int:pk>/detail/',
         views.CharacterDetail.as_view(),
         name='character_detail'),

    path('character/<int:pk>/update/',
         views.CharacterUpdate.as_view(),
         name='character_update'),

    path('character/<int:pk>/delete/',
         views.CharacterDelete.as_view(),
         name='character_delete'),

    path('party/create/',
         views.PartyCreate.as_view(),
         name='party_create'),

    path('party/<int:pk>/update/',
         views.PartyUpdate.as_view(),
         name='party_update'),

    path('party/list/',
         views.PartyCharactersList.as_view()),

    path('party/add/',
         views.AddCharacterToParty.CharacterChoice)
]
