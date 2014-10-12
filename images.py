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

class Images:
    def __init__(self):
        self.__dirName = None
        self.__listDir = []
        self.__current = None
    # __init__()

    def loadImages(self, image):
        self.__dirName = os.path.dirname(image)

        self.__listDir = os.listdir(self.__dirName)
        self.__listDir.sort()

        self.__current = self.__listDir.index(os.path.basename(image))
    # loadImages()

    def getImage(self):
        if not self.__listDir:
            return None

        image_name = self.__listDir[self.__current]
        image_path = self.__imagePath(image_name)

        return image_path

    # getImage()

    def __imagePath(self, image):
        return self.__dirName+'/'+image
    # imagePath()

    def next(self):
        """
        Go to previous images
        """

        if not self.__listDir:
            return

        if len(self.__listDir) > self.__current + 1:
            self.__current += 1

        return self.getImage()

    # next()

    def prev(self):
        """
        Go to previous images
        """

        if not self.__listDir:
            return

        if self.__current - 1 >= 0:
            self.__current -= 1

        return self.getImage()
    # prev()

    def getNumImages(self):
        return len(self.__listDir)
    # getNumImages()

    def getLast(self):
        return self.__imagePath(self.__listDir[self.getNumImages() - 1])
    # getLast()

    def getFirst(self):
        return self.__imagePath(self.__listDir[0])
    # getFirst()

