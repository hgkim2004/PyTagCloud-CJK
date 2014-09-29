=============
 PyTagCloud
=============

PyTagCloud let you create simple tag clouds inspired by `Wordle <http://www.wordle.net/>`_.

This is a fork of `the PyTagCloud-CJK <https://github.com/e9t/PyTagCloud-CJK>`_, that aims to support Korean. [1]_

Currently, the following output formats have been written and are working:

- PNG images
- HTML/CSS code

The aim of this fork is to explain how to install on CentOS6 not Ubuntu.


Requirements
============

#. Requries python >= 2.7::

Installing Python 2.7.8 on CentOS 6.5
http://bicofino.io/blog/2014/01/16/installing-python-2-dot-7-6-on-centos-6-dot-5/

#. Install `pygame <http://www.pygame.org/download.shtml>`_ >= 1.9.1::

yum install python-devel SDL_image-devel SDL_mixer-devel SDL_ttf-devel SDL-devel smpeg-devel numpy subversion portmidi-devel libpng-devel libjpeg-devel
wget http://www.pygame.org/ftp/pygame-1.9.1release.tar.gz
tar xzvf pygame-1.9.1release.tar.gz
cd pygame-1.9.1release
python setup.py build
python setup.py install

#. Install simplejson::

   $ pip install simplejson


Installation
============

Try::

    # pip install git+https://github.com/e9t/PyTagCloud.git

or::

    $ git clone git@github.com:e9t/PyTagCloud.git
    $ cd PyTagCloud
    # python setup.py install


Examples
========

- `Korean <examples/korean.py>`_::
    .. image:: examples/korean.png

- `Arabic <examples/arabic.py>`_::
    .. image:: examples/arabic.png


.. [1] A `pull request <https://github.com/atizo/PyTagCloud/pull/19>`_ has been sent to the original at Jun 11, 2014, and closed at Sep 2, 2014.
