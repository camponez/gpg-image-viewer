from crypto import GNUPG
import unittest
import os
import filecmp

class TestCrypto(unittest.TestCase):
    def setUp(self):
        self.fixture_dir = os.path.dirname(__file__)+"/fixtures/gnupg"
        self.gnupg = GNUPG(None, self.fixture_dir+"/gpg.key")
    # setUp()

    def test_decrypt_file(self):
        """
        Test decrypting file
        """
        d_file = self.fixture_dir+"/image10.jpg.gpg"
        no_d_file = self.fixture_dir+"/temp_image10.jpg"

        d_pixbuf = self.gnupg.decrypt_file(d_file, 'gpg-image-viewer')

        d_pixbuf.save(no_d_file, "jpeg")

        self.assertTrue(filecmp.cmp(no_d_file, no_d_file))

        os.remove(no_d_file)

    # test_decrypt_file()
