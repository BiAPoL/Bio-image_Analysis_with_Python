(machine_learning:pixel_classification)=
# Interactive pixel classification and object segmentation in Napari

In this exercise we will train a [Random Forest Classifier](https://en.wikipedia.org/wiki/Random_forest) for pixel classification and convert the result in an instance segmentation.
We will use the napari plugin [napari-accelerated-pixel-and-object-classification](https://www.napari-hub.org/plugins/napari-accelerated-pixel-and-object-classification).

## Getting started

Open a terminal window and activate your conda environment:

```
conda activate devbio-napari-env
```

Afterwards, start up Napari:

```
napari
```

Load the "Blobs" example dataset from the menu `File > Open Sample > clEsperanto > Blobs (from ImageJ)`

![](apoc1.png)

## Pixel classification and Object Segmentation in Napari

For segmenting objects, we can use the Object Segmentation tool in APOC. 
Under the hood it uses a pixel classifier and [connected component labeling](https://en.wikipedia.org/wiki/Connected-component_labeling). 
The following procedure is also shown in [this video](apoc_object_segmentation.mp4).

Start the object segmentation from the `Tools > Segmentation / Labeling > Object Segmentation (APOC)` menu.

![](apoc2.png)

Add a new labels layer by clicking on this button:
![](apoc3.png)

Change the brush size to a small number such as 2 or 3.
![](apoc4.png)

Click on the `Paint brush` button.
![](apoc5.png)

Start annotating the `background` region where there is no object.
![](apoc6.png)

Increase the label that is drawn by one.
![](apoc7.png)

Draw an annotation within the objects of interest. Draw background and object annotation close by each other. The closer these two annotations are drawn, the smaller is the degree of freedom the computer has when optimizing the model later.
![](apoc8.png)

Within the `Object segmentation` user interface on the right, select the image/channel that should be processed.
![](apoc9.png)

Also select the annotation label image you have just drawn.
![](apoc10.png)

Click on `Train`. A label image should show up.
![](apoc11.png)

If the segmentation works well, consider backing up the `ObjectSegmenter.cl` file that has been saved. 
If you didn't change the file location before training, it will be located in the folder from where you started napari on the command line.
