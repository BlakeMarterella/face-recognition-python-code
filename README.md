# PyPeepHole

## Project Overview
Identify the faces of people at your door to give you an early warning of who is there.

## How to use
There are 3 main files:
<dl>
  <dt><strong>scanFromCam.py</strong></dt>
  <dd>Once the script is run, the user is prompted for their name and a unique identifier. Then, a popup window with an image preview from the webcam appears. To capture a photo of the face, click `s` or `q` to cancel the operation. A total of 5 pictures will be taken and the window will disapear automatically</dd>
  <dt><strong>scanFromFile.py</strong></dt>
  <dd>Faces are saved from files uploaded into the 'face' directory. In order to work properly, have a directory inside of faces where multiple images can be uploaded. ** Only upload png images **. The files should be uploaded as such: 'faces/name01/image01', 'faces/name01/image02', etc.</dd>
  <dt><strong>recognition.py</strong></dt>
  <dd>A popup window identifies faces in the current webcam faces. Click q to quit analyzing the video feed.</dd>
</dl>

### Utilities and Debugging Tools
#### utilites.py
erase all of the saved faces in the pickle files to test
 

## Obstacles
- Reading faces from multiple files
