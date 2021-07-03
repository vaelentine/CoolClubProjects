from django.test import TestCase
from unittest import mock
from django.db.utils import IntegrityError
from GameApp.models import Character, Attributes, Player, Faction, Party, Pronouns

class CharacterCreationUnitTests(TestCase):
    def setUp(self):
        self.mock = mock.Mock
