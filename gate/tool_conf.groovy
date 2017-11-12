/*
 * A Groovy script used by the ToolConfEditor to update Galaxy's 
 * tool_conf.xml file with the LAPPS Grid GATE services.
 */

// A function to generate the full path to a GATE tool xml
def declare = { "gate/${it}_2.2.0.xml" }

// A list of all GATE services.
def service_list = ['tokenizer', 'splitter', 'tagger', 'ner', 'npchunker',
	'vpchunker', 'gazetteer']
	
// Populate a Map with the relative path to each service's
// XML configuration file.
def service = [:]
service_list.each { service[it] = declare it }

// Add the converter services for completeness
service.gate2json = 'converters/gate2json_2.1.0.xml'
service.json2gate = 'converters/json2gate_2.1.0.xml'

// Declare a section for all GATE tools
gate 'GATE', {
	service_list.each { name ->
		tool service[name]		
	}
	tool service.gate2json 
	tool service.json2gate
}

// Add each of the tools to the relevant other sections.
tokenizers {
	tool service.tokenizer
}

splitters {
	tool service.splitter
}

taggers {
	tool service.tagger
}

ner {
	tool service.ner
}

misc {
	tool service.gazetteer
}

chunkers {
	tool service.npchunker
	tool service.vpchunker
}

converters {
	tool service.gate2json
	tool service.json2gate
}
