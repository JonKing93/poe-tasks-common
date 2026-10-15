Installation
============

.. highlight:: none

.. admonition:: Prerequisites

    Requires `Python 3.12+`_. We also recommend `installing uv`_.


.. _Python 3.12+: https://www.python.org/downloads/

.. _installing uv: https://docs.astral.sh/uv/getting-started/installation/



``pyproject.toml``
------------------

We recommend most users install and configure the package via a ``pyproject.toml`` file.
The :doc:`configuration guide </guide/pyproject>` will walk you through this.


``pip install``
---------------

You can also install the package globally using pip::

    pip install poe-tasks-common

This can be useful for running tasks globally.
However, note that the package's tasks will not be available until registered with poe.
Refer to the `global task guide <https://poethepoet.natn.io/guides/global_tasks.html>`_
for more details.
