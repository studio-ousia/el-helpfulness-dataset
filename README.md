el-helpfulness-dataset
======================

This dataset is created for the paper *Evaluating the Helpfulness of Linked Entities to Readers*.

The paper aims to automatically detect entities that are helpful to document readers. The dataset is based on an *entity linking* dataset called [*IITB EL dataset*](http://www.cse.iitb.ac.in/soumen/doc/CSAW/Annot/).

The dataset is contained in *annotations.json*. Each annotation contains the following properties:

* *annotator*: The annotator's ID
* *label*: The annotated label that represents whether the entity is helpful to readers
* *wikipediaTitle*: The Wikipedia title of the entity
* *iitbDocName*: The file name of the document in the IITB dataset
* *iitbLength*: The entity length
* *iitbLength*: The entity offset
* *iitbUserId*: The user ID in the IITB dataset

A *label* can be one of the following:

* *Very helpful (YY)*: Converting this keyword into a link is highly helpful to readers.
* *Helpful (Y)*: Converting this keyword into a link might be helpful to some readers.
* *Rarely helpful (N)*: Converting this keyword into a link is rarely helpful to readers.
* *Not helpful (NN)*: Converting this keyword into a link is not helpful to readers.

## License

[![Creative Commons License](http://i.creativecommons.org/l/by-nc/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc/4.0/)

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).
