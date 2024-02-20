import time
import unittest

def floyd_warshall_recursive(graph, k, i, j):
    """
    Recursive function to calculate shortest paths using Floyd-Warshall algorithm.

    Parameters:
    - graph: The adjacency matrix representation of the graph.
    - k: Intermediate vertex
    - i, j: Source and destination vertices

    Returns:
    - Shortest path distance from i to j considering intermediate vertices up to k.
    """
    # Base case: If there are no intermediate vertices, return the direct edge weight
    if k == 0:
        return graph[i][j]

    # Recursive case: Consider two possibilities - include vertex k in the path or not
    include_k = floyd_warshall_recursive(graph, k-1, i, k) + floyd_warshall_recursive(graph, k-1, k, j)
    exclude_k = floyd_warshall_recursive(graph, k-1, i, j)

    # Choose the minimum of the two possibilities
    return min(include_k, exclude_k)

def floyd_warshall_recursive_wrapper(graph):
    """
    Wrapper function to initiate the recursive calculation for all pairs of vertices.

    Parameters:
    - graph: The adjacency matrix representation of the graph.

    Returns:
    - The resulting matrix with shortest path distances between all pairs of vertices.
    """
    num_vertices = len(graph)
    
    # Initialize result_matrix with the same dimensions as the input graph
    result_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Iterate through all pairs of vertices and calculate the shortest paths
    k = num_vertices - 1
    for i in range(num_vertices):
        for j in range(num_vertices):
            result_matrix[i][j] = floyd_warshall_recursive(graph, k, i, j)

    return result_matrix


def measure_performance(graph_function, graph, num_iterations=10):
    total_execution_time = 0
    for _ in range(num_iterations):
        start_time = time.perf_counter()
        result = graph_function(graph)
        end_time = time.perf_counter()
        total_execution_time += end_time - start_time
    average_execution_time = total_execution_time / num_iterations
    return result, average_execution_time


# Example usage
graph_example = [
    [0, 7, float('inf'), 8],
    [float('inf'), 0, 5, float('inf')],
    [float('inf'), float('inf'), 0, 2],
    [float('inf'), float('inf'), float('inf'), 0]
]

result, execution_time = measure_performance(floyd_warshall_recursive_wrapper,
                                             graph_example)
print("Result Matrix:")
print(result)
print(f"Execution Time: {execution_time:.6f} seconds")


class TestFloydWarshallRecursive(unittest.TestCase):
    def test_floyd_warshall_recursive_example(self):
        graph_example = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd_warshall_recursive_wrapper(graph_example)
        expected_result = [
            [0, 7, 12, 8],
            [float('inf'), 0, 5, 7],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(result, expected_result)


    def test_floyd_warshall_recursive_wrapper(self):
        graph_example = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd_warshall_recursive_wrapper(graph_example)
        # Add your assertions for the wrapper function here
        self.assertIsNotNone(result)
        # You can add more specific assertions based on the expected behavior

if __name__ == '__main__':
    unittest.main()