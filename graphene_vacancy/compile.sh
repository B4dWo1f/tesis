#!/bin/sh


# compilation script

f="vacancy_magnetism"

pdflatex $f
bibtex $f
pdflatex $f

