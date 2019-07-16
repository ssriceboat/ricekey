riceprint
=========

|shield1| |shield2| |shield3| |shield4| |shield5|

.. |shield1| image:: https://img.shields.io/github/release/ssriceboat/ricekey.svg?color=blue
   :width: 20%

.. |shield2| image:: https://img.shields.io/badge/Python-%3E=3.5-blue.svg?color=e6ac00
   :width: 20%

.. |shield3| image:: https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg
   :width: 24%

.. |shield4| image:: https://img.shields.io/github/license/ssriceboat/ricekey.svg?color=blue
   :width: 20%

.. |shield5| image:: https://img.shields.io/pypi/dm/ricekey.svg?color=blueviolet
   :width: 20%

About
=====

Author: Kevin Sacca ssriceboat@gmail.com

A simple threaded Python keypress event detector for stopping loops or other threads. Effective for safely stopping large for-loops, continuous functions, and enabling keypress directives for GUIs.

Works on Linux, macOS, Windows.

License
=======

MIT License

Copyright (c) 2019 ssriceboat

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Installation using pip
======================

.. code:: bash

    pip install ricekey

Usage:
======

After you have installed the package, check that its working by running
the module directly. This will demonstrate an example keypress kill event.

.. code:: bash

    cd /path/to/ricekey-package/src/ricekey/
    python ricekey.py

Below is an example of how you can use ricekey to stop your main thread if you need to:

.. code:: python

    from ricekey import kbcontrol
    from riceprint import ConsolePrinter, pprint, tprint, progressbar
    cp = ConsolePrinter()
    import threading
    import time

    # Start the keypress monitoring thread
    thread = threading.Thread(target=kbcontrol, args=())
    thread.start()

    # While the thread is alive, do something.
    i = 0
    while thread.isAlive():
       c = cp.palette.colors[i % 16]
       progressbar(i%100, 100, color=c, char='\u2587', lend='|', rend='|')
       time.sleep(0.01)
       i+=1

    pprint('Done! I hope you use this package!', 'dm')

