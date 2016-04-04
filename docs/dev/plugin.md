# Creating new plugin

## Plugin definition class

To provide basic description for your plugin subclass `DCPlugin` and provide basic information.


    "Name of the plugin"
    MyCustomPlugin>>name
    	^ 'My Custom Plugin'
    
    "Toplevel class of the diagram"
    MyCustomPlugin>>modelClass
    	^ MCPDiagram
    
    "Controller for the diagramClass"
    MyCustomPlugin>>diagramControllerClass
    	^ MCPDiagramController
    
    "Icon, 16x16 Form instance"
    MyCustomPlugin>>icon
    	^ Smalltalk ui icons databaseIcon

	"Class responsible for serializing the model and diagram to text format"
	MyCustomPlugin>>serializerClass
		^ DCNullSerializer
