!!! warning "Possibly outdated"

    This page is possibly outdates and is pending review.

#Form

To be able to edit a model through a form you need model's controller to describe what and how should be edited\.

Override `DCController>>buildEditorForm:` and describe all the elements required\. The recieved `aForm` argument is an instance of `DCDynamicForm`\.




    buildEditorForm: aForm
    	"base class automatically adds edit field for `name`"
    	super buildEditorForm: aForm.

    	(aForm addText: 'Alternative name')
    		text: self model altName;
    		whenTextIsAccepted: [ :newValue | self model altName: newValue ].


All `add*:` methods of `DCDynamicForm` return appropriate *Spec* models, so you have their full API at your disposal\.
The argument of `add*:` is a string label that will be displayed alongside the control\.

The description of available controls follows\.



##`addLabel:`
Add a single label\.

&nbsp;



    aForm addLabel: aString.

Usually not needed as all the other methods add their own label automatically\.



##`addText:`
Add a multiline text area\.

&nbsp;



    (aForm addText: aString)
    	text: aString; "set the value of the input"
    	whenTextIsAccepted: [ :newValue | ]. "observed change"




##`addTextInput:`
Add a single line text field\.

&nbsp;



    (aForm addText: aString)
    	text: aString; "set the value"
    	whenTextIsAccepted: [ :newValue | ].




##`addCheckbox:`
Add a single checkbox\.


&nbsp;



    (aForm addCheckbox: aString)
    	state: aBoolean; "set the state"
    	whenChangedDo: [ :aBool | ]. "observed change"




##`addDroplist:`
Add a droplist with specified items\.


&nbsp;



    (aForm addDroplist: aString)
    	items: #(#opt1 #opt2); "collection of options available in the droplist"
    	displayBlock: [ :item | item asString ]; "if items are complex object, specify what should be displayed"
    	setSelectedItem: oneOfTheItems; "set specific value"
    	whenSelectedItemChanged: [ :newValue | ]. "observed change"


For particularities of the models consult Spec's documentation\.