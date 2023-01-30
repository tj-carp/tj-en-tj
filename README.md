# RailNL
RailNL is a case for the course Algorithms and Heuristics. The case is centered around making a planning of train trajectories in the Netherlands. We've been given a set of coordinates of all the train stations in NL, as well as a list of which stations have a connection with eachother. With this wwe have received the objective to try and make an efficient railmap where all stations are connected with eachother, and the trains ride in a trajectory which is well planned. 

To evaluate our performance a objective function is given. 

### K = P * 10.000 - (T * 100 + Min)

where: 
K = Total score of a particular solution
P = (used connections / total connections)
T = Amount of trajectories
Min = Total time driven 

To answer the main question we will not think of any solutions ourselfs. Instead we have to design algoritms which generate solutions for us. The first algorithm is designed to just produce a valid solution, randomly. but we can run it thousands of times and check which one was best. Other algorithms that we have included are a greedy algorithm. And a Hillclimber. 

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

### Structure
- **/code**: all project code
  - **/code/algorithms**: algorithms code
  - **/code/classes**: classes created for this case
  - **/code/visualisation**: code for creating a visualisation of the case
- **/data**: the data files we use for input


## Versioning
* **Python 3.8.10**

## Authors
* **Tom Zeeuwe**
* **Jaco van der Meij**
* **TJ Leeuwerik**