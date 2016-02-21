# DynaCASE

[![Build Status](https://travis-ci.org/dynacase/dynacase.svg?branch=master)](https://travis-ci.org/dynacase/dynacase) ![](license.svg)

DynaCASE is a modeling platform implemented in the dynamic environment [Pharo](https://pharo.org) aimed at supporting activities surrounding software and business engineering such as modeling, execution, simulation, source code generation, etc.

Showcase video for [ESUG 2015 conference](http://esug.org/wiki/pier/About)

<iframe width="560" height="315" src="https://www.youtube.com/embed/slIcmccsgyo" frameborder="0" allowfullscreen></iframe>

## Download

You can download preinstalled Pharo image containing all currently supported notations:

* FSM - Finite State Machines
* BORM ORD — [Business Objects Relation Modeling](http://ccmi.fit.cvut.cz/methodologies/borm/) Object-Relation Diagrams
* DEMO (early alpha) — [Design & Engineering Methodology for Organizations](http://ccmi.fit.cvut.cz/methodologies/demo/)
* UML Class Diagrams

Keep in mind that DynaCASE is still in alpha stage and contains many bugs and missing features.

[//]: # (http://dynacase.ccmi.fit.cvut.cz/builds/all-in-one/dynacase-image-latest.zip)

| Build | Linux <i class="fa fa-linux"></i> | Mac <i class="fa fa-apple"></i> | Windows <i class="fa fa-windows"></i> | image only <i class="fa fa-code"></i> |
| -- | -- | -- | -- | -- |
| **all-in-one (alpha build)** | [download](http://dynacase.ccmi.fit.cvut.cz/builds/all-in-one/dynacase-linux-latest.zip) | [download](http://dynacase.ccmi.fit.cvut.cz/builds/all-in-one/dynacase-mac-latest.zip) | [download](http://dynacase.ccmi.fit.cvut.cz/builds/all-in-one/dynacase-win-latest.zip) | [download](http://dynacase.ccmi.fit.cvut.cz/builds/all-in-one/dynacase-image-latest.zip) |

## Direct installation

If you are an experienced Pharo user and you want to download DynaCASE directly into your image, you can do so by executing the following code:

```smalltalk
Metacello new
	baseline: 'DynaCASE';
	repository: 'github://dynacase/dynacase/repository';
	load: 'complete'.
```

## Opening

The downloaded package contains `README.md` with additional instructions, however on properly configured system launching `dynacase.sh` (under Linux & Mac) or `DynaCASE.exe` (under Windows) should be sufficient.

*@todo: in-image guide*

## Requirements

Under Windows and Mac it should work out of the box.

**Linux may require extra configuration** as Pharo VM is currently only 32bit. Please refer to Pharo's [official guide](http://pharo.org/gnu-linux-installation).

Additionally you will require 32bit `cairo2` library, usually available in distribution package managers as `libcairo2:i386` (debian), `libcairo2`, etc.

The bundled launcher will check those requirements and will warn you and provide some tips if your system is not configured properly.
