User interfaces
===============

(I)Python shell
---------------

Brightway2 can be used from the interactive python shell. `IPython <http://ipython.org/>`_ is a nicer python shell that adds shortcuts, shell commands, and a lot else.

IPython notebook
----------------

`IPython notebooks <http://ipython.org/notebook.html>`_ are the probably the best way to interact with Brightway2 (the :ref:`five tutorials <five-tutorials>` are all ipython notebooks). These lab notebooks open incredible possibilities for interactive, reproducible, collaborative, and understandable science. Read more about the `praise IPython has been getting <http://ipython.org/#announcements>`_, and see `some awesome demos <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_. IPython notebooks are `not just for python <http://jupyter.org/>`_, either.

bw2-controller
--------------

``bw2-controller`` is a command line application that helps manage LCI databases and LCIA methods. Each time it is invoked, it does one action, and then exits. The following commands are available:

* *bw2-controller --help*: List the commands supported by ``bw2-controller``.
* *bw2-controller list databases*: List all LCI databases.
* *bw2-controller list methods*: List all LCIA methods.
* *bw2-controller details <name>*: Give details of database *name*.
* *bw2-controller copy <name> <newname>*: Copy database *name* to *newname*.
* *bw2-controller backup <name>*: Backup database *name*.
* *bw2-controller validate <name>*: Validate the datasets in database *name*.
* *bw2-controller versions <name>*: List the saved versions of database *name*.
* *bw2-controller revert <name> <revision>*: Revert database *name* to version *revision*.
* *bw2-controller remove <name>*: Delete database *name*.
* *bw2-controller export <name> [--include-dependencies]*: Export database <name>. Set *--include-dependencies* to include any databases linked by <name>.
* *bw2-controller setup*: Download default biosphere database and LCIA methods.
* *bw2-controller setup --data-dir=<datadir>*: Set the data directory permanently to <datadir>, and then download default biosphere database and LCIA methods.
* *bw2-controller upload_logs [COMMENT]*: Upload error logs to the Brightway2 server. Useful for helpign debug platform-specific errors.
* *bw2-controller color on*: Turn color output on.
* *bw2-controller color off*: Turn color output off. Sometimes the color library doesn't work perfectly.

bw2-browser
-----------

``bw2-browser`` is a command line application that allows you to interactively examine LCA datasets and databases. There is a `video explaining how it works <https://www.youtube.com/watch?v=Dw3s5K8OsM0>`_. After starting the activity browser by typing ``bw2-browser`` into a command shell or terminal, the following commands are available:

Basic commands:

* *?*: Print this help screen.
* *quit* or *q*: Exit the activity browser.
* *<number>*: Go to option <number>, when a list of options is present.
* *l*: List current options.
* *n*: Go to next page in paged options.
* *p*: Go to previous page in paged options.
* *p* number: Go to page number in paged options.
* *h*: List history of databases and activities viewed.
* *wh*: Write history to a text file.
* *autosave*: Toggle autosave behaviour on and off.

Working with databases:

* *ldb*: List available databases.
* *db <name>*: Go to database <name>. No quotes needed.
* *s <string>*: Search activity names in current database with <string>.

Working with activities:

* *a <id>*: Go to activity <id> in current database. Complex ids in quotes.
* *i*: Info on current activity.
* *web*: Open current activity in web browser. Must have ``bw2-web`` running.
* *r*: Choose a random activity from current database.
* *u*: List upstream activities (inputs for the current activity).
* *d*: List downstream activities (activities which consume current activity).
* *b*: List biosphere flows for the current activity.

bw2-web
-------

``bw2-web`` is a web user interface launched from the command line. To be honest, it is not great - it is OK for exploring methods and databases, and has what could be, with some work, a good LCA calculation report. However, it is convenient for some things, and will remain so until someone decides to make it better.

There isn't any specific documentation for ``bw2-web`` - just click on stuff and hope it doesn't break.
