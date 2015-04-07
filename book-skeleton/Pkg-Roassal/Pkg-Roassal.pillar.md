

## Pkg\-DynaCASE\-Roassal2

This package contains classes which extend the Roassal2 for DynaCASE purposes\.
Roassal2 is layer for manipulation with visual aspects in high\-level manners, for example manipulating with elements and connecting them with edges\.



###1\.  Builders

Contains classes used to prepare and create other classes and elements\.



####1\.1\.  Feedback builders

Serve for visualising whether given edge, element, view etc\. can or can not be used withing current context\.
[usage for connection creation](file://../figures/connection%20creation%20tool%20sequence.png)\.



####1\.2\.  DCRTCallbackBuilder



####1\.3\.  DCRTEdgeBuilder

Serve for creation of lines and edges used in DC



####1\.4\.  DCStarAssociationBuilder

Handler for visualisation of association between multiple elements, connected with 'star topology'\. Usable for example for generalization\.



###2\.  Core



####2\.1\.  Constraints

Constraint classes are inspired by TRConstraint classes, which serve to adapt element's properties according to other element\(s\)\.

EdgeConstraint are applicable only for positioning of an element according to properties \(mostly position\) of roassal edge\.
'Along' constraint uses relative position from center of line \(based also on lenght of line\), 'End' constraint uses distance of start or end of line\.

ElementsConstaint are applicable only for two elements\.



####2\.2\.  DCRTToSelf\(WithOffset\)AttachPoint

A DCRTToSelfAttachPoint is attachpoint for connecting an element with itself\.
Offset version: If multiple connections are made, each one has its attach point moved by offset\.



###3\.  Interactivity



####3\.1\.  DCInteractiveLine

Temporary line displayed while creating associations\. After the first element is chosen, it shows how could the line look like at the current moment\.
[usage for connection creation](file://../figures/connection%20creation%20tool%20sequence.png)



####3\.2\.  DCRTFocusable

Implementation of RTAbstractHighlightable, highlighting an element or edge when the item is clicked\. Previously selected item automatically loses focus\.



###4\.  Line Decoration

System of classes used as replacement for Roassal2 RTLineDecoration classes, which serve as line heads \(for example with arrowed line\)\.
DCRTLineHead \(and DCRTLineTail\) could be used in place of RTLineDecoration classes, acting like them\.
DCRTLineDecorationShape and its subclasses define its shape\.



###5\.  Shapes



####5\.1\.  DCRTClass

Rectangle\-shaped standard class, containing name \(and stereotype\) in upper part and attributes in lower part\.



####5\.2\.  DCRTMultiLine

Multi\-purpose line with possibility of being made from multiple parts, having head and/or tail \(like arrow\) and being styled \(dashed, dotted\.\.\.\)\.
