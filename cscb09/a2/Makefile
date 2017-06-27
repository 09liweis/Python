buxfer: buxfer.o lists.o lists.h
	gcc -Wall -Werror -g -o buxfer buxfer.o lists.o

buxfer.o: buxfer.c lists.h
	gcc -Wall -Werror -g -c buxfer.c

lists.o: lists.c lists.h
	gcc -Wall -Werror -g -c lists.c

clean: 
	rm buxfer *.o
