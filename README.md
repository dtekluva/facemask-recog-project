FaceMask-Detection-using-Deeplearning

A CNN based Image Classification model to classify people with and without masks. A pilot project of Face mask detection. During the times of COVID-19, covering our face with a mask and maintaining social distancing is essential.
With advancements in the field of Deep Learning, now we can easily train a model and check if someone is earning a mask or not.


🗃 Dataset	📰 HaarCascade

🎉 Output: A video constantly trying to detect faces and nose mask

For getting real-time results, run detect_mask_video.py

🧠 How it works!!
Read input either as single image or video from webcam using OpenCV.
Detect location of faces in given frame using Face_Frontal_Default Cascade Classifier

Save the list of face portions for further steps.
Load the Custom-trained CNN model, iterate each face through the model to predict mask on face.

DNN Face Detector in OpenCV

It is a Caffe model which is based on the Single Shot-Multibox Detector (SSD) and uses ResNet-10 architecture as its backbone. It was introduced post OpenCV 3.3 in its deep neural network module. There is also a quantized Tensorflow version that can be used but we will use the Caffe Model.

Post-process the frame ie; Tagging Face, with respective predictions.

🔧Setup
You can setup this project using either of the methods mentioned below.

👉 Method 1: Setup (pip)
Clone the project to your local system
Navigate inside the project directory on your local system inside the terminal
Install all dependencies using pip install -r requirements.txt


🏃‍♂️ How to Run

Detecting faces with mask in video

Navigate to FACE-MASK-DETECTION-MASTER
Make sure you have the correct environment active

And then run detect_mask_video.py.

Make sure you're well lit up