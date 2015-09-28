Installation on Mac OS X
************************

Installation using Miniconda
============================

1. Download the `Python 3 Miniconda installer <https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`__ to your ``Downloads`` folder.
2. Open a new Terminal window. The Terminal is ``Appplications`` > ``Utilities`` > ``Terminal.app``., and enter the following commands:

.. code-block:: bash

    cd ~/Downloads
    chmod +x Miniconda3-latest-MacOSX-x86_64.sh
    ./Miniconda3-latest-MacOSX-x86_64.sh

This will start the Miniconda installer:

.. image:: images/osx-1.png
    :align: center

Press ENTER to start reading the Miniconda license.

.. image:: images/osx-2.png
    :align: center

Press the space bar to progress through the license.

.. image:: images/osx-3.png
    :align: center

Type ``yes`` to agree to the license terms. Next, change the default installation location to ``/Users/<your user name>/bw2-python``.

3. Next,

    cd ~/bw2-python && bin/conda install -q -y conda && bin/conda update -q conda && bin/conda update -q wheel pip setuptools && bin/conda create -y -q -n bw2 anaconda python=3.4 && source bin/activate bw2 && conda install -y numpy ipython ipython-notebook jupyter scipy flask lxml requests nose docopt whoosh && pip install eight && pip install --pre --extra-index-url http://129.132.92.166:8787/simple/ --trusted-host 129.132.92.166 brightway2

4. In the same terminal window, you can enter the ipython interpreter with the command ``ipython``, or run Jupyter notebooks with ``jupyter notebook``.



https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=conda%20distutils%2010.5

https://github.com/MacPython/wiki/wiki/Spinning-wheels

Build special wheel just for Anaconda? Or Anaconda package?

http://stackoverflow.com/questions/31627515/installing-a-python-wheel-file-whl-results-in-is-not-a-supported-whee

https://www.reddit.com/r/Python/comments/1vled5/anaconda_seems_to_have_a_nicely_set_up_library/


ls /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/lib/libgc*.*

https://github.com/Homebrew/homebrew/issues/40653
