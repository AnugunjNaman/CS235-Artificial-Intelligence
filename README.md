# CS235-Artificial-Intelligence

Submissions of all AI Assignments CS235 2020

    1. N Queens using Uniform Cost Search where cost = 1. So, it's similar to BFS
    2. N Queens using Heuristic Search where h(n) = Calculating number of attacks between Queens
    3. Genetic Algorithm for Diversity Reduction in Group
    4. Game of Sticks: Player vs Player,  Player vs AI, AI VS AI

## N Queens using UCS
 The code is self explanotary. It can be run directly python <filename>. If you want to change n value you can change at the end. Currently set ot 8
<br><br>
Uniform-Cost Search is a variant of Dijikstra’s algorithm. Here, instead of inserting all vertices into a priority queue, we insert only source, then one by one insert when needed. In every step, we check if the item is already in priority queue (using visited array). If yes, we perform decrease key, else we insert it.This variant of Dijsktra is useful for infinite graphs and those graph which are too large to represent in the memory.
  
## N Queens using Heuristic A*:
The code is self-explanotary<br><br>
A heuristic is a method that might not always find the best solution but is guaranteed to find a good solution in reasonable time. By sacrificing completeness it increases efficiency.Useful in solving tough problems which could not be solved any other way. solutions take an infinite time or very long time to compute. The classic example of heuristic search methods is the travelling salesman problem. A star algorithm is a version of it
  
## Genetic Algorithm
To run the code just input N = <your value> when asked. The marks are generated at random. Though I have set the seed to avoid different answers <br><br>
Genetic Algorithms(GAs) are adaptive heuristic search algorithms that belong to the larger part of evolutionary algorithms. Genetic algorithms are based on the ideas of natural selection and genetics. These are intelligent exploitation of random search provided with historical data to direct the search into the region of better performance in solution space. They are commonly used to generate high-quality solutions for optimization problems and search problems.
    
 ## Game of Sticks
Run the code directly. Input will be self explanatory for Player vs AI, Player vs Player. <br>
For AI VS AI just enter number of sticks.
    
 ## All the files are single source code with no additional dependencies. 
    1. Python Files:
        $$ python <filename>.py
    2. For Java Files:
        $$ javac <filename>.java
        $$ java <filename>.class
    
