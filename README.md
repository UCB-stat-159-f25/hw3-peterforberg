[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wOo27OxG)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-peterforberg/HEAD?urlpath=%2Fdoc%2Ftree%2FLOSC_Event_tutorial.ipynb)

_This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Fall 2025 installment of UC Berkeley's Stat 159/259 course,_ Reproducible and Collaborative Data Science](https://ucb-stat-159-f25.github.io/site/). _Authorship of the original analysis code rests with the LIGO collaboration._

## How to use this repository
### The notebook
This repository can be launched in JupyterHub using the Binder badge above. You will automatically be directed to the main notebook, which can be run all the way through to produce a series of visualizations related to the discovery of gravitational waves. However, to demonstrate various aspects of reproducibility, there are a few more features to this repository:

### `ligotools`
Many of the functions originally written by the Ligo Scientific Collaboration (LSC) have been turned into a package, named `ligotools`. This package will be automatically installed the first time that the main notebook is run.

For each of the package modules, there are unit tests. They can be run from a terminal with the command `pytest ligotools`. `pytest` has been added to the `environment.yml`.

### The Makefile
In the home directory of the JupyterHub, you can create a terminal and run commands using the Makefile.
* Running `make env` will install a `ligo` environment and build the `IPython - LIGO` kernel, which will come with `ligotools` installed. You can swap to this kernel in the main notebook. _Note: It can take a minute for JupyterHub to recognize the kernel._
* Running `make clean` will delete all outputs from the main notebook.
* Running `make html` will create a local MyST webpage; however, this is not actually accessible on the JupyterHub. This command is for demonstration purposes only. `mystmd` has been added to the `environment.yml`.

### MyST
There is a website version of this repository available here: https://ucb-stat-159-f25.github.io/hw3-peterforberg/




