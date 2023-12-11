

grid_rows = int(input().strip())
grid_columns = int(input().strip())

grid = []

for _ in range(grid_rows):
    list=input("enter the list")
    grid.append(list)
s,count=0,0

columns=len(grid)
rows=len(grid[0])
for i in range(grid_columns):
    for j in range(grid_rows):
        neighbour_grid=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
        count+=1
        
        if grid[1][1]==grid[i][j]:
            for nc,nr in neighbour_grid:
                if(0<=nc<columns and 0<=nr<rows):
                    print(grid[nc][nr],grid[i][j])

        if all(0<=nc<columns and 0<=nr<rows and grid[i][j] >= grid[nc][nr] for nc,nr in neighbour_grid):
            s+=1
        else:
            continue
print(s)



