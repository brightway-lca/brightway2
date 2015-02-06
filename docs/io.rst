Importing and exporting
=======================

Importing data - not as easy as you would prefer
------------------------------------------------

There are some standards for life cycle inventory data, but the sad truth is that there are no really good standards, and each implementation of the standards has its own quirks. The basic strategy for importing data from other programs is the following:

First, data is extracted from the export format (ecospold 1, ecospold 2, SimaPro CSV) into a common Python format. Next a series or strategies is applied to the data to link exchanges. This is the difficult and delicate step, as it can sometimes be quite difficult to find the correct links. Finally, the cleaned and linked data is written to a new database.

The current strategies for cleaning and linking data include:

* Foo
* Bar

Ecospold1:
