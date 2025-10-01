class Solution:
    def get_graph_data(self, graph):
        graph_data = {}
        for i in range(len(graph)):
            graph_data[i] = graph[i]
        return graph_data

    def bipartite(self, graph, node, visited, color_data, current_color):
        visited[node] = True
        color_data[node] = current_color
        for child in graph[node]:
            if not visited[child]:
                temp = self.bipartite(graph, child, visited, color_data, current_color ^ 1)
                if not temp:
                    return False
            else:
                if color_data[child] == color_data[node]:
                    return False

        return True

    def isBipartite(self, graph):
        graph_data = self.get_graph_data(graph)
        visited = {}
        color_data = {}
        for i in range(len(graph)):
            visited[i] = False
            color_data[i] = None

        for node in graph_data.keys():
            if not visited[node]:
                if not self.bipartite(graph_data, node, visited, color_data, 0):
                    return False
        return True
