import gnupg
import os
import tempfile
import gtk

"""
This file is part of GPG Image Viewer.

    GPG Image Viewer is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

class GNUPG:
    """
    GNUPG class
    """
    def __init__(self, error_dialog):
        self.gpg = gnupg.GPG()
        self.error_dialog = error_dialog
    #__init__()

    def decryptFile(self, imageFile, passphrase):
        """
        This method decrypt a image file
        """
        decryptFile = self.gpg.decrypt_file(open(imageFile, 'rb'),
                passphrase = passphrase)

        image_path = tempfile.mkstemp()
        open(image_path[1], 'wb').write(decryptFile.data)

        try:
            pixbuf = gtk.gdk.pixbuf_new_from_file(image_path[1])
        except:
            self.error_dialog.run()
            self.error_dialog.hide()
            raise

        os.remove(image_path[1])

        return pixbuf
    #decryptFile()
