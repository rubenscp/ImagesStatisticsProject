"""
Project: This project produces the statistics of images used in the training, validation and test.
Author: Rubens de Castro Pereira
Advisor: Dibio Leandro Borges
Date: 09/02/2021
Version: 1.0.0
"""

# Importing needed libraries

import os
import glob
from shutil import copyfile

# ###########################################
# Constants
# ###########################################
LINE_FEED = '\n'


# ###########################################
# Application Methods
# ###########################################


# ###########################################
# Methods of Level 1
# ###########################################


# process all annotated images
def processImagesFiles(imagesClassesPath, statisticFilename):
    # removing statistic file
    statisticFileAndPath = imagesClassesPath + statisticFilename
    if os.path.isfile(imagesClassesPath + statisticFilename):
        os.remove(statisticFileAndPath)

    # producing images statistics by classes
    produceStatisticsByClassName(imagesClassesPath, 'exuvia', statisticFilename)
    produceStatisticsByClassName(imagesClassesPath, 'instar1', statisticFilename)
    produceStatisticsByClassName(imagesClassesPath, 'instar2', statisticFilename)
    produceStatisticsByClassName(imagesClassesPath, 'instar3', statisticFilename)
    produceStatisticsByClassName(imagesClassesPath, 'instar4', statisticFilename)
    produceStatisticsByClassName(imagesClassesPath, 'adulta', statisticFilename)
    produceStatisticsByClassName(imagesClassesPath, 'ovo', statisticFilename)


# ###########################################
# Methods of Level 2
# ###########################################


# produczes statistics by class name
def produceStatisticsByClassName(imagesClassesPath, className, statisticFilename):
    # initializing variables
    numberOfImagesInCenter = countFiles(imagesClassesPath, className, 'center')
    numberOfImagesInNorth = countFiles(imagesClassesPath, className, 'north')
    numberOfImagesInSouth = countFiles(imagesClassesPath, className, 'south')
    numberOfImagesInEast = countFiles(imagesClassesPath, className, 'east')
    numberOfImagesInWest = countFiles(imagesClassesPath, className, 'west')
    numberOfImagesInNortheast = countFiles(imagesClassesPath, className, 'northeast')
    numberOfImagesInNorthwest = countFiles(imagesClassesPath, className, 'northwest')
    numberOfImagesInSoutheast = countFiles(imagesClassesPath, className, 'southeast')
    numberOfImagesInSouthwest = countFiles(imagesClassesPath, className, 'southwest')

    # saving statistics file
    saveCroppedBoundingBoxAnnotationFile(imagesClassesPath, statisticFilename, className,
                                         numberOfImagesInCenter, numberOfImagesInNorth, numberOfImagesInSouth,
                                         numberOfImagesInEast, numberOfImagesInWest, numberOfImagesInNortheast,
                                         numberOfImagesInNorthwest, numberOfImagesInSoutheast,
                                         numberOfImagesInSouthwest)

    # imagesStatisticsFile = open(imagesClassesPath + statisticFilename, 'a+')
    #
    # # setting line to write
    # line = str(className + ' ' \
    #            + str(numberOfImagesInCenter) + ' ' \
    #            + str(numberOfImagesInNorth) + ' ' \
    #            + str(numberOfImagesInSouth) + ' ' \
    #            + str(numberOfImagesInEast) + ' ' \
    #            + str(numberOfImagesInWest) + ' ' \
    #            + str(numberOfImagesInNortheast) + ' ' \
    #            + str(numberOfImagesInNorthwest) + ' ' \
    #            + str(numberOfImagesInSoutheast) + ' ' \
    #            + str(numberOfImagesInSouthwest) + ' ' \
    #            + LINE_FEED)
    #
    # # write line
    # imagesStatisticsFile.write(line)
    #
    # # closing annotation file
    # imagesStatisticsFile.close()


def saveCroppedBoundingBoxAnnotationFile(imagesClassesPath, statisticFilename, className,
                                         numberOfImagesInCenter, numberOfImagesInNorth, numberOfImagesInSouth,
                                         numberOfImagesInEast, numberOfImagesInWest, numberOfImagesInNortheast,
                                         numberOfImagesInNorthwest, numberOfImagesInSoutheast,
                                         numberOfImagesInSouthwest):
    # saving statistics file
    imagesStatisticsFile = open(imagesClassesPath + statisticFilename, 'a+')

    # setting line to write
    line = str(className + ' ' \
               + str(numberOfImagesInCenter) + ' ' \
               + str(numberOfImagesInNorth) + ' ' \
               + str(numberOfImagesInSouth) + ' ' \
               + str(numberOfImagesInEast) + ' ' \
               + str(numberOfImagesInWest) + ' ' \
               + str(numberOfImagesInNortheast) + ' ' \
               + str(numberOfImagesInNorthwest) + ' ' \
               + str(numberOfImagesInSoutheast) + ' ' \
               + str(numberOfImagesInSouthwest) + ' ' \
               + LINE_FEED)

    # write line
    imagesStatisticsFile.write(line)

    # closing annotation file
    imagesStatisticsFile.close()


# ###########################################
# Methods of Level 3
# ###########################################

# count number of files
def countFiles(imagesClassesPath, className, position):
    wildcardsText = imagesClassesPath + className + "/*-" + position + ".jpg"
    return len(glob.glob(wildcardsText))


# ###########################################
# Main method
# ###########################################
if __name__ == '__main__':
    IMAGES_CLASSES_PATH = 'E:/desenvolvimento/projetos/DoctoralProjects/CropMultipleBoundingBoxesProjectImages/Block 20/20.2 White Fly Cropped Images by Classes/'
    STATISTIC_FILENAME = '20.2 statisticsByClasses.txt'

    print('Statistics of Images')
    print('--------------------')
    print('')
    print('Images path         : ', IMAGES_CLASSES_PATH)
    print('Statistics filename : ', STATISTIC_FILENAME)
    print('')

    # processing the annotated images
    processImagesFiles(IMAGES_CLASSES_PATH, STATISTIC_FILENAME)

    # print('Total of Yolo annotations:', str(counter))
    print('End of processing')
