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
import subprocess
from gobject import GError

class GNUPG(object):
    """
    GNUPG class
    """
    def __init__(self, error_dialog, s_keyring=None, p_keyring=None, use_agent=True):

        gpg_path = self.find_gpg_path()

        self.gpg = gnupg.GPG(secring=s_keyring,
                keyring=p_keyring,
                use_agent=use_agent)
        self.error_dialog = error_dialog
    #__init__()

    def find_gpg_path(self):
        return subprocess.check_output(['which', 'gpg2']).strip()
    # find_gpg_path()

    def decrypt_file(self, image_file, gpg_passphrase=None):
        """
        This method decrypt a image file
        """
        decrypted_file = self.gpg.decrypt_file(open(image_file, 'rb'),
                                               passphrase=gpg_passphrase)

        pbl = gtk.gdk.PixbufLoader()
        pbl.write(decrypted_file.data)

        try:
            pixbuf = pbl.get_pixbuf()
        except:
            if self.error_dialog:
                self.error_dialog.run()
                self.error_dialog.hide()
            raise
        finally:
            pbl.close()

        return pixbuf
    #decryptFile()
