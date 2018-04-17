## Plan
2 Week iterations

### Iterations
1. First iteration, starting week of June 17, Extend API tests
2. Iteration 2: Extend API tests, starting week of July 1
3. CLI testing, starting July 15
4. ...

#### BL comments:
* I think extending the tests in mininet/test is a good idea.
* CLI testing is also a good idea.
* I also wonder if we want to have more extensive API testing.
* In the best of all possible worlds, it would be nice to measure the code coverage of our tests as well, and to try to get to the point where every API call is tested.
* It would be nice to automate all of the manual testing that we had to do for Mininet 2.0
* Also refer to my [[Mininet 2.0.0 Testing Plan and Projects]]

## Iteration 1
I want to start with testing the classes and functions of the Mininet API.
Extending what already exist in the https://github.com/mininet/mininet/tree/master/mininet/test directory with more tests testing the operations on nodes and arguments that the Mininet constructor takes.

A test's workflow would look like this. 
* Set up topology
* Validate connectivity
* Make API call, (change something)
* Validate expected connectivity

For most cases a simple topology will do but enabling the test to be done on any topo might be useful (eg. when using large topologies when testing scale)


