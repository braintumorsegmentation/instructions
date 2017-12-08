# Docker containers

To ensure maximum compatibility and distributability, we want to use a container approach with Docker. We therefore want you to put your runnable code in a Docker container in accordance with the requirements listed below.

In most cases, containerization of your code is a simple and straightforward procedure. We will provide an example container with functional code soon. Furthermore, many containers are available on the internet to be used as a basis, probably including your favourite programming environment and neuroimaging tools.

### Containerization

The concept of containerization is to simplify the deployment of applications. Docker is a technique to do so and will be used for the MICCAI BRATS challenge.

Docker can be used to “wrap” your entire segmentation method (including all dependencies and the operating system) into a single container. This container can be run as if it would be a single standalone application, anywhere, on any platform. Because your method and all dependencies are included in the container, the method is guaranteed to run exactly the same all the time.

This is a very popular concept and has been used successfully in previous MICCAI challenges. Docker Hub provides a large overview of existing Docker containers (base images), that can be used to build your own container. Furthermore, many popular programming environments and image analysis methods have Dockerfiles available.

### Data access

Because your container runs in an isolated environment, the data needs to be mapped into the container. The input data files (4 modalities: fla.nii, t1c.nii, t1.nii, t2.nii) will be mapped to /data and the result of your segmentation must be placed in /data/results.
Please call the resulting file "tumor<your_image>class.nii".
There should be no interaction with the container required other than running the Docker command below.

### Computing environment & Resources

We will run your container on a selecton on test cases. Docker can set resource limits on containers. Please give us an indication how many CPUs and how much RAM is needed for you method, and what the resulting computation time will be.

### GPU computation

In our first instalment, we would like to run all code CPU-only to retain compatibility. Docker does not yet support GPU mapping on all platforms, so please provide a CPU-only version of you code. If you really want/need to use a GPU, please contact us.

### Examples

To help you containerize your segmentation method with Docker, we have provided some examples. Some exemplary Dockerfiles can be found on Github: https://github.com/njarng

### Assistance

If you are unsure whether your method can be containerized or how to proceed, please contact us in advance. We will try to help you with Docker.

### What we need from you


### Docker commands

Your container will be run with the following commands:
~~~~
docker run −v <directory>:/data −it <your image> <your script call>
~~~~
directory will be our test directory containing the four modalities and the empty folder for your results.  
your image is the name of your Docker image.  
your script call is the script that should be called when running the container.  
