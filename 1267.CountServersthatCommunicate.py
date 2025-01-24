class Solution(object):
    def countServers(self, grid):
        row=[]
        column=[]
        position=[]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    row.append(i)
                    column.append(j)
                    position.append([i,j])
        c=0
        for i,j in position:
            if(row.count(i)>1 or column.count(j)>1):
                c+=1
        return c

