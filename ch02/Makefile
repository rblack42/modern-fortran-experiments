all: tsunami

tsunami:	main.o
	gfortran -o $@ $^

main.o:	main.f90
	gfortran -c -o $@ $^

.PHONY: run
run:	tsunami	
	./tsunami > tsunami_output.txt

.PHONY: view
view:	tsunami_output.txt
		python plot_height_multipanel.py tsunami_output.txt

