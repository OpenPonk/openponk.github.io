# Overall Architecture

OpenPonk is attempting to follow in some respect MVC architecture.

## Model

We assume that a model is supplied by the user, therefore we do not want to force them inherit from our magical classes.
However some basic basic interoperability is still required. Therefore we expect from every model element to implement the following interface:


::uml::
title Interface expected from all model elements
interface Model {
  announcer() : Announcer
  announcer:(anAnnouncer : Announcer)
  uuid() : Object
  uuid:(aUUID : Object)
}

note right of Model::uuid
Typically one would return (and store) an instance of UUID,
but any globally unique id (e.g. as a string) is acceptable.
end note
::end-uml::

Element represents a singular object within the model (e.g. UML class or UML generalization). Diagram then encompasses all elements applicable to the given model.

Project is abstraction on top of collection of diagrams. This is mainly for application use, however it can still be used independently. It is also aware of layout of each diagram.

## Controller

Controllers provide binding between model and visualization (or GUI). Generally each model is controlled by it's own controller, which in turn is a subclass of `OPController`. The responsibility of controller is to update model when some outside event requests it (e.g. value is changed from a form field), and in turn update the visualization (after model has changed).

For the canvas view an extra controller is expected. This controller subclasses from `OPDiagramController` and manages general operations related to the canvas -- layouting, clicking on empty space in the canvas, as well as managing the remaining controllers.


::uml::
skinparam nodesep 150

title MVC

package ImaginaryModel {
  class ContainerModel
  class ElementModel
  ContainerModel *--> "elements *" ElementModel
}

package OpenPonk::Controllers {
  class OPController
  class OPDiagramController
  class OPElementController

  OPController <|-- OPDiagramController
  OPController <|-- OPElementController
}

ContainerModel "model 1" <- OPDiagramController
ElementModel "model 1" <- OPElementController

package "Roassal (View)" {
  class RTElement
  class RTView

  RTElement "elements *" <---left--* "view 1" RTView
}

OPDiagramController --> "view (figure)" RTView
OPElementController --> "figure" RTElement
::end-uml::

::uml::

title Controllers and UI

package OpenPonk::Models {
  class OPProject
}

package OpenPonk::Controllers {
  class OPProjectController
  class OPDiagramController

  OPController <|-- OPDiagramController
}

OPProject "model 1" <- OPProjectController

package "OpenPonk::UI" {
  class OPWorkbench
  class OPEditor
  class OPCanvasModel

  OPWorkbench "workbench 1" *--> "editors *" OPEditor
  OPEditor "editor 1" --> "canvasModel 1" OPCanvasModel
}

package "Roassal (View)" {
  class RTView
}

OPProjectController "projectController 1" <-- "workbench 1" OPWorkbench
OPDiagramController "diagramController 1" <-- "editor 1" OPEditor
RTView "roassalView 1" <-left- OPCanvasModel
::end-uml::


## View (Roassal)

OpenPonk uses [Roassal2](http://www.agilevisualization.com).

Roassal project comes in multiple layers; we interact mostly only with the top one:

- Roassal
- Trachel (part of Roassal)
- Athens (part of Pharo)
- graphics library we should not care about


### Roassal

Roassal is layer for manipulation with visual aspects in high\-level manners, for example manipulating with elements and connecting them with edges.
Main behavior and drawing via Roassal is based on these Roassal parts:

- RTShapedObject (RTElement or RTEdge), which are semantic part, telling what we have and what is connected
- RTShape (RTEllipse, RTArrowedLine, etc.), which control what shapes and looks should elements and edges use
- RTView, which is where objects above take place

Most of interaction from Roassal TO application is made using events. Any object can tell (subscribe) RTAnnouncableObject (RTShapedObject and RTView) to make given action (announce) when given event occurs. For example, when mouse clicks on such object (Trachel event TRMouseClick occurs).

For complex cases it may be better to write "shapes" library on top of Roassal to cater to your specific diagramming needs, such as https://github.com/OpenPonk/uml-shapes.

### Trachel

Trachel defines how exactly should shapes look (TRShape). All these shapes are drawn on surface called canvas (TRCanvas). For controlling what part of canvas is displayed Trachel uses TRCamera, defining zoom (scale), size and position of current crop of canvas.

Trachel uses callbacks, which are somewhat similar to announcements/events, making specified action if predefined events with Trachel shapes occur (when trachel object is resized, moved or removed).
