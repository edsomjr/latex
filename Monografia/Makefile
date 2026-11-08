# Compila com latexmk (pdflatex + bibtex + makeindex, quantas vezes forem necessárias)
MAIN = tcc

.PHONY: all clean dist-clean

all:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

clean:
	latexmk -c $(MAIN).tex

dist-clean:
	latexmk -C $(MAIN).tex
