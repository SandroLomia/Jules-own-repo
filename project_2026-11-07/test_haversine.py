import unittest
from haversine import calculate_haversine_distance

class TestHaversineDistance(unittest.TestCase):

    def test_identical_coordinates(self):
        # Distance between the exact same point should be 0
        dist = calculate_haversine_distance(40.7128, -74.0060, 40.7128, -74.0060)
        self.assertAlmostEqual(dist, 0.0, places=4)

    def test_negative_coordinates(self):
        # Test coordinates in the southern and eastern hemispheres (e.g., Sydney to Buenos Aires)
        # Sydney: -33.8688, 151.2093
        # Buenos Aires: -34.6037, -58.3816
        dist = calculate_haversine_distance(-33.8688, 151.2093, -34.6037, -58.3816)
        # Expected distance is around 11790 km
        self.assertTrue(11700 < dist < 11900)

    def test_known_distance_ny_london(self):
        # New York City: 40.7128° N, 74.0060° W
        # London: 51.5074° N, 0.1278° W
        dist = calculate_haversine_distance(40.7128, -74.0060, 51.5074, -0.1278)
        # Expected distance is approximately 5570 km
        self.assertTrue(5500 < dist < 5600)

    def test_equator_distance(self):
        # Test distance along the equator (1 degree of longitude is ~111.32 km)
        dist = calculate_haversine_distance(0.0, 0.0, 0.0, 1.0)
        self.assertAlmostEqual(dist, 111.19, places=1) # Haversine with R=6371 gives ~111.19 km

if __name__ == '__main__':
    unittest.main()
