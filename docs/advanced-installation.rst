.. _windows-scripts:

Scripts in the installation package
-----------------------------------

bw2-env.bat
```````````

.. code-block:: bat

    @ECHO OFF
    ECHO Setting path to Brightway2 environment
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2

bw2-update.bat
``````````````

.. code-block:: bat

    @ECHO OFF
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2
    @ECHO ON
    pip install -U --no-deps --pre brightway2 bw2io bw2data bw2calc bw2analyzer
    PAUSE

bw2-ipython.bat
```````````````

.. code-block:: bat

    @ECHO OFF
    ECHO Setting path to Brightway2 environment
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2
    CALL ipython

bw2-notebook.bat
````````````````

.. code-block:: bat

    @ECHO OFF
    ECHO Setting path to Brightway2 environment
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2
    CALL jupyter notebook

bw2-activity-browser.bat
````````````````````````

.. note:: The activity browser is still under heavy development. Use with caution!

.. code-block:: bat

    @ECHO OFF
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2
    @ECHO ON
    CALL activity-browser.exe
    PAUSE
