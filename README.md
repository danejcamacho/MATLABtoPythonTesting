# Matlab to Python code validation
This repository is a basic version of code validation between matlab code and python code. To run the tests use `python3 pythonFunctions.py` and 
run the matlabFunctions script in matlab or on the matlab VSCode extention

Then, run `python3 validity_tests.py` to see whether or not they are valid

## About

This repository was created to submit to an internship offer at Sandia National Labs. The matlab code was generated by AI tools and manually transcribed
to python by me. Tests were also written manually

Given more time and resources, my next steps to improve on this process would be: 
  1. create the tests using the python unittest module
  2. leverage python json module instead of using text files for a more universal testing environment
  3. write a script to run the matlab code and python code before running the tests to expedite proces