.ONESHELL:
SHELL = /bin/bash

.PHONY : env
env : 
	source /srv/conda/.condarc
	conda env update -f environment.yml
	conda activate ligo
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - LIGO"

.PHONY : html
html :
	myst build --html

.PHONY : clean
clean : 
	rm -f audio/*
	rm -f data/*.csv
	rm -f figures/*