.ONESHELL:
SHELL = /bin/bash

create_environment :
	source /srv/conda/.condarc
	conda env update -f environment.yml 

.PHONY : clean
clean : 
	rm -f audio/*
	rm -f data/*
	rm -f figures/*