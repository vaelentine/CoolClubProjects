from django.test import TestCase
from unittest import mock
from GameApp.models import Character, Attributes,Player


class CharacterModelUnitTests(TestCase):
    def setUp(self):
        self.mock = mock.Mock
        self.mock.name_01 = 'ImaTest'
        self.mock.name_02 = 'NotNotATestVar'
        self.mock.player = 'TestlyTests'
        self.mock.stats = {
            'strength':6,
            'dexterity': 9,
            'constitution':11,
            'intelligence':13,
            'wisdom':16,
            'charisma':18,
            'hit_point_max':20}
        Character.objects.create(name=self.mock.name_01)
        test_stats = Attributes.objects.create(
            strength=self.mock.stats['strength'],
            dexterity=self.mock.stats['dexterity'],
            constitution=self.mock.stats['constitution'],
            intelligence=self.mock.stats['intelligence'],
            wisdom=self.mock.stats['wisdom'],
            charisma=self.mock.stats['charisma'],
            hit_point_max=self.mock.stats['hit_point_max']
        )
        test_obj = Character.objects.create(name=self.mock.name_02)
        test_obj.attributes=test_stats
        test_obj.save()

        player = Player.objects.create(name=self.mock.player)
        test_obj.player=player
        test_obj.save()

    def test_01_char_object_creation(self):
        data_obj = Character.objects.get(name=self.mock.name_01)
        self.assertEqual(data_obj.__str__(), self.mock.name_01)

    def test_02_char_null_attributes(self):
        data_obj = Character.objects.get(name='ImaTest')
        self.assertIsNone(data_obj.attributes)

    def test_03_char_attribute_attach(self):
        test = Character.objects.get(name='NotNotATestVar')
        self.assertIsNotNone(test.attributes)

    def test_04_char_attribute_value(self):
        test = Character.objects.get(name='NotNotATestVar')
        self.assertEqual(test.attributes.wisdom, self.mock.stats['wisdom'])

    def test_05_player_character(self):
        data_obj = Character.objects.get(name=self.mock.name_02)
        self.assertEqual(data_obj.player.name, self.mock.player)