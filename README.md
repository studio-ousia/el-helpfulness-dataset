el-helpfulness-dataset
======================

This dataset is created for the paper [*Evaluating the Helpfulness of Linked Entities to Readers*](http://dl.acm.org/citation.cfm?id=2631802).

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

If you use this dataset in your research, please cite the following paper:

    @inproceedings{LINKIFY2014,
     author = {Yamada, Ikuya and Ito, Tomotaka and Usami, Shinnosuke and Takagi, Shinsuke and Takeda, Hideaki and Takefuji, Yoshiyasu},
     title = {Evaluating the Helpfulness of Linked Entities to Readers},
     booktitle = {Proceedings of the 25th ACM Conference on Hypertext and Social Media},
     location = {Santiago, Chile},
     year = {2014},
     pages = {169--178}
    }

## License

[![Creative Commons License](http://i.creativecommons.org/l/by-nc/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc/4.0/)

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).
