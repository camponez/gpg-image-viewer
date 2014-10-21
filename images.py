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

import os
import glob

class Images(object):
    """
    Image class
    """
    def __init__(self):
        self.__dir_name = None
        self.__list_dir = []
        self.__current = None
    # __init__()

    def load_images(self, image):
        """
        Load images
        """
        self.__dir_name = os.path.dirname(image)

        # everytime it loads should start with a blank list
        self.__list_dir = []

        for img in ["/*.jpg", "/*.png", "/*.gpg"]:
            self.__list_dir += (glob.glob(self.__dir_name+img))

        self.__list_dir.sort()

        self.__current = self.__list_dir.index(image)
    # load_images()

    @property
    def image(self):
        """
        Image path
        """
        if self.__current >= 0:
            return self.__list_dir[self.__current]
        else:
            return None

    # image()

    def next(self):
        """
        Go to previous images
        """

        if not self.__list_dir:
            return

        if len(self.__list_dir) > self.__current + 1:
            self.__current += 1

        return self.image

    # next()

    def prev(self):
        """
        Go to previous images
        """

        if not self.__list_dir:
            return

        if self.__current - 1 >= 0:
            self.__current -= 1

        return self.image
    # prev()

    @property
    def num_images(self):
        """
        Get number of images
        """
        return len(self.__list_dir)
    # num_images()

    def get_last(self):
        """
        Return last image
        """
        return self.__list_dir[self.num_images - 1]
    # get_last()

    def get_first(self):
        """
        Return first image
        """
        return self.__list_dir[0]
    # get_first()

