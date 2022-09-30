# Modern Fortran Experiments

This project contains a number of experiments conducted on code presented in
Milan Curcic's "Modern Fortran", published by Manning Publications Co. These
experiments are being conductd to rewrite my old Fortran CFD code so it can be
updated for modern hardware. 

Since Fortran excels at number-crunching, but not at interacting with humans, I
am using Python for the front end and **matplotlib** to display graphical
results. Fortran is used where speed is required only. For this reason, most of
the Fortran code ends up in modules designed to be called by Python code. The
**numpy** **f2py** package is used to wrap the Fortran code for this purpose.

```{tableofcontents}
```
