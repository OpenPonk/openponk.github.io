# OpenPonk (formerly DynaCASE)

[![Build Status](https://travis-ci.org/OpenPonk/openponk.svg?branch=master)](https://travis-ci.org/OpenPonk/openponk) ![](license.svg)

OpenPonk (formerly known as DynaCASE) is a metamodeling platform and a modeling workbench implemented in the dynamic environment [Pharo](https://pharo.org) aimed at supporting activities surrounding software and business engineering such as modeling, execution, simulation, source code generation, etc.

Showcase video for [ESUG 2016 conference](http://esug.org/wiki/pier/About)

<iframe width="560" height="315" src="https://www.youtube.com/embed/_gQgXdJyr-0" frameborder="0" allowfullscreen></iframe>

## Download

You can download preinstalled Pharo image containing all currently supported notations:

* FSM - Finite State Machines
* BORM ORD — [Business Objects Relation Modeling](http://ccmi.fit.cvut.cz/methodologies/borm/) Object-Relation Diagrams
* DEMO (early alpha) — [Design & Engineering Methodology for Organizations](http://ccmi.fit.cvut.cz/methodologies/demo/)
* UML Class Diagrams

Keep in mind that OpenPonk is still in early development and contains many bugs and missing features.

We are also performing a major overhaul of many parts (such as working on a full UML 2.5 metamodel, creating user documentation, and more) and we plan to do a release in late summer 2017.

[//]: # (http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-image-latest.zip)

*Alpha* is a semi-stable version, but possibly outdated compared to bleeding edge.

| Build | Linux <i class="fa fa-linux"></i> | Mac <i class="fa fa-apple"></i> | Windows <i class="fa fa-windows"></i> | image only <i class="fa fa-code"></i> |
| -- | -- | -- | -- | -- |
| **all-in-one (alpha)** | <a href="http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-linux-latest.zip" onclick="ga('send', 'event', 'Downloads', 'download', 'linux-latest')">download</a> | <a href="http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-mac-latest.zip" onclick="ga('send', 'event', 'Downloads', 'download', 'mac-latest')">download</a> | <a href="http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-win-latest.zip" onclick="ga('send', 'event', 'Downloads', 'download', 'win-latest')">download</a> | <a href="http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-image-latest.zip" onclick="ga('send', 'event', 'Downloads', 'download', 'image-latest')">download</a> |

*Bleeding edge* is the very latest version that passed CI, but is still possibly broken.

| Build | Linux <i class="fa fa-linux"></i> | Mac <i class="fa fa-apple"></i> | Windows <i class="fa fa-windows"></i> | image only <i class="fa fa-code"></i> |
| -- | -- | -- | -- | -- |
| **all-in-one (bleeding edge)** | <a href="http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-linux-bleedingEdge.zip" onclick="ga('send', 'event', 'Downloads', 'download', 'linux-bleedingEdge')">download</a> | <a href="http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-mac-bleedingEdge.zip" onclick="ga('send', 'event', 'Downloads', 'download', 'mac-bleedingEdge')">download</a> | <a href="http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-win-bleedingEdge.zip" onclick="ga('send', 'event', 'Downloads', 'download', 'win-bleedingEdge')">download</a> | <a href="http://openponk.ccmi.fit.cvut.cz/builds/all-in-one/openponk-image-bleedingEdge.zip" onclick="ga('send', 'event', 'Downloads', 'download', 'image-bleedingEdge')">download</a> |



## Direct installation

If you are an experienced Pharo user and you want to download OpenPonk directly into your image, you can do so by executing the following code:

```smalltalk
Metacello new
	baseline: 'OpenPonk';
	repository: 'github://openponk/openponk/repository';
	load: 'complete'.
```

## Opening

The downloaded package contains `README.md` with additional instructions, however on properly configured system launching `openponk.sh` (under Linux & Mac) or `OpenPonk.exe` (under Windows) should be sufficient.

*@todo: in-image guide*

## Requirements

Under Windows and Mac it should work out of the box.

**Linux may require extra configuration** as Pharo VM is currently only 32bit. Please refer to Pharo's [official guide](http://pharo.org/gnu-linux-installation).

Additionally you will require 32bit `cairo2` library, usually available in distribution package managers as `libcairo2:i386` (debian), `libcairo2`, etc.

The bundled launcher will check those requirements and will warn you and provide some tips if your system is not configured properly.
