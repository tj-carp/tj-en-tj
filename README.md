# RailNL
RailNL is a case for the course Algorithms and Heuristics. The case is centered around making a planning of train route within a railmap in the Netherlands. We've been given a set of coordinates of all the train stations in Holland and NL, as well as a list of which stations have a connection with each other. With this we have received the objective to try and make an efficient railmap which adheres to the maximum of allowed routes and length in minutes, where all stations are connected with eachother, so that the trains ride well-planned routes. 

To evaluate our performance an objective function is given: 

```
K = P * 10.000 - (T * 100 + Min)
```

where

K = Total score of a particular solution

P = (used connections / total connections)

T = Amount of routes

Min = Railmap length in minutes


To answer the main question we will not think up solutions ourselves. Instead we have to design algoritms to generate solutions for us. The first algorithm is designed to just produce a valid solution, randomly. But we can run it any amount of iterations, and check which one was best. Other algorithms that we have included are a greedy as well as a hillclimber algorithm. 

## Get started!
### Requirements
All requirements can be found in the requirements.txt file. For easy installing call:
```
pip install -r requirements.txt
```

### How to use
Run an example by calling:
```
python3 main.py
```
and follow instructions for input

### Structure
- **/code**: all project code
  - **/code/algorithms**: algorithms code
  - **/code/classes**: classes created for this case
  - **/code/visualisation**: code for creating a visualisation of the case
- **/data**: the data files we use for input
- **/output**: this is where we save the output when running any or all algorithms


## Versioning
* **Python 3.8.10**

## Authors
* **Tom Zeeuwe**
* **Jaco van der Meij**
* **TJ Leeuwerik**
