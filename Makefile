.ONESHELL:
SHELL = /bin/bash

.PHONY : env
env : 
	source /srv/conda/.condarc
	conda env update -f environment.yml

.PHONY : html
html :
	myst build --html

.PHONY : clean
clean : 
	rm -f audio/*
	rm -f data/*.csv
	rm -f figures/*