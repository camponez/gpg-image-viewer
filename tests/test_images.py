import unittest
from images import Images
import os

class TestImages(unittest.TestCase):
    def setUp(self):
        self.images = Images()
        self.image = os.path.dirname(__file__)+'/fixtures/image4.jpg'
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

    def test_prevThanFirst(self):
        self.images.loadImages(self.image) # image4
        self.images.prev() # image3
        self.images.prev() # image2
        self.images.prev() # image1

        firstImage = os.path.dirname(__file__)+'/fixtures/image1.jpg'

        self.assertEqual(firstImage, self.images.getImage())

        self.images.prev() # image1

        self.assertEqual(firstImage, self.images.getImage())

    # test_prevThanFirst()

    def test_afterThanlast(self):
        self.images.loadImages(self.image) # image4
        self.images.next() # image5
        self.images.next() # image6
        self.images.next() # image7
        self.images.next() # image8
        self.images.next() # image9

        lastImage = os.path.dirname(__file__)+'/fixtures/image9.jpg'

        self.assertEqual(lastImage, self.images.getImage())

        self.images.next() # image9

        self.assertEqual(lastImage, self.images.getImage())

    # test_prevThanFirst()

