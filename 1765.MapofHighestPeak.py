class Solution(object):
    def highestPeak(self, isWater):
        m=len(isWater)
        n=len(isWater[0])
        q=deque()
        visit=set()
        height = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(isWater[i][j]):
                    height[i][j]=0
                    q.append((i,j))
                    visit.add((i,j))
        while q:
            r,c=q.popleft()
            h=height[r][c]
            neighbors=[[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for nr,nc in neighbors:
                if(nr<0 or nc<0 or nr==m or nc==n or ((nr,nc) in visit)):
                    continue
                q.append((nr,nc))
                visit.add((nr,nc))
                height[nr][nc]=h+1
        return height
