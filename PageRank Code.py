# Import libraries
import math
import numpy as np
import pandas as pd
import operator


# Read data into pandas table
df_edges = pd.read_csv('web-Google.txt', sep="\t", header=None, skiprows=4)
df_edges.columns = ["from", "to"]

# Get all the nodes simply from distinct values from the whole table
df_nodes = pd.unique(df_edges[['from', 'to']].values.ravel('K'))
df_nodes = np.sort(df_nodes)  # sort ascending order

# Create dictionaries to store list of parents, number of outlinks, pagerank score and latest pagerank score
parent_dict = {}
outlink_num_dict = {}
pagerank_dict = {}
latest_pagerank_dict = {}

# Number of nodes and edges 
number_of_nodes = df_nodes.shape[0] # number = 875713
number_of_edges = df_edges.shape[0] # number = 5105039
initial_pagerank = 1/number_of_nodes

# Function to find parents (inlinks) for each node
def add_edge(node2, node1):
  temp = []
  temp.extend(parent_dict[node1]) # Get the current list
  temp.append(node2)              # Add the new parent
  parent_dict[node1] = temp
       
# Function to calculate pagerank for each node
def pagerank_cal(beta):
  for i in range(len(pagerank_dict)):
    temp_sum = 0
    for j in range(len(parent_dict[df_nodes[i]])):
      temp_sum += pagerank_dict[parent_dict[df_nodes[i]][j]]/outlink_num_dict[parent_dict[df_nodes[i]][j]]
    temp_sum = ((1-beta)/number_of_nodes) + beta * temp_sum
    latest_pagerank_dict[df_nodes[i]] = temp_sum

# Function to normalize pagerank (total sum of pagerank equals 1)
def pagerank_normalize():
  total_sum = sum(latest_pagerank_dict.values())
  for i in range (len(latest_pagerank_dict)):
    latest_pagerank_dict[df_nodes[i]] = latest_pagerank_dict[df_nodes[i]]/total_sum


# Fill 3 dictionaries with keys (all nodes) and empty values
for i in range(number_of_nodes):
  # empty_dict(df1[i])
  parent_dict[df_nodes[i]]=[]
  outlink_num_dict[df_nodes[i]] = 0
  pagerank_dict[df_nodes[i]] = initial_pagerank



for i in range(number_of_edges):
  # List all parents for all nodes
  add_edge(df_edges.iloc[i,0],df_edges.iloc[i,1])

  # Count outlink number for all nodes
  outlink_num_dict[df_edges.iloc[i,0]] += 1


# Iterations for PageRank Algorithm
for i in range(52):
  pagerank_cal(0.86)
  pagerank_normalize()
  pagerank_dict = latest_pagerank_dict.copy()




# Sort the pagerank by 
latest_pagerank_dict = dict(sorted(latest_pagerank_dict.items(), key=operator.itemgetter(1),reverse=True))
top10_dict = dict(list(latest_pagerank_dict.items())[0:10])

with open(r'C:\Users\manho\OneDrive\桌面\University of Adelaide\Year 2 Sem 1\Data Mining\Assignment 3\result.txt', 'w') as fi: 
  # Top 10 pagerank list 
  fi.write('top 10 having the largest PageRank')
  fi.write('\n')
  for key, value in top10_dict.items(): 
    fi.write('%s:%s\n' % (key, value))

  fi.write('\n\n\n')
  fi.write('PageRank of all nodes')
  fi.write('\n')

  # All Nodes pagerank
  for key, value in latest_pagerank_dict.items(): 
    fi.write('%s:%s\n' % (key, value))

