# OpenCL installation
Graphics processing units (GPUs) allow accelerated processing of image data, especially in three dimensions. 
[OpenCL](https://en.wikipedia.org/wiki/OpenCL) is one technology allowing to exploit GPUs for image processing.
Before we can dive into this topic, we need to install it.

## OpenCL installation in Fiji
In Fiji, there is a plugin for GPU-acclerated image processing using OpenCL: [CLIJ](https://clij.github.io/).
To install it, follow these steps:
* Download and unpack [Fiji](https://fiji.sc)
* Start Fiji and run its update using the menu `Help > Update`

![Image](install_fiji_menu.png)

* Click on "Manage update sites" and activate the _three_ updates sites "clij", "clij2" and "clijx-assistant".

![Image](installation.png)

* Click on "Close"
* Click on "Apply Changes"
* Restart Fiji

Installation was successful if you find the CLIJx-Assistant starting point button in Fijis tool bar:

![Image](installation_ok.png)

## OpenCL installation in Python
For python, there exist a couple of image processing libraries using OpenCL. We will work with 
[pyopencl](https://documen.tician.de/pyopencl/) and 
[clEsperanto](https://github.com/clEsperanto/pyclesperanto_prototype). 
You can install them into your conda environment using these commands:
```
conda install -c conda-forge pyopencl
pip install pyclesperanto-prototype
```

Afterwards, you can test it for example by executing these commands in python:
```
import pyclesperanto_prototype as cle

print("Used GPU:", cle.get_device().name)
```

Also feel free to install the [napari-pyclesperanto-assistant plugin in napari](https://clesperanto.github.io/napari_pyclesperanto_assistant/).
