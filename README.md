# Speech_Music_Noise_classification_using_Spectrograms
This work, done as a part of Mid Semester Project of UW-Madison's course ECE 533: Image Processing, aims to classify Speech, Music and Noise sounds from Spectrograms. I trained a 2D CNN network on a small subset of the [MUSAN corpus](https://www.openslr.org/17/) from JHU's CLSP group

This repository contains my answer to one of the many questions posed in the mid semester project. 

speech_music_noise.nb - The Main Notebook. A detailed explanation of the steps I had taken for this question.\
CNN_training_ablations_2.nb - Contains the short ablation study done for selecting the best CNN model.\
preprocess_noise.py - Python script for preprocessing the noise files.\
preprocess_speech_music.py - Python script for preprocessing the speech and music files.

Due to Github's space constraints, I am not uploading the final model and the preproceesed data used to train the networks.

An evaluation was conducted by the teaching assistants of the course, and my submission got 23/30 sounds correct, just one short of the overall best among the students in the course.
