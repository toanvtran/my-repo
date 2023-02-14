
import random

def create_distance_matrix(N,max):
    d_mat = list()
    for i in range(N):
        row = [None]*N
        row[i] = 0
        d_mat.append(row)
    for i in range(0,N):
        d_mat[i][i] = 0
    W = list((j,i) for i in range(0,N) for j in range(0,i))
    for coor in W:
        d_mat[coor[0]][coor[1]] = random.randrange(0,max)
        d_mat[coor[1]][coor[0]] = d_mat[coor[0]][coor[1]]
    
    return d_mat

# distance_matrix = [[0, 2, 3, 10], [2, 0, 3, 6], [3, 3, 0, 9], [10, 6, 9, 0]]

def create_data(N,M,K):
    with open('..\data\dataset_' + str(N) + '.txt', 'w+') as writefile:
        for i in range(K):
            distance_matrix = create_distance_matrix(N,M)
            writefile.write(str(distance_matrix) + '\n' ) 

create_data(18, 20, 10)