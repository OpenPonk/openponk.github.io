!!! warning "Possibly outdated"

    This page is possibly outdates and is pending review.

#Palette


Palette is a UI widget providing a *palette* of tools for interaction with the canvas\.

<a name=""></a>![](../figures/palette-example.png "Finite State Machine palette")

Currently there are available three different kinds of tools\.



##Selection Tool

The purpose of selection tool is to select objects in canvas\. This tool is also selected by default and is also switched to after some other tool has completed its purposed action\.
This tool is always available and cannot be removed\.

Selecting an element will highlight this element while removing the highlight of previously selected element\. Highlight behavior of each element can be controlled via `DCController>>hideSelectionFeedback` and `DCController>>showSelectionFeedback`\.
Secondly selecting will also open editable form for this element \(if provided\)\. The form is to be specified in `DCController>>buildEditorForm:`\.

<a name=""></a>![](../figures/selection%20sequence.png "file://../figures/selection%20sequence.png")



##Creation Tool

Creation tool is used to add new elements to the canvas\. It can be added into the palette by sending `DCPalette>>newCreationTool:factory:`\. Factory should a block producing a new instance of element's DCController\.
When adding a new element one always places the element inside a target \- whether the canvas itself \(represented by DCDiagramController\) or another element \(e\.g\. putting state inside statemachine region\)\. To successfully add a new element the target must accept it, this is controlled by target's controller method `DCController>>canBeTargetFor: aController`; by default nobody accepts anything\. If the target accepts it, it must also implement method `>>addAsTargetFor: aController` since the target is providing context within the new element is being created\.

Similarly to selection highlighting, Creation Tool uses accept/deny feedback to display whether target element accepts the creation\. This behavior is provided by `DCAcceptDenyFeedbackBuilder` which at the moment displays green \(accept\) or red \(deny\) border around the target \(or changes the color of a line if the target is an edge\)\.

<a name=""></a>![](../figures/creation%20tool%20sequence.png "file://../figures/creation%20tool%20sequence.png")



##Connection Creation Tool

`DCPalette>>newConnectionCreationTool: aLabel factory: aBlock`
This is a tool for creating connections between two other existing elements\. The basis of functionality is similar to creation tool, but with two main differences\.
The first is that `DCController>>canBeTargetFor:` \(and `DCController>>addAsTargetFor:`\) is used for the second connected element, while for the specification of the first one there is `DCController>>canBeSourceFor:` \(resp\. `DCController>>addAsSourceFor:`\)\.
Secondly the new element's controller is must implement `DCRelationshipController>>connectionFeedback`\. This provides visual feedback for the newly created line before it is finalized \- essentially a connection between the source element and current mouse position\. \[\[Pkg\-OpenPonk\-Roassal2\#DCInteractiveLine\|DCInteractiveLine\]\] can be used to simplify creation of the feedback\.

<a name=""></a>![](../figures/connection%20creation%20tool%20sequence.png "An attempt to visualize ConnectionCreationTool's behavior")



##Separator

Currently there is no support for groups \- so one cannot logically group together tools\. As a temporary replacement one can add separator to provide extra horizontal spacing between tools\. `DCPalette>>newSeparator`



##Example




    aPalette
    	newCreationTool: 'element' "tool label"
    		factory: [ ElementController new ] "a descendant of DCElementController"
    		icon: Smalltalk ui icons nautilusIcon; "optional icon"
    	newSeparator; "add extra spacing"
    	newConnectionCreationTool: 'edge'
    		factory: [ TransitionController new ] "a descendant of DCRelationshipController"