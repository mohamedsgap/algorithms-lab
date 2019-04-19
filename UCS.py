
import queue as q
from collections import defaultdict

class g:
	def __init__(self):
		self.graph=defaultdict(list)
		self.edgeCost={}
		self.parents = {}
		self.visitedInClosed={}
		self.visitedInQueue={}
		
	def addEdge(self,u,v,cost):
		self.graph[u].append(v)
		self.edgeCost[(u,v)]=cost
		
	def removeFromQueue(self,oldqu,item):
		newqu=q.PriorityQueue()
		while not oldqu.empty():
			p=oldqu.get()
			if p!=item:
				newqu.put(p)
		return newqu
		
	def ucs(self, start, goal):
		self.queue = q.PriorityQueue()
		self.queue.put((0, start))
		self.visitedInQueue[start]=0
		
		while not self.queue.empty():
			cost, node = self.queue.get() #return tuple (cost, node)
			
			self.visitedInClosed[node]=cost
			
			#if node in self.visitedInQueue:
			
			del self.visitedInQueue[node]
				
			print(node,"(",cost,")")
			if node == goal:
				print("Final Cost:",cost)
				break
			for i in self.graph[node]:
				total_cost = cost + self.edgeCost[(node, i)]				
				if (i in self.visitedInClosed and total_cost >= self.visitedInClosed[i])or(i in self.visitedInQueue and total_cost >= self.visitedInQueue[i]):
					pass
				else:
					if i in self.visitedInQueue and total_cost < self.visitedInQueue[i]:
						self.queue=self.removeFromQueue(self.queue,(self.visitedInQueue[i],i))
					self.queue.put((total_cost, i))
					self.visitedInQueue[i]=total_cost
					self.parents[i]=node
		#print(self.parents)
		cur=goal
		reverspath=[cur]
		while True:
			if cur == start:
				break
			else:
				cur=self.parents[cur]
				reverspath.append(cur)
		reverspath.reverse()
		print("Shortest Path:",reverspath)


o=g()
o.addEdge(1,2,3)
o.addEdge(1,3,2)
o.addEdge(2,4,4)
o.addEdge(3,4,3)
o.addEdge(4,5,1)
o.addEdge(5,6,20)
o.ucs(1,6)

'''
o=g()
o.addEdge(1,2,10)
o.addEdge(1,3,20)
o.addEdge(2,4,2)
o.addEdge(3,4,-15)
o.addEdge(4,5,15)
o.ucs(1,5)
'''
'''
o=g()
o.addEdge(1,2,2)
o.addEdge(1,5,1)
o.addEdge(2,3,3)
o.addEdge(2,6,5)
o.addEdge(3,4,4)
o.addEdge(4,8,6)
o.addEdge(5,9,1)
o.addEdge(6,5,3)
o.addEdge(6,7,3)
o.addEdge(6,10,6)
o.addEdge(7,3,4)
o.addEdge(7,8,5)
o.addEdge(7,11,4)
o.addEdge(8,12,12)
o.addEdge(9,10,2)
o.addEdge(10,11,6)
o.addEdge(11,12,7)

o.ucs(1,12)
'''


'''
o=g()
o.addEdge(0,1,1)
o.addEdge(0,2,1)
o.addEdge(1,3,3)
o.addEdge(2,5,2)
o.addEdge(3,5,2)
o.addEdge(3,6,4)
o.addEdge(4,6,1)
o.addEdge(4,7,5)
o.addEdge(5,0,3)
o.addEdge(5,4,4)
o.addEdge(5,8,1)
o.addEdge(6,7,1)
o.addEdge(8,4,1)
o.addEdge(8,9,3)
o.addEdge(9,7,1)
o.ucs(0,7)
'''


