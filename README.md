
# Sign Language Detection and Translation using Python & Machine Learning (Ultralytics YOLOv8, OpenCV, Pyttsx3)

This is a sign language detection and translation model built using 
[ultralytics](https://github.com/ultralytics/ultralytics)
& [OpenCV](https://github.com/opencv/opencv)

Our pre-trained model trained on custom dataset detects sign language for the 9 following labels:
<ul>
    <li>Hello</li>
    <li>I Love You</li>
    <li>Yes</li>
    <li>No</li>
    <li>Thanks</li>
    <li>Please</li>
    <li>How</li>
    <li>Name</li>
    <li>You</li>
</ul>

Based on the limited vocabulary detected, the app can construct meaningful sentences and play and audio 🔊 of the sentences constructed to the user, thereby giving voice to people with determination 💪🏻 

PS: We were complete noobs at the time of building the project. When we were looking for resources to build, we couldn't literally find ANY suitable model to train/run. Most of the sign detection models were built out of Tensorflow and brother when I tell you it didn't WORK AT ALL due to dependecies error issue 😤. Yes, TF might've worked for this project in the past, but it doesn't anymore. 

Frustrated with TF we were about to ditch the project, until we finally figured out a way to build this project. That time I told myself, if this ever works out, I'm gonna make this open source so that others don't suffer 🗿

So, here's the PyTorch file of the pretrained model. Contact me on [LinkedIn](https://linkedin.com/in/mohamed-nadhim) if you want the Jupyter Notebook file to train the model using Google Colab. Have fun 😊




### Contributors
- [T. Mohamed Nadhim]("https://github.com/nadhim")
- Mohamed Fardeen I
- Jayashree C G




## Installation

- Clone the repository

```git
    git clone https://github.com/Nadhim/Sign-Language-Detection.git
    cd Sign-Language-Detection
```

- Create a virtual environment
```git 
    python -m venv venv
```


- Install the required python packages

```git 
    pip install -r ./requirements.txt
```

## Demo
<img src="assets/demo.png" alt="demo" style="width:500px; border-radius:10px;"/>
<p></p>
<img src="assets/demo2.png" alt="demo" style="width:500px; border-radius:10px;"/>
<p></p>
<img src="assets/demo3.png" alt="demo" style="width:500px; border-radius:10px;"/>
    