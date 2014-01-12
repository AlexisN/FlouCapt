Modules
=======
Camera
------
.. class:: Camera

	Class that allow obtain a picture since a image source (webcam or ip camera)
	
.. function:: Camera.getPicture()

	:return:  bool -- the ok value
	:return:  image -- the image
	
PictureProcessing
-----------------

.. class PictureProcessing
	
	
.. function:: PictureProcessing.detectFaces(img)

	Detect a human faces in the picture

	:param img: The picture where the human faces will be detected
	:type img: Image
	:return: rects (Rectangle) -- tab of rectangles contains humab faces
	
	
.. function:: PictureProcessing.smoothFaces(rects, img)

	Apply a blur where human faces has been detected

	:param rects: The rectangles where the human face has been detected
	:type rects: Rectangle
	:param img: The picture where the human faces will be detected
	:type img: Image
	:return: img (Image) -- Picture with a human face blurring

	
Main
----
.. function:: savePicture( img )

	Save the picture passed in parameter

    :param img: the picture who should be saved
    :type img: Image
    
.. function:: loadConfig()
	
	Load a parameters since a config file (config.cfg)
	
	**Parameters**
	  * freqPictures (*int*)


	:return: freqPictures (*int*) -- the numbers of seconds between capture photos


	
.. function:: __main__
	
	The main function.
	Start a picture processing application.
