import unittest
from images import Images
import os

class TestImages(unittest.TestCase):
    def setUp(self):
        self.images = Images()
        self.image = os.path.dirname(__file__)+'/fixtures/image4.jpg'
        self.firstImage = os.path.dirname(__file__)+'/fixtures/image1.jpg'
        self.lastImage = os.path.dirname(__file__)+'/fixtures/image9.jpg'
    # setUp()

    def test_loadImages(self):
        image = os.path.dirname(__file__)+'/fixtures/image4.jpg'
        self.images.loadImages(image)
        self.assertEqual(image, self.images.getImage())
        self.assertEqual(9, self.images.getNumImages())
    # test_loadImages()

    def test_nextImage(self):
        self.images.loadImages(self.image)
        nextImage = os.path.dirname(__file__)+'/fixtures/image5.jpg'

        self.assertEqual(nextImage, self.images.next())
    # test_nextImage()

    def test_prevImage(self):
        self.images.loadImages(self.image)
        prevImage = os.path.dirname(__file__)+'/fixtures/image3.jpg'

        self.assertEqual(prevImage, self.images.prev())
    # test_nextImage()

    def test_prevFirst(self):
        self.images.loadImages(self.image) # image4
        self.images.prev() # image3
        self.images.prev() # image2
        self.images.prev() # image1

        self.assertEqual(self.firstImage, self.images.getImage())

        self.images.prev() # image1

        self.assertEqual(self.firstImage, self.images.getImage())

    # test_prevThanFirst()

    def test_afterLast(self):
        self.images.loadImages(self.image) # image4
        self.images.next() # image5
        self.images.next() # image6
        self.images.next() # image7
        self.images.next() # image8
        self.images.next() # image9

        self.assertEqual(self.lastImage, self.images.getImage())

        self.images.next() # image9

        self.assertEqual(self.lastImage, self.images.getImage())

    # test_prevThanFirst()

    def test_lastImage(self):
        """
        Return last image
        """
        self.images.loadImages(self.image)
        self.assertEqual(self.lastImage, self.images.getLast())
    # test_lastImage()

    def test_firstImage(self):
        """
        Return first Image
        """
        self.images.loadImages(self.image)
        self.assertEqual(self.firstImage, self.images.getFirst())
    # test_lastImage()

    def test_doNothingWhenEmpty(self):
        """
        Try to move with no images
        """

        self.assertIsNone(self.images.getImage())

        self.images.next()

        self.assertIsNone(self.images.getImage())

        self.images.prev()

        self.assertIsNone(self.images.getImage())

    # test_doNothingWhenEmpty()

if __name__ == '__main__':
    unittest.main()
