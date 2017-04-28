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
// htrc tools and data set should live inside the main galaxy container
args.removeElement("htrc")

int port = 8000
/***
println "docker network create -d overlay --subnet 192.168.0.0/16 appliance-network"
args.each {
	println "docker service create --name $it -p ${++port}:8080/tcp --network appliance-network lappsgrid/$it"
}
println "docker service create --name galaxy -p 80:80/tcp --network appliance-network lappsgrid/galaxy-keith"

return
*/

println "version: '2'"
println "services:"
args.each {
	println "    ${it}:"
	println "        build: ./$it"
	println "        image: $appliance/$it"
	println "        container_name: $it"
	println "        ports:"
	println "            - ${++port}:8080"
}

println """    galaxy:
        image: $appliance/galaxy-htrc
        container_name: galaxy
        build: ./build
        ports:
            - 80:80
        depends_on:"""

args.each {
	println "            - $it"
}
println "        links:"
args.each {
	println "            - $it"
}
	
