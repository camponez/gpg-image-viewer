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

        self.__list_dir = os.listdir(self.__dir_name)
        self.__list_dir.sort()

        self.__current = self.__list_dir.index(os.path.basename(image))
    # load_images()

    def get_image(self):
        """
        Get Image
        """
        if not self.__list_dir:
            return None

        image_name = self.__list_dir[self.__current]
        image_path = self.__image_path(image_name)

        return image_path

    # get_image()

    def __image_path(self, image):
        """
        Image path
        """
        return self.__dir_name+'/'+image
    # imagePath()

    def next(self):
        """
        Go to previous images
        """

        if not self.__list_dir:
            return

        if len(self.__list_dir) > self.__current + 1:
            self.__current += 1

        return self.get_image()

    # next()

    def prev(self):
        """
        Go to previous images
        """

        if not self.__list_dir:
            return

        if self.__current - 1 >= 0:
            self.__current -= 1

        return self.get_image()
    # prev()

    def get_num_images(self):
        """
        Get number of images
        """
        return len(self.__list_dir)
    # get_num_images()

    def get_last(self):
        """
        Return last image
        """
        return self.__image_path(self.__list_dir[self.get_num_images() - 1])
    # get_last()

    def get_first(self):
        """
        Return first image
        """
        return self.__image_path(self.__list_dir[0])
    # get_first()

