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
        self.__listDir = None
        self.__current = None
    # __init__()

    def loadImages(self, image):
        self.__dirName = os.path.dirname(image)

        self.__listDir = os.listdir(self.__dirName)
        self.__listDir.sort()

        self.__current = self.__listDir.index(os.path.basename(image))
    # loadImages()

    def getImage(self):
        image_name = self.__listDir[self.__current]
        image_path = self.__dirName+'/'+image_name

        return image_path

    # getImage()

    def next(self):

        self.__current += 1

        if len(self.__listDir) <= self.__current:
            self.__current -= 1

        return self.getImage()

    # next()

    def prev(self):
        self.__current -= 1

        if self.__current < 0:
            self.__current += 1

        return self.getImage()
    # prev()

    def getNumImages(self):
        return len(self.__listDir)
    # getNumImages()

