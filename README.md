# PageRank-Algorithm-by-Scratch

# Task

1. Implement the PageRank Algorithm as discussed in Section 5.1 and 5.2 (Leskovec, Rajaraman and Ullman) in JAVA, Python or C++. Your implementation should make use of the improvements regarding efficiency and the methods of dealing with dead-ends and spider traps. There are several PageRank implementations available on the web. You have to do your own implementation without using any code from other sources.

2. Run your algorithm on the Google Web Graph 2002 available at http://snap.stanford.edu/data/web-Google.html and provide a file listing the PageRank for each node. Report separately, the ordered list of the ten nodes having the largest PageRank Your approach should be efficient as possible in terms of runtime and memory requirements.

<B>Note: you are asked to implement the algorithm from scratch, without using third party implementations/ libraries.</B>

# Major Challenge

The PageRank algorithm needs to be implemented from scratch. The file contains total 875,713 nodes and 5,105,039 edges, and the program needs to run efficiently.

# Implementations

I used Python to do the implementation of PageRank Algorithm. Below are the procedures:

1) Imported basic libraries like math, numpy, pandas and operator.

2) Used a pandas table (2 columns) to store the whole dataset (skipped the first 4 lines), the first column is fromNodeId (parent/inlink) while the second column is toNodeID (child/outlink).

3) Extracted all the distinct values from above pandas table in order to get all Nodes ID and put all of them into a numpy array, and then sorted it into ascending order.

4) Created 4 empty dictionaries to store list of parents for each child, number of parent’s outlinks, pagerank score and latest pagerank score, and filled 3 dictionaries with keys (list of parents for each child, number of outlinks, pagerank score) and empty values

5) Calculated some constants of dataset, for example: number of nodes (875713), number of edges (5105039) and initial pagerank (= 1/875713)

6) Used Function (add_edges) to find all parents (inlinks) for each node – by reading rows for the fromNodeId and toNodeID in pandas table, store the list of parents into the dictionary for each node.

7) Run 52 iterations (>50 is fine)  of pagerank algorithm with lambda = 0.86 (within the range 0.8-0.9 is fine)

![image](https://user-images.githubusercontent.com/57484350/187126664-db646861-2b6e-4b38-b793-a64705f42eb7.png)

For the pagerank algorithm, because of the huge size of dataset, it is impossible to construct a transition matrix. Therefore, I used above formula to update the pargerank of each node. Therefore, I constructed dictionaries to store the parent’s list and number of parent’s outlinks, in order to look up the parent’s pagerank and parent’s outlinks.

Besides, the taxation can help us to deal with spider traps and dead ends. Therefore, the parameter (lambda in above formula) is used to multiply the summation and also add (1-lambda)/number of nodes to update the pagerank in each iteration.

8) After that, I used normalize all the pagerank score to make the total sum of pagerank score equals 1.

9) Sorted the latest pagerank dictionary by descending order and create a file to hold page rank score for all nodes and top10

# Result

![image](https://user-images.githubusercontent.com/57484350/187126979-7b3fa206-2850-4516-a1c7-3cc27dfe7dc1.png)

