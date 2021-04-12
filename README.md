[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed by Robert Haase, [PoL Dresden](http://physics-of-life.tu-dresden.de/) under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

# Bio-image analysis, biostatistics, programming and machine learning for computational biology
This repository contains training resources for Python beginners who want to dive into image processing with Python. 
It specifically aims for students and scientists working with microscopy images in the life sciences.
We start with python basics, dive into descriptive statistics for working with measurements and [matplotlib](https://matplotlib.org/) for plotting results.
Furthermore, we will process images with [numpy](https://numpy.org), [scipy](https://www.scipy.org/), [scikit-image](https://scikit-image.org/) and [clEsperanto](https://github.com/clEsperanto/pyclesperanto_prototype).
We will explore [napari](https://napari.org) and [Fiji](https://fiji.sc) for interactive image data analysis. 
Finally, we will use [scikit-learn](https://scikit-learn.org/stable/), [CellPose](https://github.com/MouseLand/cellpose) and [StarDist](https://github.com/stardist/stardist) to process images using machine learning techniques.

The material will develop between April and July 2021. Stay tuned for the later lessons.

## How to use this material
You can browse the material online for taking a quick look.
If you want to do the exercises, it is recommended to download the whole repository, e.g. by hitting the `code` button in the top right corner and clicking on download.
Unzip the downloaded zip-file and navigate inside the sub folders, e.g. using the command prompt. 
In order to execute code and do the exercises, you need to install conda, which will be explained in the first lesson.

<img src="images/download.png" width="200"/>

This course explains everything in very detail. 
Every lesson ends with an exercise and it is recommended to do it before moving on to the next lesson. 
If you have python basics knowledge already, test yourself by doing these exercises before starting with an advanced lesson.

## Feedback and support

If you have any questions, please use the anonymous etherpad (see email) or open a thread on [image.sc](https://image.sc), put a link to the lesson or exercise you want to ask a question about and tag @haesleinhuepf.

## Contents

* Block 1 - Introduction
  * [Introduction to bio-image analysis, programming, bio-statistics and machine learning](https://cloudstore.zih.tu-dresden.de/index.php/s/2Xm4awQiQ4oYQSx)
  * [Setting up a conda environment](https://github.com/BiAPoL/Bio-image_Analysis_with_Python/blob/main/conda_basics/01_conda_environments.md)
  * [Our first jupyter notebook](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/01_our_first_juptyer_notebook.ipynb)
  * [Trailer: bio-image analysis, machine learning and bio-statistics with python](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/image_processing/00_trailer.ipynb)
* Block 2 - Data structures
  * Introduction to Python data structures
  * [Basic math in python](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/02_Math_in_python.ipynb)
  * [Pitfalls when using notebooks](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/03_Dont_try_this_at_home.ipynb)
  * [Basic types in python](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/04_Basic_types.ipynb)
  * [Arrays, lists and tuples](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/05_Arrays_lists_tuples.ipynb)
  * [Dictionaries and tables](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/06_Dictionaries_and_tables.ipynb)
* Block 3 - Algorithms
  * Introduction to Python algorithms
  * [The conditional, "if" statement](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/07_Conditions.ipynb)
  * [Loops](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/08_loops.ipynb)
  * [Functions](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/09_custom_functions.ipynb)
  * [Libraries](http://nbviewer.jupyter.org/github/BiAPoL/Bio-image_Analysis_with_Python/blob/main/python_basics/10_custom_libraries.ipynb) 
* Block 4 - Image processing
* Block 5 - Image segmentation + 3D Image Processing
* Block 6 - Quantitative measurements, Processing folders
* Block 7 - Introduction to Biostatistics
* Block 8 - Descriptive statistics
* Block 9 - Method Comparison - Bland-Altman analysis
* Block 10 - Hypothesis testing
* Block 11 - Big data and data visualization
* Block 12 - Machine learning I
* Block 13 - Machine learning II
* Block 14 - Summary

## See also
* [Python/Conda environments](https://mpicbg-scicomp.github.io/ipf_howtoguides/guides/Python_Conda_Environments)
* [Scientific data analyis in Python, Biotec lecture](https://youtu.be/MOEPe9TGBK0)
* [Python for Microscopists, video series by Sreeni](https://www.youtube.com/channel/UC34rW-HtPJulxr5wp2Xa04w)
* [Managing Conda environments, online documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [Bio-image Analysis using Scikit-Image in Python, Biotec lecture](https://youtu.be/FnvgepHDqRA)
* [Python for Bio-image Analysis by the Image Analysis Focused Interest Group of the Royal Microscopical Society](https://github.com/IAFIG-RMS/Python-for-Bioimage-Analysis)
* [Interactive Bioimage Analysis with Python and Jupyter, NEUBIAS academy webinar](https://youtu.be/2KF8vBrp3Zw), [Part 2](https://youtu.be/Y3pB3wnOivE)
* [Multi-dimensional image visualization in Python using napari, NEUBIAS Academy webinar](https://youtu.be/VgvDSq5aCDQ)

## Contributing
Contributions to this repository are welcome! If you see typos, bugs or have general feedback, please create a [github issue](https://github.com/BiA-PoL/Bio-image_Analysis_with_Python_course/issues) to let us know. 
If you would like to add additional lessons or want to suggest improvements to existing ones, [pull-requests](https://github.com/BiA-PoL/Bio-image_Analysis_with_Python_course/pulls) are very welcome!

## Acknowledgements
[Robert Haase](https://twitter.com/haesleinhuepf/) was supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany’s Excellence Strategy – EXC2068 - Cluster of Excellence Physics of Life of TU Dresden.

[Imprint](https://tu-dresden.de/impressum)
