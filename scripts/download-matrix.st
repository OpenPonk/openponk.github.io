header := '.. list-table:: Download Matrix
   :header-rows: 1

   * - Build
     - Version
     - Linux
     - Windows
     - image only
'.

baseUrl := 'https://openponk.ccmi.fit.cvut.cz/builds'.

platforms := #('linux' 'windows' 'image').

ga := 'ga(''send'', ''event'', ''Downloads'', ''download'', ''{type}-{platform}-stable'')'.

anchor := '<a href="', baseUrl, '/openponk-{platform}-{version}.zip" onclick="', ga, '">download</a>'.

ind := '   '.
in2 := ind, '  - '.

tbl := String << [ :stream | |types|
	stream << header; lf.
	
	types := #(
		('All in One' 'all-in-one' ('outdated' 'latest'))
		('UML CD + OntoUML' 'uml' ('0.9.x' '0.9.3'))
		('BORM ORD' 'borm' ())
		('FSM' 'fsm' ())
		('Petri Nets' 'petrinets' ())
		('DEMO (WIP)' 'demo' ())
	).

	types do: [ :arr | |name type versions|
		name := arr first.
		type := arr second.
		versions := arr third.
		stream << ind.
		stream << '* - **' << name << '**'; lf.
		stream << in2.
		arr third
			ifEmpty: [
				stream << 'TBA'; lf.
				platforms do: [ :plat | 	stream << in2; lf ].
			]
			ifNotEmpty: [
				stream << versions first; lf.
				platforms do: [ :plat |
					stream << in2.
					stream << ':download-link:`' << type << ',' << versions second << ',' << plat << '`'.
					stream lf.
				]
			]
	]
].

'D:\OpenPonk\openponk.github.io\download-matrix.txt' asFileReference
	writeStreamDo: [ :stream | 
		stream << tbl ]
