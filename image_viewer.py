#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Eduardo Elias"
__copyright__ = "Copyright 2014, GPG Image viewer"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Eduardo Elias"
__email__ = "camponez@gmail.com"

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import os
import pygtk

try:
    pygtk.require('2.0')
except:
    sys.exit(0)

import gtk
import magic
import gtk.glade

from crypto import GNUPG
from images import Images


class ImageViewer:
    """
    Image Viewer class
    """

    def __init__(self, gladeFile):
        self.gtkBuilder = gtk.Builder()
        self.gtkBuilder.add_from_file(gladeFile)

        self.gpg = GNUPG(self.gtkBuilder.get_object('error_decrypt_dialog'))

        self.window = self.gtkBuilder.get_object('mainWindow')
        self.image = self.gtkBuilder.get_object('imageView')

        signals = {
            "on_mainWindow_destroy" : gtk.main_quit,
            "on_menu_quit_activate" : gtk.main_quit,
            "on_menu_open_activate" : self.showFileChooser,
            "on_go_left_button_clicked" : self.goLeftImage,
            "on_go_right_button_clicked": self.goRightImage,
             }

        self.gtkBuilder.connect_signals(signals)
        self.passphrase = None

        self.images = Images()

    def goLeftImage(self, data):
        self.showImage(self.images.prev())
    # goLeftImage()

    def goRightImage(self, data):
        self.showImage(self.images.next())
    # goRightImage()

    def showFileChooser(self, data):
        file_chooser = self.gtkBuilder.get_object('file_chooser_dialog')
        response = file_chooser.run()
        file_chooser.hide()

        if response != gtk.RESPONSE_OK:
            return

        imageFile = file_chooser.get_filename()

        self.images.loadImages(imageFile)

        self.showImage(imageFile)
    # showFileChooser()

    def showImage(self, image_path):
        """
        Function showImage
        """

        # detect if it's a supported image type
        #if not check if is encrypted
        # fail otherwise
        if not gtk.gdk.pixbuf_get_file_info(image_path):

            file_type = magic.from_file(image_path)

            if  file_type == 'GPG encrypted data':
                if not self.passphrase:
                    self.passphrase = self.__get_user_pw()

                try:
                    pixbuf = self.gpg.decryptFile(image_path, self.passphrase)
                except:
                    return

            else:
                not_supported_dialog = \
                self.gtkBuilder.get_object('not_supported_dialog')

                not_supported_msg = file_type + ' is not a supported file!'
                not_supported_dialog.set_markup(not_supported_msg)
                not_supported_dialog.run()
                not_supported_dialog.hide()
                return

        else:
            pixbuf = gtk.gdk.pixbuf_new_from_file(image_path)


        width = pixbuf.get_width()
        height = pixbuf.get_height()

        while width > 1900 or height > 1000:
            width = width * .9
            height = height * .9

        width = int(width)
        height = int(height)

        resize_pixbuf = pixbuf.scale_simple(width, height, gtk.gdk.INTERP_HYPER)

        mainLabel = self.gtkBuilder.get_object('main_label')
        mainLabel.set_label("Image "+os.path.basename(image_path)+" size: " + str(width) + " x " + str(height))


        self.image.set_from_pixbuf(resize_pixbuf)

    def __get_user_pw(self):
        """
        This function returns the passphrase that will be used for the GPG
        encrypted files.
        """

        dialogWindow = self.gtkBuilder.get_object('passwordDialog')
        userEntry = self.gtkBuilder.get_object('passphrase_entry')

        response = dialogWindow.run()
        text = userEntry.get_text()

        dialogWindow.hide()

        if (response == gtk.RESPONSE_OK) and (text != ''):
            return text
        else:
            return None


if __name__ == '__main__':

    image = ImageViewer("image_viewer.glade")
    if len(sys.argv) > 1:
        image.showImage(sys.argv[1])

    gtk.main()
