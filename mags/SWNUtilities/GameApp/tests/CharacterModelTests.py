from django.test import TestCase
from unittest import mock
from GameApp.models import Character, Attributes, Player, Faction, Party
from django.db.utils import IntegrityError

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
        self.mock.faction = 'The Greatest Test'
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

        faction = Faction.objects.create(name=self.mock.faction)
        test_obj.faction=faction
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

    def test_06_character_faction_attach(self):
        data_obj = Character.objects.get(name=self.mock.name_02)
        self.assertEqual(data_obj.faction.name, self.mock.faction)

    def test_07_attach_party_to_characters(self):
        party_obj = Party.objects.create() # create party
        party_obj.save()  # save it
        self.p_id = party_obj.id  # get id

        #  get characters and assign to party and save updates
        char_obj_1 = Character.objects.get(name='ImaTest')
        char_obj_2 = Character.objects.get(name='NotNotATestVar')
        char_obj_1.party = party_obj
        char_obj_1.save()
        char_obj_2.party = party_obj
        char_obj_2.save()
        # get all existing parties
        party = Party.objects.get(id=self.p_id)
        # reverse lookup all characters that have
        party.character_party.all()
        # characters should be found ny reverse lookuyp
        with self.subTest():
            self.assertIn(char_obj_1, party.character_party.all(), 'key is not in container')
        with self.subTest():
            self.assertIn(char_obj_2, party.character_party.all(), 'key is not in container')

    def test_08_non_unique_name_raises_integrity_error(self):
        test_name = 'Soo UnIqUe'
        test_obj = Character.objects.create(name=test_name)
        self.assertRaises(IntegrityError, lambda: Character.objects.create(name=test_name))

    def test_09_update_character_name(self):
        char_obj_1 = Character.objects.get(name='ImaTest')
        char_obj_1.name = 'NotImaTest'
        char_obj_1.save()
        with self.subTest():
            test_updated_obj = Character.objects.get(name='NotImaTest')
            self.assertEqual(test_updated_obj.name, 'NotImaTest')
        with self.subTest():
            self.assertRaises(Character.DoesNotExist, lambda: Character.objects.get(name='ImaTest'))

    def test_10_delete_character(self):
        char_obj = Character.objects.get(name=self.mock.name_02)
        char_obj_id = char_obj.id

        char_obj.delete()
        self.assertRaises(Character.DoesNotExist, lambda: Character.objects.get(id=char_obj_id))