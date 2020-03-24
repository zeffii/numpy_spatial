import numpy as np

verts = [
    [2.48262054,  0.,          0.], [2.18126921,  0.74883066,  0.],
    [1.27680251,  0.99377529,  0.], [0.70457323,  1.07842961,  0.],
    [0.44261043,  1.74782907,  0.], [-0.13097626,  1.5806484,   0.],
    [-0.94757905,  2.16026265,  0.], [-0.93380734,  1.01438518,  0.],
    [-1.52347523,  0.82446356,  0.], [-1.92350252,  0.3209758,  0.],
    [-2.57691846, -0.43001164,  0.], [-1.57387206, -0.85173697,  0.],
    [-0.90413648, -0.98215403,  0.], [-0.92463881, -2.10796417,  0.],
    [-0.16693189, -2.01456837,  0.], [0.31202013, -1.23213965,  0.],
    [1.43075202, -2.18992899,  0.], [2.18188065, -1.69822587,  0.],
    [2.28210863, -0.78344888,  0.]
]

def make_combos(nsize):
    """
    finds all unique pairs of index combinations
      input  num = 5
      output = [[0 1] [0 2] [0 3] [0 4] [1 2] [1 3] [1 4] [2 3] [2 4] [3 4]]
    """
    A1, B1 = np.triu_indices(nsize-1, 0)
    COMBOS = np.ravel(np.column_stack((A1, B1))).reshape((-1, 2)) + [0, 1]
    return COMBOS

def find_distances(VERTS, combos):
    """
    input  verts = np.array of verts
    input  combos = np.array of (all possible) combos between verts, passed as indices of verts
    output  np.array of linear distances between all combos
    """
    column_one = combos[:,0]
    column_two = combos[:,1]
    V1 = np.take(VERTS, column_one, axis=0)
    V2 = np.take(VERTS, column_two, axis=0)
    return np.linalg.norm(V1 - V2, axis=1)

def get_combos_within_distance(combos, distances, dist):
    too_close = np.where(distances < dist)
    return np.take(combos, too_close, axis=0)


VERTS = np.array(verts)
num_verts = VERTS.shape[0]
combos = make_combos(num_verts)
distances = find_distances(VERTS, combos)

# print(distances)
vertex_combos_too_close = get_combos_within_distance(combos, distances, 1.0)
print(vertex_combos_too_close)
# > [[[ 0  1]  [ 0 18]  [ 1  2]  [ 2  3]  [ 3  4]  [ 3  5]  [ 4  5]  
# [ 5  7]  [ 7  8]  [ 8  9]  [ 9 10]  [11 12]  [13 14]  [14 15]  [16 17]  [17 18]]]

# xy, x_ind, y_ind = np.intersect1d(x, y, return_indices=True)




