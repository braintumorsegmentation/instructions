# Docker BRATS

Version: 0.1

Author: Christoph Berger, TU Munich

**This is a version of the introductory text that can be found here: https://www.med.upenn.edu/sbia/brats2017/algorithms.html**

## Introduction

**In a nutshell:** We would like to have your algorithms in a Docker container, as well as in their original source code. We intend to run your dockerized algorithm on the BraTS 2016 test dataset to compare segmentation results as part of the BraTS'14-'16 journal manuscript, and to make all contributed Docker containers available through the upcoming BraTS algorithmic repository. Your source code will not be distributed and will only be used internally by the BraTS organizers, as a proof of code ownership (contact us if you cannot share your source code).

Your algorithm should be able to generate a tumor segmentation on any multimodal brain scan that is preprocessed like a BraTS test subject. To allow for fair comparisons and assessing performance differences across algorithms, you are expected to indicate what training set you have used, during training and/or design of your algorithm, and in the case of private datasets then a description of those datasets.

## Docker containers

To ensure maximum compatibility and distributability, we want to use a container approach with Docker. We therefore want you to put your runnable code in a Docker container in accordance with the requirements listed below.

In most cases, containerization of your code is a simple and straightforward procedure. We will provide an example container with functional code soon. Furthermore, many containers are available on the internet to be used as a basis, probably including your favourite programming environment and neuroimaging tools.

### Containerization

The concept of containerization is to simplify the deployment of applications. Docker is a technique to do so and will be used for the MICCAI BRATS challenge.

Docker can be used to “wrap” your entire segmentation method (including all dependencies and the operating system) into a single container. This container can be run as if it would be a single standalone application, anywhere, on any platform. Because your method and all dependencies are included in the container, the method is guaranteed to run exactly the same all the time.

This is a very popular concept and has been used successfully in previous MICCAI challenges. Docker Hub provides a large overview of existing Docker containers (base images), that can be used to build your own container. Furthermore, many popular programming environments and image analysis methods have Dockerfiles available.

### Data access

All test sets will be identical to the 2016 or 2017 test data that you have already processed. They are co-registered, skull-stripped, resampled to 1mm^3 isotropic resolution, and aligned to the SRI space. Data will be in NIfTI GZIP Compressed Tar Archive (.nii.gz) format, with all header information except the spatial resolution removed, and the individual volumes will be named ‘fla.nii.gz’, ‘t1c.nii.gz’, ‘t1.nii.gz’, ‘t2.nii.gz’. You can use any of the BRATS training or testing image volumes to check whether your Docker image runs as expected.

Because your container runs in an isolated environment, the data needs to be mapped into the container. The input data files, i.e., the ‘fla.nii.gz’, ‘t1c.nii.gz’, ‘t1.nii.gz’, ‘t2.nii.gz’ volumes, will be linked to /data and your segmentations must be placed in /data/results. Results should be a NIfTI file with the same resolution as the input data. Please call the resulting file "tumor\_'your_image'\_class.nii.gz", where ‘your\_image’ is an eight digit identifier of your algorithm. If your algorithm returns probabilities as well, you can return them accordingly, and name them, e.g., "tumor\_'your_image'\_prob_4.nii.gz" for results of class 4. If your algorithm returns tissue classes, please use “tissue\_’your_name’\_wm.nii.gz” for white matter (\*'\_gm.nii.gz' and ''\*\_csf.nii.gz' for the other two).

There should be no interaction with the container required other than running the Docker command below.

### Computing environment & Resources

We will run your container on a selection on test cases. Docker can set resource limits on containers. Please give us an indication how many CPUs and how much RAM is needed for you method, and what the resulting computation time will be.

### GPU computation

In our first instalment, we would like to run all code CPU-only to retain compatibility. Docker does not yet support GPU mapping on all platforms, so please provide a CPU-only version of you code. If you really want/need to use a GPU, please contact us.

### Examples

To help you containerize your segmentation method with Docker, we have provided some examples. Some exemplary Dockerfiles can be found on Github: https://github.com/njarng

### Assistance

If you are unsure whether your method can be containerized or how to proceed, please contact us in advance. We will try to help you with Docker.  
We have created a PDF-Document containing the exact specifications which you can download here: https://github.com/njarng/docker_brats/raw/master/BRATS_Docker_Interface.pdf

### What we need from you
+ Your version of the Docker run command below with the name of your container and the script call
+ Your requirements as far as resource usage is concerned
+ Additional notes regarding functionality
+ Links to Docker Hub or another platform where the image is available

### Docker commands

Your container will be run with the following commands:
~~~~
docker run −v <directory>:/data −it <your image> <your script call>
~~~~
"directory" will be our test directory containing the four modalities and the empty folder for your results.  
"your image" is the name of your Docker image.  
"your script call" is the script that should be called when running the container.


## Notes regarding this repository

### Purpose
This repository should provide some files and documents to aid in the containerization of BRATS methods.

It also contains a script to run an arbitrary number of BRATS Docker containers on a set of patient volumes, but this script is not yet functional and is only provided for informational purposes.

### Info
This code is not yet functional. Please contact me in case of questions.

### Additional documents
This repository also contains the Docker interface definition (PDF) for Docker containers taking part in the MICCAI BRATS competition and a website markdown explaining the details for the participants.

**Please contact me in case of any questions or if you have remarks regarding the documents provided.**
