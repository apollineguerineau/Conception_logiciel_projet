import unittest

from adresse import Adresse


class AdresseTest(unittest.TestCase):
    '''teste les fonctions de la classe Adresse
    '''
    def test_donne_latitude_longitude(self):
        '''vérifie que la fonction retourne bien la bonne latitude
        et longitude'''
        adresse = Adresse(10, "Place", "Paul et Jean-Paul Avisseau", 33300)
        expected = [45.259605, -1.078761]
        actual = adresse.donne_latitude_longitude()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
