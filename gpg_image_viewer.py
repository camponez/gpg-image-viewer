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

import gi
from crypto import GNUPG
from images import Images
import sys
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf

import magic


class GPGImageViewer:
    """
    Image Viewer class
    """

    def __init__(self, glade_file):
        self.gtk_builder = Gtk.Builder()
        self.gtk_builder.add_from_file(glade_file)

        self.gpg = GNUPG(self.gtk_builder.get_object('error_decrypt_dialog'))

        self.window = self.gtk_builder.get_object('mainWindow')
        self.image = self.gtk_builder.get_object('imageView')

        signals = {"on_mainWindow_destroy": Gtk.main_quit,
                   "on_menu_quit_activate": Gtk.main_quit,
                   "on_menu_open_activate": self.cb_show_file_chooser,
                   "on_go_left_button_clicked": self.cb_go_left_image,
                   "on_go_right_button_clicked": self.cb_go_right_image,
                   }

        self.gtk_builder.connect_signals(signals)

        self.images = Images()

        self.prev_button = self.gtk_builder.get_object('go_left_button')
        self.next_button = self.gtk_builder.get_object('go_right_button')
        self.gtk_builder.get_object('ok_passphrase_button').grab_default()

    def cb_go_left_image(self, cb_data):
        """
        Show previous image
        """
        self.show_image(self.images.prev())
    # cb_go_left_image()

    def cb_go_right_image(self, _data):
        """
        Show to next image
        """
        self.show_image(self.images.next())
    # cb_go_right_image()

    def cb_show_file_chooser(self, _data):
        """
        Show file chooser
        """
        file_chooser = self.gtk_builder.get_object('file_chooser_dialog')
        response = file_chooser.run()
        file_chooser.hide()

        if response != Gtk.ResponseType.OK:
            return

        image_file = file_chooser.get_filename()

        self.images.load_images(image_file)

        self.show_image(image_file)
    # cb_show_file_chooser()

    def is_gpg_file(self, file_type):
        if file_type.startswith('GPG encrypted data'):
            return True

        if file_type.startswith('PGP RSA encrypted'):
            return True

        return False
    # is_gpg_file()

    def show_image(self, image_path):
        """
        Function show_image
        """

        if not image_path:
            return

        self.images.load_images(image_path)

        self.prev_button.set_sensitive(self.images.image !=
                                       self.images.get_first())
        self.next_button.set_sensitive(self.images.image !=
                                       self.images.get_last())

        # detect if it's a supported image type
        # if not check if is encrypted
        # fail otherwise
        # if not GdkPixbuf.Pixbuf.get_file_info(image_path):

        file_type = magic.from_file(image_path)

        if self.is_gpg_file(file_type):

            pixbuf = self.gpg.decrypt_file(image_path)
        else:
            not_supported_dialog = \
                self.gtk_builder.get_object('not_supported_dialog')

            not_supported_msg = file_type + ' is not a supported file!'
            not_supported_dialog.set_markup(not_supported_msg)
            not_supported_dialog.run()
            not_supported_dialog.hide()
            return

        # else:
        #     pixbuf = GdkPixbuf.Pixbuf.new_from_file(image_path)

        pixbuf = pixbuf.apply_embedded_orientation()
        width = pixbuf.get_width()
        height = pixbuf.get_height()

        while width > 900 or height > 900:
            width = width * .9
            height = height * .9

        width = int(width)
        height = int(height)

        resize_pixbuf = pixbuf.scale_simple(width, height,
                                            GdkPixbuf.InterpType.HYPER)

        main_label = self.gtk_builder.get_object('main_label')
        main_label.set_label("Image " + os.path.basename(image_path) +
                             " size: " + str(width) + " x " + str(height))

        self.image.set_from_pixbuf(resize_pixbuf)

    def __get_user_pw(self):
        """
        This function returns the passphrase that will be used for the GPG
        encrypted files.
        """

        dialog_window = self.gtk_builder.get_object('passwordDialog')
        user_entry = self.gtk_builder.get_object('passphrase_entry')

        response = dialog_window.run()
        text = user_entry.get_text()

        dialog_window.hide()

        if (response == gtk.RESPONSE_OK) and (text != ''):
            return text
        else:
            return None
    # __get_user_pw()


if __name__ == '__main__':

    IMG = None
    if len(sys.argv) > 1:
        IMG = sys.argv[1]

    GPGImageViewer("gpg_image_viewer.glade").show_image(IMG)
    Gtk.main()
