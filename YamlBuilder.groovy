/*
 * A Groovy script that can be used to generate a docker-compose.yml
 * file needed to run all the Docker containers that make up a
 * LAPP Grid Galaxy Appliance.
 */
@Grab('commons-cli:commons-cli:1.2')

CliBuilder cli = new CliBuilder()
cli.usage = 'groovy YamlBuilder.groovy [-e path] <repository> module [module ...]'
cli.header = '\nGenerates the docker-compose.yml file for a Galaxy appliance.\n'
cli.footer = '\nCopyright 2017 The Language Applications Grid.\n'
cli.h(longOpt:'help', 'displays this help message')
cli.e(longOpt:'export', args:1, 'define the directory to mount as the /export volume for Galaxy')

def params = cli.parse(args) 
if (args.size() == 0 || params.h) {
	cli.usage()
	return
}

String appliance = params.arguments()[0]
args = params.arguments()[1..-1]
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
        privileged: true"""
        if (params.e) {
        	println "        volumes:"
        	println "            - ${params.e}:/export/"
        }
println """        ports:
            - 80:80
        depends_on:"""
args.each {
	println "            - $it"
}
println "        links:"
args.each {
	println "            - $it"
}
	
