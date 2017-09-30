!!! warning "Possibly outdated"

    This page is possibly outdates and is pending review.

#DCNavigator

<a name=""></a>![](../figures/navigator/navigator.png)

Navigator is a tree view of your project \(models\)\.

As semantics of models vary, it may be needed to explicitly
specify what kind of relations are between elements, what are elements
named, or what kind of icon should accompany it\.

To do this, simply subclass `DCNavigatorAdapter` and define your mappings\.
If you do not specify some mapping \(or do not create your adapter at all\),
the default one will be used instead `DCDefaultNavigatorAdapter`\.




##Mappings

The mapping itself is an array of mappings

`model class -> block/symbol/object`

e\.g\.

`DCFsmVertex -> #outgoing`

If the right value is block or symbol, it will be applied on actual model\.
So `#outgoing` is equivalent to \[ :vertex \| vertex outgoing \]\.
If it is some other object \(string, collection, …\), it will be returned
as specified\.



##




###`childrenMapping`

Children mapping defines what elements should be displayed as children
in the navigator\.




    DCFsmNavigatorAdapter>>childrenMapping
    	^ {
    		DCFsm -> #states. "show all states of the diagram as children"
    		DCFsmVertex -> #outgoing. "show all outgoing transitions"
    		DCFsmTransition -> #() "transition has no children"
    	}





###`displayMapping`


&nbsp;
<p class="todo">Rename it to displaySuffixMapping?</p>
Display mapping customizes the suffix of the displayed string, by default
the class name is displayed
\(so element named "Example" of class "DCDiagram" will show *Example \(DCDiagram\)*\)\.



&nbsp;



    DCFsmNavigatorAdapter>>displayMapping
    	^ {
    		DCFsm -> 'Diagram'.
    		DCFsmInitialState -> 'Initial State'.
    		DCFsmState -> [ :o | o isNormal
    			ifTrue: [ 'State' ]
    			ifFalse: [ 'Final State' ]
    		].
    		DCFsmTransition -> 'Transition'
    	}




###`iconMapping`

Icon mapping defines the icon displayed for the item\. Icon is a 16x16 `Form` instance\.
If you want to ease creation of icons, you can use [http://smalltalkhub\.com/\#\!/~peteruhnak/IconFactory](http://smalltalkhub.com/#!/~peteruhnak/IconFactory)


&nbsp;



    DCFsmNavigatorAdapter>>iconMapping
    	^ {
    		DCFsm -> DCIcons current dcFsmDiagramIcon.
    		DCFsmInitialState -> DCIcons current dcFsmInitialStateIcon.
    		DCFsmTransition -> DCIcons current dcFsmTransitionIcon.
    	}




###`actionMapping`


&nbsp;
<p class="todo">This is not yet implemented\.</p>
In the future action mapping should define the action that occures when double clicking on an element\.
Currently this is hardcoded to have no action for elements and open diagram for diagram\.



###`menuMapping`


&nbsp;
<p class="todo">This is not yet implemented\.</p>
This will control menu displayed on right mouse click, currently there are only basic options available like Rename, Inspect, and Delete\.



##Using same mapping for hierarchy of classes

When looking for mapping for an object, it's class hierarchy is used starting from the most generic one and stopping on the first match\.

So for hierarchy


&nbsp;



    DCNamedElement
     |
     |- DCFsmVertex
         |
    	 |- DCFsmInitialState
    	 |- DCFsmState


you can specify the mapping for any class in the hierarchy\.

**Note:** if you use class too far up in the hierarchy, like `DCNamedElement` you will also need a way to tell that your particular mapping is
only for your specific model, e\.g\. any subclass of `DCNamedElement`, but only if the object is part of `FSM` plugin\.

To do so, override method `hasMappingFor:`


&nbsp;



    DCFsmNavigatorAdapter>>hasMappingFor: anObject
    	^ anObject className beginsWith: 'DCFsm' "define whatever rule you want as long as it returns boolean"
