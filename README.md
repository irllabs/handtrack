# Hand Tracker
This repository contains code for performing segmenting the human hand from the background using pixel-level classification.  This project is based on work by Cheng Li and Kris Kitani, and documented in the publication below: 

Cheng Li and Kris M. Kitani.
[Pixel-level Hand Detection for Ego-centric Videos](http://www.cs.cmu.edu/~kkitani/pdf/LK-CVPR13.pdf)
Conference on Computer Vision and Pattern Recognition (CVPR 2013). Jun 2013.

This project relies on OpenCV.

## Dependencies
### IDE
This project is ported to work in Apple's [Xcode]
Hand Tracker uses Xcode which can be installed from the Mac App Store [here](https://developer.apple.com/xcode/downloads/).

This project also uses the OpenCV library (Version 2.4.13 or 2.4.12) for C++. 
### OpenCV on OS X
Two ways to install OpenCV on OS X: 
  1. Using [Homebrew](http://brew.sh): `brew install opencv`
  	* Make sure OpenCV's dependencies are also installed, you can check using `brew info opencv`
  2. Downloading [OpenCV](http://opencv.org/downloads.html) and building it using [cMake](https://cmake.org/download/)
  	* [This tutorial](http://blogs.wcode.org/2014/10/howto-install-build-and-use-opencv-macosx-10-10/) provides greater detail for setting up OpenCV with cMake and Xcode.

## Project Installation
To install the Hand Tracking project, complete the following steps.

1. Clone this repository: `git clone https://github.com/cmuartfab/handtrack.git`

2. Double click `HandTracker.xcodeproj` to open it in Xcode

3. In Xcode, right click on `HandTracker.xcodeproj` and select `add files to Hand Tracker`.
4. When the file window pops up, press `/` to open the folder option. Type in `usr/local/lib` and hit Go.
5. When in the usr/local/lib folder, **select all** of the *libopencv.dylib* files 
4. Before you click add:
	* Make sure `Add to targets: Hand Tracker` is selected.
	* Make sure `Added Folder: Create Groups` is selected.
5. Click Add. You should see all the `libopencv.dylib` files in the HandTracker project folder. 
6. In Xcode, click on `HandTracker.xcodeproj` to open the build settings.
7. Under *targets* on the left column, select HandTracker.
8. Make sure `Library Search Paths` points to where OpenCV is installed on your machine.
	* If you used Homebrew, it should be in `usr/local/Cellar`

## Running the Project
* With Xcode open, on the top toolbar go to `Xcode->preferences->Text Editing`. Check `Show Line Numbers`.
* In `main.cpp`, change lines 13 and 14 to the following to run training:
	
```c++
bool TRAIN_MODEL = 1;
bool TEST_MODEL  = 0;
```

* In `main.cpp`, change line 36 with the absolute file path to the Hand Tracker project folder.
	
```c++
string root = "ABSOLUTE PATH TO PROJECT FOLDER"; 
```

* Click Run to run the training model. When completed you should see .xml files in `models/` and `globfeat/`
* In `main.cpp`, change lines 13 and 14 to the following to run testing:
	
```c++
bool TRAIN_MODEL = 0;
bool TEST_MODEL  = 1;
```

* Click Run to run the testing model. This should open your laptop's webcam and shade your hands with a deep purple color in real time. 
