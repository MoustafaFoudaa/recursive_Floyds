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


def measure_performance(graph_function, graph, num_iterations=10):
    total_execution_time = 0
    for _ in range(num_iterations):
        start_time = time.perf_counter()
        result = graph_function(graph)
        end_time = time.perf_counter()
        total_execution_time += end_time - start_time
    average_execution_time = total_execution_time / num_iterations
    return result, average_execution_time


# Example usage corrected
graph_example = [
    [0, 7, float('inf'), 8],
    [float('inf'), 0, 5, float('inf')],
    [float('inf'), float('inf'), 0, 2],
    [float('inf'), float('inf'), float('inf'), 0]
]

result, execution_time = measure_performance(floyd_warshall_recursive, graph_example)
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
        result = floyd_warshall_recursive(graph_example)
        expected_result = [
            [0, 7, 12, 8],
            [float('inf'), 0, 5, 7],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
