# PEARL Workshop

## Accessing PEARL

### On Windows
 - Download [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
 - Follow [these instructions](https://devops.ionos.com/tutorials/use-ssh-keys-with-putty-on-windows/#install-putty-and-puttygen) to setup PuTTY. Specifically the parts:
   - Install PuTTY And PuTTYgen
   - Use Existing Public And Private Keys
  
  
### On Linux

Assuming your username is `pearl008` and your key file is called `key_file.txt` you can use the following command to ssh into the PEARL system.

```bash
ssh -i key_file.txt pearl008@ui.pearl.scd.stfc.ac.uk
```

## Singularity

### Pulling Images
There are lots of places where you can get existing container images for Singularity.

 - [Singularity Container Library](https://cloud.sylabs.io/library)
 - [Docker hub](https://hub.docker.com/search?q=&type=image)
 - [NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/all)
 
Some examples of pulling images from each of these locations (can take a long time to download):

```bash
singularity pull library://library/default/centos

singularity pull docker://tensorflow/tensorflow:latest-gpu

singularity pull docker://nvcr.io/nvidia/tensorflow:20.07-tf1-py3
```

### Running Containers

```bash
singularity exec tensorflow_latest-gpu.sif python -c "import tensorflow as tf; print(tf.__version__)"
```

```bash
singularity run tensorflow_latest-gpu.sif
```

```bash
singularity shell tensorflow_latest-gpu.sif
```

### Building Containers

```
BootStrap: library
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install fortune cowsay lolcat

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%runscript fortune | cowsay | lolcat
```

```bash
singularity build --fakeroot lolcow.sif lolcow.def
```

```bash
singularity run lolcow.sif 
```
