from collections import defaultdict

def build_graph():
    graph = defaultdict(lambda: {'letter': '', 'neighbors': []})
    
    # nodes 
    nodes = {
        0: 'p', 1: 'o', 2: 'p',
        3: 'c', 4: 'o', 5: 'r',
        6: 'n', 7: 'k', 8: 'm'
    }
    for node_id, letter in nodes.items():
        graph[node_id]['letter'] = letter
    
    # edges (undirected connections)
    edges = [
        (0, 1), (1, 2), (2 , 3) ,(3, 4), (3, 7), (4, 5), (4, 7), (4, 8),
         (5, 6)
    ]
    for a, b in edges:
        graph[a]['neighbors'].append(b)
        graph[b]['neighbors'].append(a)
    
    return graph
def find_words(graph, is_word):
    found_words = set()
    
    def dfs(node, visited_edges, current_word):
        current_word += graph[node]['letter']
        
        # Check if the current string is a valid word
        if is_word(current_word):
            found_words.add(current_word)
        
        # Explore all neighbors
        for neighbor in graph[node]['neighbors']:
            edge = frozenset({node, neighbor})  # Represent edges uniquely
            if edge not in visited_edges:
                new_visited = set(visited_edges)
                new_visited.add(edge)
                dfs(neighbor, new_visited, current_word)
    
    # Start DFS from every node
    for start_node in graph:
        dfs(start_node, set(), "")
    
    return sorted(found_words)  # Return alphabetically ordered list
    
# is_word function to check if a string is a valid word
def is_word(word):
    valid_words = {'pop', 'rom', 'corn', 'popcorn', 'rock', 'mock', 'ok'}
    return word in valid_words

#find words
graph = build_graph()
result = find_words(graph, is_word)
print(result) 