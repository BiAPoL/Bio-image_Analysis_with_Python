[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed by Anna Poetsch, [Biotec Dresden](https://tu-dresden.de/cmcb/biotec/forschungsgruppen/poetsch) and Robert Haase, [PoL Dresden](http://physics-of-life.tu-dresden.de/bia) under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

# Bio-image analysis, biostatistics, programming and machine learning for computational biology
This repository contains training resources for Python beginners who want to dive into image processing with Python. 
It specifically aims for students and scientists working with microscopy images in the life sciences.
We start with Python basics, image processing, dive into descriptive statistics for working with measurements and [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/) for plotting results.
Furthermore, we will process data and images with [numpy](https://numpy.org), [scipy](https://www.scipy.org/), [scikit-image](https://scikit-image.org/) and [clEsperanto](https://github.com/clEsperanto/pyclesperanto_prototype).
We will explore [napari](https://napari.org) for interactive image data analysis and [scikit-learn](https://scikit-learn.org/) and [apoc](https://github.com/haesleinhuepf/apoc) for processing image using machine learning.

The material will develop between April and July 2023. The materials from former years are linked below.

## How to use this material
You can browse the material online for taking a quick look.
If you want to do the exercises, it is recommended to download the whole repository, e.g. by hitting the `code` button in the top right corner and clicking on download.
Unzip the downloaded zip-file and navigate inside the sub folders, e.g. using the command prompt. 
In order to execute code and do the exercises, you need to install conda, which will be explained in the first lesson.

<img src="images/download.png" width="200"/>

This course explains everything in very detail. 
Every lesson ends with an exercise and it is recommended to do it before moving on to the next lesson. 
If you have Python basics knowledge already, test yourself by doing these exercises before starting with an advanced lesson.

## Contents

* Introduction + Python Programming I (2023-Apr-04)
  * [Introduction to bio-image analysis, programming, bio-statistics and machine learning (slides)](01_introduction_python_programming/Introduction_QBIA.pdf)
  * [Setting up your computer with mambaforge](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html)
  * [Our first jupyter notebook](01_introduction_python_programming/01_our_first_juptyer_notebook.ipynb)
  * [Math in Python](01_introduction_python_programming/02_Math_in_python.ipynb)
  * [Basic types in Python](01_introduction_python_programming/03_Basic_types.ipynb)
  * [Don't try this at home](01_introduction_python_programming/04_Dont_try_this_at_home.ipynb)
  * [Lists and tuples](01_introduction_python_programming/05_lists_tuples.ipynb)
  * [Cropping lists](01_introduction_python_programming/05a_cropping_lists.ipynb)
  * [Sorting lists](01_introduction_python_programming/05b_sorting_lists.ipynb)
  * [Dictionaries and tables](01_introduction_python_programming/06_Dictionaries_and_tables.ipynb)

* Python programming II (2023-Apr-11)
* Image Processing (2023-Apr-18)
* Image Segmentation + Quality Assurance (2023-Apr-25)
* Feature extraction (2023-May-2)
* Introduction to Biostatistics (2023-May-9)
* Descriptive Statistics (2023-May-16)
* Hypothesis Testing (2023-May-23)
* Introduction to Machine Learning + Random Forest Classifiers  (2023-Jun-6)
* Unsupervised Machine Learning  (2023-Jun-13)
* Supervised Machine Learning / Deep Learning (2023-Jun-20)
* Introduction to Genomic Data (2023-Jun-27)
* Multimodal Machine Learning (2023-Jul-4)
* Summary, exam preparation (2023-Jul-11)

## See also

### Former & future lecture materials
* [Bio-image Analysis, programming, bio-statistics and machine learning 2022](https://github.com/BiAPoL/Bio-image_Analysis_with_Python/tree/035bb75d90444f14ef21876bf3fdf9e53417f87b)
* [Bio-image Analysis, programming, bio-statistics and machine learning 2021](https://github.com/BiAPoL/Bio-image_Analysis_with_Python/tree/a62070dee408814cee4258758f5187f135774519)
* [Bio-image Analysis, programming, bio-statistics and machine learning 2020](https://git.mpi-cbg.de/rhaase/lecture_applied_bioimage_analysis_2020)
* [Bio-image Analysis, ImageJ Macro programming 2019](https://git.mpi-cbg.de/rhaase/lecture_applied_bioimage_analysis)
* [Bio-image Analysis Notebooks](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/)

### Image Analysis
* [Introduction to Bioimage Analysis](https://bioimagebook.github.io/)
* [Basics of Image Processing and Analysis by Kota Miura](https://github.com/miura/ij_textbook1/raw/76b51338e1f006c580b6f0f5cfc48fe02fba38d7/CMCIBasicCourse201102Bib.pdf)
* [Classic ImageJ training resources](https://imagej.nih.gov/ij/docs/examples/index.html)
* [Bioimage Data Analysis Workflows edited by Kota Miura and Nataša Sladoje](https://link.springer.com/book/10.1007%2F978-3-030-22386-1)

### Python
* [Python cheat sheet](https://github.com/gto76/python-cheatsheet)
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
