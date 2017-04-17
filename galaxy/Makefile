NAME=galaxy-htrc

include ../Makefile.master

run:
	docker run -d -p 80:80 --name galaxy $(APPLIANCE)/$(NAME)
	
stop:
	docker rm -f galaxy

login:
	docker exec -it galaxy /bin/bash
