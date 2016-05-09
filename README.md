# 
A collection of code we used for the project extracting relevant images from the yelp data set
Here is a a breif description of what the programs and in the repository are, and what they do

Get TestarauntImages  is a java program that lets you specify a scorce folder, desination file, and destination path, and also a json file it goes though every file in the scorce folder and if it is also contained in the json file then that file gets moved to the destination, this is useful if we queried a subset of images using apache drill then we can get folder contaiing only that subset
Author- Tim
Give captions to images is a java program that takes in a .txt file that is copied form the matlab consol containin the a photo id and the new catagory that the image processor gave to that image. It inserts the new captions into the json file that containins those inage ids and labels.
Author-Tim
getFileNames is a bash scpipt that returns a texxt file that contains all the names of files in a folder, this was used for getting photo ids in a folder for use in matlab
Author-Tim
