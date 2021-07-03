from django.urls import path
from . import views
from GameApp.views import ModelsDropDown
from GameApp.views import CharacterList, CharacterCreate, CharacterUpdate
from GameApp.views import CharacterDetail, CharacterDelete
from GameApp.views import AttributeCreate
from GameApp.views import character_choice
from GameApp.views import PartyCharacterList
from GameApp.views import PlayerList, PlayerCreate, PlayerDelete, PlayerUpdate, PlayerDetail, PlayerCharacterList
from GameApp.views import FactionList, FactionCreate, FactionDelete, FactionUpdate, FactionDetail, FactionCharacterList
from GameApp.views import BackgroundDetail, BackgroundList, BackgroundUpdate, BackgroundDelete, BackgroundCreate
from GameApp.views import AddCharacterBackground
urlpatterns = [

    # Base View
    path('', views.index.index, name='index'),

    # Models
    path('models/',
         ModelsDropDown.models_choice,
         name='models'),

    # Character
    path('character/list/',
         CharacterList.as_view(),
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

    # Party
    path('party/create/',
         views.PartyCreate.as_view(),
         name='party_create'),

    path('party/<int:pk>/update/',
         views.PartyUpdate.as_view(),
         name='party_update'),

    path('party/list/',
         PartyCharacterList.as_view(),
         name='main_party_list'),

    path('party/add/',
         character_choice,
         name='add_char_to_party'),

    # PLAYERS
    path('player/create/',
         PlayerCreate.as_view(),
         name='player_create'),

    path('player/<int:pk>/delete',
         PlayerDelete.as_view(),
         name='player_delete'),

    path('player/list/',
         PlayerList.as_view(),
         name='player_list'),

    path('player/<int:pk>/update',
         PlayerUpdate.as_view(),
         name='player_update'),

    path('player/<int:pk>/detail',
         PlayerDetail.as_view(),
         name='player_detail'),

    path('player/<int:pk>/character/list',
         PlayerCharacterList.as_view(),
         name='player_character_list'),

    # Factions
    path('faction/create/',
         FactionCreate.as_view(),
         name='faction_create'),

    path('faction/<int:pk>/delete',
         FactionDelete.as_view(),
         name='faction_delete'),

    path('faction/list/',
         FactionList.as_view(),
         name='faction_list'),

    path('faction/<int:pk>/update',
         FactionUpdate.as_view(),
         name='faction_update'),

    path('faction/<int:pk>/detail',
         FactionDetail.as_view(),
         name='faction_detail'),

    path('faction/<int:pk>/list/',
         FactionCharacterList.as_view(),
         name='faction_character_list'),

    # background
    path('background/<int:pk>/detail/',
         BackgroundDetail.as_view(),
         name='background_detail'
         ),

    path('background/create/',
         BackgroundCreate.as_view(),
         name='background_create'
         ),

    path('background/<int:pk>/delete',
         BackgroundDelete.as_view(),
         name='background_delete'
         ),

    path('background/list/',
         BackgroundList.as_view(),
         name='background_list'
         ),

    path('background/<int:pk>/update',
         BackgroundUpdate.as_view(),
         name='background_update'
         ),

    # CHARACTER CREATION

    # Attributes
    path('character/<int:pk>/attribute/add/',
         AttributeCreate.as_view(),
         name='attribute_creation'),

    # Background
    path('character/<int:pk>/background/add/',
         AddCharacterBackground.as_view(),
         name='add_background'),

]
