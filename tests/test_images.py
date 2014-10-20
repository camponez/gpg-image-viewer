import unittest
from images import Images
import os

class TestImages(unittest.TestCase):
    def setUp(self):
        self.images = Images()
        self.image = os.path.dirname(__file__)+'/fixtures/image4.jpg'
        self.first_image = os.path.dirname(__file__)+'/fixtures/image1.jpg'
        self.last_image = os.path.dirname(__file__)+'/fixtures/image9.jpg'
    # setUp()

    def test_load_images(self):
        image = os.path.dirname(__file__)+'/fixtures/image4.jpg'
        self.images.load_images(image)
        self.assertEqual(image, self.images.image)
        self.assertEqual(9, self.images.num_images)
    # test_load_images()

    def test_next_image(self):
        self.images.load_images(self.image)
        next_image = os.path.dirname(__file__)+'/fixtures/image5.jpg'

        self.assertEqual(next_image, self.images.next())
    # test_nextImage()

    def test_prev_image(self):
        self.images.load_images(self.image)
        prev_image = os.path.dirname(__file__)+'/fixtures/image3.jpg'

        self.assertEqual(prev_image, self.images.prev())
    # test_nextImage()

    def test_prev_first(self):
        self.images.load_images(self.image) # image4
        self.images.prev() # image3
        self.images.prev() # image2
        self.images.prev() # image1

        self.assertEqual(self.first_image, self.images.image)

        self.images.prev() # image1

        self.assertEqual(self.first_image, self.images.image)

    # test_prevThanFirst()

    def test_after_last(self):
        self.images.load_images(self.image) # image4
        self.images.next() # image5
        self.images.next() # image6
        self.images.next() # image7
        self.images.next() # image8
        self.images.next() # image9

        self.assertEqual(self.last_image, self.images.image)

        self.images.next() # image9

        self.assertEqual(self.last_image, self.images.image)

    # test_prevThanFirst()

    def test_last_image(self):
        """
        Return last image
        """
        self.images.load_images(self.image)
        self.assertEqual(self.last_image, self.images.get_last())
    # test_lastImage()

    def test_first_image(self):
        """
        Return first Image
        """
        self.images.load_images(self.image)
        self.assertEqual(self.first_image, self.images.get_first())
    # test_lastImage()

    def test_do_nothing_when_empty(self):
        """
        Try to move with no images
        """

        self.assertIsNone(self.images.image)

        self.images.next()

        self.assertIsNone(self.images.image)

        self.images.prev()

        self.assertIsNone(self.images.image)

    # test_doNothingWhenEmpty()

if __name__ == '__main__':
    unittest.main()
