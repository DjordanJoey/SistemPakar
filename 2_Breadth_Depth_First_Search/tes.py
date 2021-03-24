# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 08:00:07 2021

@author: HP
"""

#contoh skema grafik
graph = {
    'A':set(['B','C']),
    'B':set(['A','D','E']),
    'C':set(['A','F']),
    'D':set(['B']),
    'E':set(['B']),
    'F':set(['C'])
}

#funstion bfs
def bfs(visited, graph, node, destination):
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        rute = queue.pop(0)
        print(rute, end=" ")

        if rute == destination:
            break

        for branch in graph[rute]:
            if branch not in visited:
                visited.append(branch)
                queue.append(branch)
visited = []

#function dfs
def dfs(graph, start, destination):
    stack = [[start]]
    visited = set()
    
    while stack:
        #menghitung panjang tumpukan
        rute = stack.pop(-1)
        
        state = rute[-1]
        #cek apakah state = destination
        if state == destination:
            return rute
        elif state not in visited:
            for branch in graph.get(state, []):
                #memasukkan semua yang ada di variabel jalur ke rute_baru
                rute_baru = list(rute)
                rute_baru.append(branch)
                stack.append(rute_baru)
            #memberikan tag pada state yang sudah dikunjungi sebagai visited
            visited.add(state)
            
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")
dfs(graph, 'A','F')

#menjalankan dfs
print("DFS nya yaitu")
print(dfs(graph, 'A','C'))
print("------------------")
#menjalankan bfs
print("BFS nya yaitu")
bfs(visited, graph, 'A', 'C')