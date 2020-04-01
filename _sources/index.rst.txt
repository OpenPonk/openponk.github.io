OpenPonk modeling platform
==========================

.. figure:: figures/op-logo.jpg

.. figure:: figures/license.svg

OpenPonk is a metamodeling platform and a modeling workbench implemented in the dynamic environment `Pharo <https://pharo.org>`_ aimed at supporting activities surrounding software and business engineering such as modeling, execution, simulation, source code generation, etc.

Workshop Paper
--------------

`IWST'16 <http://www.esug.org/wiki/pier/Conferences/2016/International-Workshop-IWST_16>`_ Workshop paper: `openponk_iwst16.pdf <http://esug.org/data/ESUG2016/IWST/Papers/IWST_2016_paper_25.pdf>`_

Showcase
--------

Showcase video for `ESUG 2016 conference <http://esug.org/wiki/pier/About>`_

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/_gQgXdJyr-0" frameborder="0" allowfullscreen></iframe>

Download
========

You can download preinstalled builds for each supported notation.

.. include:: download-matrix.txt


* All in One -- All notations together
* UML Class Diagrams with semi-complete UML 2.5 metamodel and XMI support
* `OntoUML <https://ccmi.fit.cvut.cz/methodologies/ontouml/>`_
* BORM ORD — `Business Objects Relation Modeling <https://ccmi.fit.cvut.cz/methodologies/borm/>`_ Object-Relation Diagrams
* FSM - Finite State Machines
* Petri nets - Prototype of PT Petri nets with arc weights

Direct installation
===================

To install latest OpenPonk with all default plugins to an existing Pharo 7, 8 or 9 image, use the following snippet:

.. code-block:: smalltalk

   Metacello new
   	baseline: 'OpenPonk';
   	repository: 'github://openponk/openponk/repository';
   	load: 'complete'

Just beware that this is the master branch and might be unstable.

For downloading specific version, add the version to the repository path. For example:

.. code-block:: smalltalk

   Metacello new
   	baseline: 'OpenPonk';
   	repository: 'github://openponk/openponk:2.x/repository';
   	load: 'complete'

Opening
=======

On most systems extracting the archive and launching the executable file should be sufficient (for example openponk-class-editor.exe on Windows and openponk-class-editor on Linux).

In case of errors, make sure you have write privileges to the extracted directory.

Once launched, clicking on the desktop will show a menu containing entries for OpenPonk.

Requirements
============

* **Windows** builds: Windows 7 or higher (64bit)
* **Linux** builds: any recent 64bit distro except OpenSUSE and Fedora-like ones
* **Image-only** builds use following Pharo image versions:

	* 2.x and latest: Pharo 8 64bit
	* 0.x and 1.x: Pharo 6.1 32bit

**Versions 1.x and lower may require extra configuration on Linux**. Please refer to Pharo's `official guide <http://pharo.org/gnu-linux-installation#64-bit-System-Setup>`_. 
Additionally you will require 32bit `cairo2` library, usually available in distribution package managers as `libcairo2:i386` (debian), `libcairo2`, etc.

Contact
=======

**Bug reports and feature requests:**

To report a bug or request a feature related to implementation of specific kind of models/notations, use the related build repository. For general OpenPonk issues, use the OpenPonk core repository. If you are not sure whether is it related to the model/notation implementation or OpenPonk core itself, use the model/notation issue tracker and we will move the issue to its proper place.

.. list-table::
   :header-rows: 1
   :widths: 150 500
   :align: left
   :stub-columns: 1

   *  -  Build
      -  Issue tracker
   *  -  OpenPonk core
      -  https://github.com/OpenPonk/openponk/issues
   *  -  UML & OntoUML
      -  https://github.com/OpenPonk/class-editor/issues
   *  -  BORM
      -  https://github.com/OpenPonk/borm-editor/issues
   *  -  Petrinets
      -  https://github.com/OpenPonk/petrinets/issues
   *  -  FSM
      -  https://github.com/OpenPonk/fsm-editor/issues


**Centre For Conceptual Modeling and Implementation (CCMi):** https://ccmi.fit.cvut.cz

**Email:** openponk@gmail.com

**GitHub:** https://github.com/openponk

Sponsors
========

.. figure:: figures/elixir-cz-logo.png
   :target: https://www.elixir-czech.cz/
   
   OpenPonk is a registered Elixir CZ tool


Past Sponsors
=============

.. figure:: figures/formetis-logo.jpg
   :target: https://www.formetis.nl/

