#-------------------------------------------------
#  FILE:   Makefile
#  AUTHOR: Simon Sedlacek, FIT
#  EMAIL:  xsedla1h@stud.fit.vutbr.cz
#  DATE:   19.4.2019
#  BRIEF:  Makefile with all the necessary targets for manipulating the project
#  NOTE:   IVS-2019-project2, Vychodni Nemci a Severni Madari
#-------------------------------------------------

PROJECT_FOLDER = xsedla1h_xsarva00_xsvobo1t_xosval03
.PHONY: all clean test doc run profile prepfolder


# Main project targets
all: run 

pack: clean prepfolder
	cd ../../ && zip -r $(PROJECT_FOLDER).zip $(PROJECT_FOLDER)
	rm -rf ../../$(PROJECT_FOLDER)

clean:
	rm -rf __pycache__ ../__pycache__ .idea ../.idea
	rm -rf ../doc 

test:
	python3 mathlibtests.py

doc:
	rm -rf ../doc
	doxygen

run:
	python3 main.py

profile:
	python3 profiling.py

# Other targets utilised by some of the main targets
prepfolder: doc
	cd ../../ && rm -rf $(PROJECT_FOLDER) $(PROJECT_FOLDER).zip
	mkdir ../../$(PROJECT_FOLDER)
	cd ../../$(PROJECT_FOLDER) && mkdir repo && mkdir install && mkdir doc
	cd ../ && cp -a installer/* ../$(PROJECT_FOLDER)/install
	cd ../ && cp -ar doc/* ../$(PROJECT_FOLDER)/doc
	cd ../../ && cp -ar IVS-2019-project2/. $(PROJECT_FOLDER)/repo
	cd ../../$(PROJECT_FOLDER)/repo && rm -rf installer doc
	rm -rf ../doc
