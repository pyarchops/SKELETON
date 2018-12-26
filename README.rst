=====================
pyArchOps/SKELETON
=====================


.. image:: https://img.shields.io/pypi/v/pyarchops_SKELETON.svg
        :target: https://pypi.python.org/pypi/pyarchops_SKELETON

.. image:: https://img.shields.io/gitlab/pipeline/gitlab-org/gitlab-ce/master.svg
        :target: https://gitlab.com/pyarchops/SKELETON/pipelines

.. image:: https://readthedocs.org/projects/SKELETON/badge/?version=latest
        :target: https://SKELETON.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pyarchops/SKELETON/shield.svg
     :target: https://pyup.io/repos/github/pyarchops/SKELETON/
          :alt: Updates


SKELETON


* Free software: MIT license
* Documentation: https://pyarchops-SKELETON.readthedocs.io.


Features
--------

* SKELETON

Usage
--------

.. code-block:: python

    import os
    import pyarchops_SKELETON

    api = Api(
        '127.0.0.1:22',
        connection='smart',
        remote_user='ubuntu',
        private_key_file=os.getenv('HOME') + '/.ssh/id_rsa',
        become=True,
        become_user='root',
        sudo=True,
        ssh_extra_args='-o StrictHostKeyChecking=no'
    )
    result = pyarchops_SKELETON.apply(api)
    print(result)

Development
-----------

Install requirements:

.. code-block:: console

    $ sudo pacman -S tmux python-virtualenv python-pip libjpeg-turbo gcc make vim git tk tcl

Git clone this repository

.. code-block:: console

    $ git clone https://github.com/pyarchops/SKELETON.git pyarchops.SKELETON
    $ cd pyarchops.SKELETON


2. See the `Makefile`, to get started simply execute:

.. code-block:: console

    $ make up


Credits
-------

* TODO

