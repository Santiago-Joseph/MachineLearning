# Get Tensorflow Setup
Windows 10 setup
Tensorfow GPU software requirements
-NVIDIA GPU drivers —CUDA 10.0 requires 418.x or higher
-CUDA Toolkit —TensorFlow supports CUDA 10.0 
-CUPTI ships with the CUDA Toolkit
-cuDNN SDK (>= 7.6)
-(Optional) TensorRT 6.0 to improve latency and throughput for inference on some models

Check your GPU
-computer management
-device manager
-display adapters

Install driver for your GPU
https://www.nvidia.com/download/index.aspx?lang=en-us

Install CDUA toolkit 10.0
https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal
version 10, local

Download cuDNN (create account to download)
https://developer.nvidia.com/cudnn
-Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.0

Create tools directory in C:\>
extract cuDNN and place cuda directory into tools directory

On your taskbar, search: Edit the system environment
-Select Environment Variables
-Under System variables select Path and Edit...
- Add these new paths:
	C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin
	C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\extras\CUPTI\libx64
	C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\include
	C:\tools\cuda\bin
	C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\libnvvp
  
The tensorflow-gpu.yml file with have some of the dependecies needed.
Move this file to User directory
  
Install Miniconda
https://docs.conda.io/en/latest/miniconda.html
Get Python 3.7 version 64bit (32bit will not work)

It is recommended by tensorflow to use a virtual Environment so we will make a conda enviroment
create & activate environment from user/"name" directory where the yml file is
Open command prompt:
C:\Users\username> conda install jupyter
C:\Users\username> conda env create -v -f tensorflow-gpu.yml
C:\Users\username> conda activate inceptionModel   (environment name could be changed from yml file)
C:\Users\username> pip install opencv-python
(tensorflow)C:\Users\username> python -m ipykernel install --user --name tensorflow --display-name "Python 3.7 (tensorflow)"
 
 If you want to test to see if tensorflow is working
(tensorflow)C:\Users\username> python
">>> import tensorflow as tf"
">>> print (tf.__version__)"
"(should get 1.15.0)"
">>> quit()"
"close command prompt"
 
#Running Project
Install Pycharm
https://www.jetbrains.com/pycharm/

open project in pycharm
use terminal in pycharm
C:\Users\username\Desktop\MachineLearning>conda activate inceptionModel
(inceptionModel) C:\Users\username\Desktop\MachineLearning>python app.py
This starts the flask server
-   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
click on the link and the website should load in a browser
The project currently does not delete user images so empty the  static/img directory each time you classify
