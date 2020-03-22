sx, sy, tx, ty = map(int,input().split())
height = ty - sy
width = tx - sx 
# path1
path1 = ['U' for _ in range(height) ]
path1.extend([ 'R' for _ in range(width)])
# path2
path2 = ['D' for _ in range(height)]
path2.extend([ 'L' for _ in range(width)])
# path3
path3 = ['U' for _ in range(height+1)]
path3.extend([ 'R' for _ in range(width+1)])
path3.insert(0,'L')
path3.extend(['D'])
# path4
path4 = ['D' for _ in range(height+1)]
path4.extend([ 'L' for _ in range(width+1) ])
path4.insert(0,'R')
path4.extend(['U'])

path = path1
path.extend(path2)
path.extend(path3)
path.extend(path4)

print(''.join(path))