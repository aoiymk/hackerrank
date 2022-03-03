from bfs import bfs



def test_bfs1():
    n = 4
    m = 2
    edges = [[1, 2] ,[1,3]]
    s = 1
    expected = [6, 6, -1]
    
    result = bfs(n, m, edges, s)
    assert result == expected

def test_bfs2():
    n = 3
    m = 1
    edges = [[2,3]]
    s = 2
    expected = [-1, 6 ] 
    
    result = bfs(n, m, edges, s)
    assert result == expected

def test_bfs3():
    n = 5
    m = 3
    edges = [[1,2], [1,3] ,[3,4]]
    s = 1
    expected = [6, 6, 12, -1] 
    
    result = bfs(n, m, edges, s)
    assert result == expected