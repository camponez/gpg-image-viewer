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

import gnupg
import os
import tempfile
import gtk


class GNUPG(object):
    """
    GNUPG class
    """
    def __init__(self, error_dialog, s_keyring=None):
        self.gpg = gnupg.GPG(secret_keyring=s_keyring)
        self.error_dialog = error_dialog
    #__init__()

    def decrypt_file(self, image_file, passphrase):
        """
        This method decrypt a image file
        """
        decrypted_file = self.gpg.decrypt_file(open(image_file, 'rb'),
                                               passphrase=passphrase)

        image_path = tempfile.mkstemp()
        open(image_path[1], 'wb').write(decrypted_file.data)

        try:
            pixbuf = gtk.gdk.pixbuf_new_from_file(image_path[1])
        except:
            if self.error_dialog:
                self.error_dialog.run()
                self.error_dialog.hide()
            raise
        finally:
            os.remove(image_path[1])

        return pixbuf
    #decryptFile()
