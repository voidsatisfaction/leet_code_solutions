class DisjointSet():
  def __init__(self, n):
    self.forest = [ i for i in range(n) ]
    self.treeNodeNums = [ 1 for i in range(n) ]

  def union(self, a, b):
    rootA = self.root(a)
    rootB = self.root(b)

    if rootA == rootB: return

    if self.treeNodeNums[a] >= self.treeNodeNums[b]:
      self.forest[rootB] = rootA
      self.treeNodeNums[rootA] += self.treeNodeNums[rootB]
    else:
      self.forest[rootA] = rootB
      self.treeNodeNums[rootB] += self.treeNodeNums[rootA]

  def root(self, a):
    initA = a
    while self.forest[a] != a:
      a = self.forest[a]

    self.forest[initA] = a

    return a

class Solution():
  def smallestStringWithSwaps(self, s, pairs):
    dSet = self._createDisjointSet(len(s), pairs)

    groups = {}

    for i in range(len(dSet.forest)):
      groupNum = dSet.root(i)
      if groups.get(groupNum) is None:
        groups[groupNum] = { "indexList": [i], "charList": [s[i]] }
      else:
        groups[groupNum]["indexList"].append(i)
        groups[groupNum]["charList"].append(s[i])

    swapedStringList = [ None for _ in range(len(s)) ]

    for groupNum in groups.keys():
      indexList = groups[groupNum]["indexList"]
      sortedCharList = sorted(groups[groupNum]["charList"])

      for i, index in enumerate(indexList):
        swapedStringList[index] = sortedCharList[i]

    swapedString = "".join(swapedStringList)

    return swapedString

  def _createDisjointSet(self, n, pairs):
    dSet = DisjointSet(n)
    
    for pair in pairs:
      a, b = pair
      dSet.union(a,b)

    return dSet

print(Solution().smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]))
print(Solution().smallestStringWithSwaps("cba", [[0,1],[1,2]]))
print(Solution().smallestStringWithSwaps("ba", [[0, 1], [1, 0]]))