---> COMPILAZIONE
gcc -c hello.c
gcc hello.o -o hello ---> with -m32  for 32 bit ..... --static per il link statico

--> COMANDI
ldd hello --> find library
strongs hello
strings hello | wc -l --> words count (lines)
nm hello ---> lista dei simboli in un file oggetto
objdump --> fornisce molte informazioni sul file oggetto in base ai parametri)
objdump -p hello
objdump -p hello | grep NEEDED 
lsof --> mi da ala lista di file aperti al momento

--> COMANDI : STRACE e LTRACE
strace ./license1.32
strace -e trace=openat ./license1.32 --> traccia solo delle particolari chiamate (filtro)
strace -e trace=file ./license1.32 --> in particolare tracciamo le interazioni con i file
strace -e trace=process ./license1.32  --> ...
strace -e trace=network ./license1.32 --> ...
strace -f ./license1.32 --> dico a strace di mostrare l'esecuzione anche di processi figli
sudo strace -p 1234567 ./license1.32 --> traccia l'esecuzione di un processid  
ltrace ./license1.32 --> trace delle chiamate di libreria
ptrace ... è una chiamata di sistema che aiuta a tracciare i processi (noi non lo useremo)

gcc -m32 -shared mytime.c -o mytime.o --> compilo la libreria
LD_PRELOAD=./mytime.o ./ggfm --> aggiusto l'esecuzione aggiungendo la libreria (sovrascriverà i metodi di default)

#COVERAGE PYTHON
python3-coverage run coverage1.py 1
python3-coverage report -m
python3-coverage html -d coverage_html
#per combinare i dieversi risultati
mv .coverage .coverage-1
mv .coverage .coverage-2
python3-coverage combine -a .coverage-1 .coverage-2
