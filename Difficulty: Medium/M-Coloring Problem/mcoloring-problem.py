class Solution:
    def graphColoring(self, v, edges, m):
        vc = {}
        def is_valid(vert, color):
            for v1,v2 in edges:
                if vert == v1 and v2 in vc and vc[v2] == color:
                    return False
                if vert == v2 and v1 in vc and vc[v1] == color:
                    return False
            return True
            
        def backTrack(vertex):
            if vertex == v:
                return True
            
            for c in range(1,m+1):
                if is_valid(vertex, c):
                    vc[vertex] = c
                    
                    if backTrack(vertex+1):
                        return True
                        
                    del vc[vertex]
                    
            return False
        return backTrack(0)