from collections import defaultdict,deque
# 图的表示
# nodeMap = {node,list(nodes)},node及其邻接点
# indegree = {node,int}，node极其入度数

# 图的DFS，需要借助栈和哈希表
# 如果是无向图，邻接点会出现重复，需要hashSet去重，这里展示无向图遍历
class GraphDFS:
    def graphDfs(self,nodeMap):
        stack = [];ans=[]
        hashSet = set()
        #这里举个例子，实际情况可以以任意一点为起点，有向图，需要入度为0的作为起点
        startNode = 0 
        stack.append(startNode)
        while stack:
            root = stack.pop()
            if not root in hashSet:
                hashSet.add(root)
                ans.append(root)
            for node in nodeMap[root]:
                if not node in hashSet:
                    #可能没有遍历完邻接点，需要重新压栈等待后续遍历其他邻接点 
                    stack.append(root)
                    stack.append(node)
                    break
        return ans


# 图的BFS，需要deque和hashSet的配合（无向图）
class GraphBFS:
    def graphBfs(self,nodeMap):
        dequeList = deque();ans=[]
        hashSet = set()
        startNode = 0
        dequeList.append(startNode)
        hashSet.add(startNode)
        while dequeList:
            root = dequeList.popleft()
            ans.append(root)
            for node in nodeMap[root]:
                if not node in hashSet:
                    hashSet.add(node)
                    dequeList.append(node)
        return ans


# 拓扑排序,需要辅助队列来记录当前所有的入度为0的点
# 实际上，indegree可以用数组表示，仅当node标号和数组下标有关系时
class TuopuSort:
    def tuopuSort(self,nodeMap,indegree):
        ans=[];dequeList = deque()
        # 首先将入度为0的压栈
        for node,inNum in indegree.items():
            if not inNum:dequeList.append(node)
        while dequeList:
            root = dequeList.popleft()
            ans.append(root)
            for node in nodeMap[root]:
                # 每次弹出root，所有的邻接点入度数-1
                indegree[node]-=1
                if not indegree[node]:dequeList.append(node) #
        return ans


# 最小生成树，1. kruskal算法（无向图）
'''通过最小权重边连接成连通图，先从小到大遍历边，判断2个端点是否在一个集合，不在的话toNode加入fromSet，edge加入result，
遍历完所有的边，得到result即为最小生成树'''

# 最小生成树，2. prim算法（无向图）
'''随便挑个点，解锁所有相关的边，加入heapq，每次选出最小的边，观察toNode是否是新的点，如果是加入set，
加入以后，toNode又会解锁所有邻边，放入heapq，然后判断新的toNode，循环往复，最后得到最小生成树'''


# 最小路径算法，Dijkstra
# 适用于没有负值权重边的图
'''指定一个出发点，得到该点到所有其他点的最短距离，
每次遍历一个点（包括初始点自己，distance=0），遍历该点的所有边以及相应的toNode，如果第一次得到源点到toNode的路径，则添加距离，
如果之前已经有了路径距离，则更新min值，需要hashMap<toNode,distance>来记录'''

