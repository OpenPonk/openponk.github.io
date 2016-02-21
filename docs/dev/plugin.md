#Creating new plugin

<p class="todo">Work\-In\-Progress</p>


##Plugin definition file

To provide basic description for your plugin subclass `DCPlugin` and provide basic information\.


&nbsp;



    "Name of the plugin"
    MyCustomPlugin>>name
    	^ 'My Custom Plugin'
    
    "Toplevel class of the diagram"
    MyCustomPlugin>>diagramClass
    	^ MCPDiagram
    
    "Controller for the diagramClass"
    MyCustomPlugin>>diagramControllerClass
    	^ MCPDiagramController
    
    "Icon, 16x16 Form instance"
    MyCustomPlugin>>icon
    	^ Smalltalk ui icons databaseIcon




##Extending UI


&nbsp;



    MyCustomPlugin>>editorToolbarFor: aGroup
    	"extends DCEditor's toolbar"


