import unittest
from point.point import Point


class TestPoint(unittest.TestCase):
    def test_constructor(self):
        point = Point()

        self.assertEqual(point.x, 0.0)
        self.assertEqual(point.y, 0.0)

    def test_operators(self):
        p1 = Point()
        p2 = Point(2, 8)

        self.assertTrue(p1 != p2)
        self.assertFalse(p1 == p2)

    def test_raises(self):
        point = Point()

        with self.assertRaises(TypeError):
            point.distance(10)


if __name__ == '__main__':
    unittest.main()
