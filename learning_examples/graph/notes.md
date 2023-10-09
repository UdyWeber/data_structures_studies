# Intro to Graphs
- Graphs uses Vertex or Nodes that are connected by edges or connections.
- Each Vertex can have edges with any other Vertex, you can have unlimited edges going through Vertexes
- To transverse the graph we hop through the Vertexes and the main objective is following the shortest path.
- Each edge can have its own weight, it can influence on the path you are going to follow.
- Trees are representation of a graph where the Vertexes are edged by 2 of their children.
- Linked lists are graphs that can only edged with one other Graph.

## Adjacency Matrix
- We can have a matrix of each Vertex and the other columns of the matrix will be the connections those make
- We ofter store in the connections of the matrix the weights that each connection has with its other Vertex

## Adjacency List
- We represent the Graph into a dictionary, where the key will be the Vertex and the values will be the vertexes that 
  the vertex makes edges with

## Big O
- In space complexity Adjacency Matrixes are O(|V|^2) because each Vertex it has to store the values of the Vertexes 
  that are not connected to it, and Adjacency Lists are O(|V| + |E|) because we just have to store for each Vertex, the
  Vertexes that are connected.
- Appending a new Vertex to the Adjacency Matrix is much more complex than adding it to an Adjacency List, the 
  respective complexities are O(|V|^2) and O(1), adding to the List is so simples because we just have to add a ney key
  to the dictionary with an empty list, while adding to the Matrix we have to add a new row and columns for each other 
  Vertex, having to rewrite the matrix.
- To create a new Edge between Vertexes, in the list and the matrix the operation is O(1)
- To remove an edge is O(|E|), E representing the edges with the Vertex, because we have to iterate the list of vertexes
  that connect with our, and in the matrix is O(1) just having to exchanging the 1 for 0 in our rows
- To remove and Vertex, in the list it will be O(|V| + |E|) because we have to remove the key of the Vertex and iterate 
  over the other key's values to see if there's an Edge with the vertex we are removing and remove it too, while in the 
  matrix is O(|V|^2) because we have to rewrite everything
