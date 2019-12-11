===  Arkadiusz Mamala - B.S.C In software Development
===  G00349088 - Final Year Student
===  Course - Emerging Technology 
===  Project - Assessment 2019

== The project consists of the following files
  .ipynb_checkpoints (Notebook Checkpoint save)
  .AssignmentNotebook-ArkadiuszMamala-checkpoint.ipynb (The Notebook Saved)

  static (folder)

     js (folder for thne js file)
       canvas.js (js file connected to canvas.html)

     AreksModel.h5 (model for testing created in digitRecognition.py )
     digitRecognition.py (for testing purposes model with testing inside)
     drawnNUmber.png (image for testing AreksModel.h5)
     resized.png (resized image created buy the digitRecognition test)

   templates (folder)
     canvas.html (html file contains the main page of the web page)

 app.py (python file using flask to connect to the webserver and recognize digits)

 AreksModel.h5 (model created by the jupyter notebook)

 AssignmentNotebook-ArkadiuszMamala-checkpoint.ipynb (The Notebook Saved)

 drawnNumber.png (picture loded in from webserver)

 resized.png (drawnNumber resized to fit the model)

== How To Run the file?
1. Install anaconda oe update using the command -conda update --all
2. Need keras and Tensorflow installed conda install -c conda-forge keras tensorflow
3. Need other imports installed such as 
   * numpy
   * PIL
   * cv2
   * base64
4. Once all the requirements are installed next step is to clone repository 
   * clone the branch "new"
   * via command "git clone -b new https://github.com/ArekMamala/EmergingTechnologies.git"
   * or download .zip file and extract in chosen directory
5. 2 Ways of running this file
   * Pycharm 
    1. Open pycharm import project cloned/downloaded
    2. Run "app.py"
   
   * Through command Line
    1. Open command Prompt in the project directory
    2. cd into "EmergingTechnologies"
    3. use command "python app.py"
6. Step five should give you a link to go to for the application "http://127.0.0.1:5000/"
7. Copy this link into the browser of choice 
8. Using your mouse/mousepad draw a single digit 0-9
9. To clear canvas press "clearArea" to predict press button "predict"
10 . Predicted number should come up on the screen beside 

For more information on the project visit the Reasearch document in both branches 
and a video on the project itself. 





  






  

 




