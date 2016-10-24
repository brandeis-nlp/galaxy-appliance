/*
 * A Groovy script that can be used to generate a docker-compose.yml
 * file needed to run all the Docker containers that make up a
 * LAPP Grid Galaxy Appliance.
 */
 
if (args.size() == 0) {
	println '''
USAGE 
    groovy YamlBuilder.groovy <repository name> module [module ...]

EXAMPLE
    groovy YamlBuilder.groovy lappsgrid masc oaqa lingpipe gate stanford
    
'''
	return
}

String appliance = args[0]
args = args[1..-1]

int port = 8000

println "version: '2'"
println "services:"
args.each {
	println "    ${it}:"
//	println "        build: $it"
	println "        image: $appliance/$it"
	println "        ports:"
	println "            - ${++port}:8080"
}

println """    galaxy:
        image: $appliance/galaxy-keith
        ports:
            - "80:80"
        volumes:
            - "./htrc_samples_norm:/samples"
        depends_on:"""
args.each {
	println "            - $it"
}
println "        links:"
args.each {
	println "            - $it"
}
	
