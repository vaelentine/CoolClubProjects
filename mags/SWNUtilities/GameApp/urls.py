from django.urls import path
from . import views
from GameApp.views import ModelsDropDown
from GameApp.views import CharacterList, CharacterCreate, CharacterUpdate
from GameApp.views import CharacterDetail, CharacterDelete
from GameApp.views import AttributeCreate
from GameApp.views import character_choice
from GameApp.views import PartyCharacterList

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

    # Attributes
    path('character/<int:pk>/attribute/add/',
         AttributeCreate.as_view()),

    # Party
    path('party/create/',
         views.PartyCreate.as_view(),
         name='party_create'),

    path('party/<int:pk>/update/',
         views.PartyUpdate.as_view(),
         name='party_update'),

    path('party/list/',
         PartyCharacterList.as_view()),

    path('party/add/',
         character_choice,
         name='add_char_to_party'),


]
