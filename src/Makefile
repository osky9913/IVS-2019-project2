#-------------------------------------------------
#  FILE:   Makefile
#  AUTHOR: Simon Sedlacek, FIT
#  EMAIL:  xsedla1h@stud.fit.vutbr.cz
#  DATE:   19.4.2019
#  BRIEF:  Makefile with all the necessary targets for manipulating the project
#  NOTE:   IVS-2019-project2, Vychodni Nemci a Severni Madari
#-------------------------------------------------

PROJECT_FOLDER = xsedla1h_xsarva00_xsvobo1t_xosval03
INSTALLER = ../installer/nem-mad-calc-1.0
.PHONY: all clean test doc run profile prepfolder


# Main project targets
all: run 

pack: prepfolder
	cd ../../ && zip -r $(PROJECT_FOLDER).zip $(PROJECT_FOLDER)
	rm -rf ../../$(PROJECT_FOLDER)

clean:
	rm -rf __pycache__ ../__pycache__ .idea ../.idea
	rm -rf ../doc 
	rm -f pycallgraph.png
	rm -rf $(INSTALLER)*

test:
	python3 mathlibtests.py

doc:
	rm -rf ../doc
	doxygen

run:
	python3 main.py

profile:
	echo "30 1 2.3 22 3 5.7 4 42 4 144.1 32 413" | python3 profiling.py

help:
	@echo $(HELP)

# Installs necessary dependencies for the project
depend:
	sudo apt-get install python3 python3-pip python3-pyqt5

# Creates a debian installer for the program
installer:
	rm -f $(INSTALLER).deb
	mkdir -p $(INSTALLER)/opt/nem-mad-calc
	cp -r ../installer/DEBIAN $(INSTALLER)
	cp -a main.py calculator.py ui_calculator.py stack.py evaluate.py mathlibrary.py $(INSTALLER)/opt/nem-mad-calc/
	chmod +x $(INSTALLER)/DEBIAN/*
	dpkg-deb --build $(INSTALLER)
	rm -rf $(INSTALLER)


# Other targets utilised by some of the main targets
prepfolder: installer doc
	cd ../../ && rm -rf $(PROJECT_FOLDER) $(PROJECT_FOLDER).zip
	mkdir ../../$(PROJECT_FOLDER)
	cd ../../$(PROJECT_FOLDER) && mkdir repo && mkdir install && mkdir doc
	cp -a $(INSTALLER).deb ../../$(PROJECT_FOLDER)/install
	cd ../ && cp -ar doc/* ../$(PROJECT_FOLDER)/doc
	cd ../../ && cp -ar IVS-2019-project2/. $(PROJECT_FOLDER)/repo
	cd ../../$(PROJECT_FOLDER)/repo && rm -rf installer doc
	rm -rf ../doc

# Stores help text
HELP=Before launching the program, please make sure you have all the necessary dependencies installed.\
You can do so by typing in the command make depend. This command will check the dependencies and if missing,\
it will ask you for permission to install them.
