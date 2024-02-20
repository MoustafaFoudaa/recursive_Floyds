import time
import unittest

def floyd_warshall_recursive(graph):
    def recursive_helper(k, i, j):
        if k == 0:
            return graph[i][j]
        include_k = recursive_helper(k-1, i, k) + recursive_helper(k-1, k, j)
        exclude_k = recursive_helper(k-1, i, j)
        return min(include_k, exclude_k)

    num_vertices = len(graph)
    result_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            result_matrix[i][j] = recursive_helper(num_vertices - 1, i, j)

    return result_matrix




