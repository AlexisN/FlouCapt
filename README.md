FlouCapt
========
Development of a web software which gives a picture of the port from a webcam. Before, a blur is applied on faces and license plates to protet privacy. New pictures will be taken every 20 seconds (20 seconds is an example).

Advertisments will appear at regular intervals, at differnt locations. Clicking on this banners will redirect the user to the sponsors's websites which had contribute to thex execution of the project.

The end goal for the user is to obtain a virtual view of the port, on different screen sizes.

The application will have to be compatible with different operating systems like Windows, Linux, et Mac. It will have to be accessible from a smartphone or a tablet with this different browsers like Firefox, Chrome, Chromium, Safari and Internet explorer.




<h3>Team members </h3>

  **Project Manager :** Alexis Nicol
  
  **Communication Manager :** 
  
  **Test Manager :** Kévin Bannier
  
  **Documentation Manager :** Mathieu Thomas
  
<h3>Technologies used for the project execution</h3>
<ul>
<li>OpenSUSE</li>
<li>OpenCV</li>
<li>Python</li>
<li>Apache</li>
<li>HTML5</li>
<li>PHP</li>
<li>Jquery</li>
</ul>


<h3>Start application</h3>
 - To start PictureProcessing application, you just need to run start_PictureProcessing.sh

```sh
sh start_PictureProcessing.sh
```
- To stop PictureProcessing application, just press Ctrl+C

<h3>Documentation</h3>

To compile the documentation, run :
```sh
cd src/PictProcess/doc
make html
```

<ul>
<li>The documentation are available in HTML in src/PictProcess/doc/build/html</li>
<li>The documentation are generated with [Sphinx](http://sphinx-doc.org/)
</ul>


<h3>Output</h3>
The blurring pictures are saved in folder : <code>src/PictProcess/out/\<date\>/</code>
