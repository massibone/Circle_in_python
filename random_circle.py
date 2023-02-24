import numpy as np
import matplotlib.pyplot as plt
def random_2D_position(c_bx, c_by, r, region_side):
    while True:
        v_pt = region_side * np.random.random((2, ))
        if np.linalg.norm(v_pt - np.array([c_bx, c_by])) > r:
            return v_pt
    return
def plot_region(c_bx, c_by, r, v_l_1, v_l_2, region_side):
    plt.plot(v_l_1[0], v_l_1[1], 's')
    plt.plot(v_l_2[0], v_l_2[1], 'o')
    circle = plt.Circle((c_bx, c_by), r, fill=False)
    plt.gca().add_artist(circle)
    plt.plot([v_l_1[0], v_l_2[0]],[v_l_1[1], v_l_2[1]], '-')
    plt.xlim((0, region_side))
    plt.ylim((0, region_side))
    return
region_side = 500  
c_bx = region_side / 3 + region_side / 3 * np.random.random()
c_by = region_side / 3 + region_side / 3 * np.random.random()
r = region_side / 4 + region_side / 30 * np.random.random()
v_l_1 = random_2D_position(c_bx, c_by, r,region_side)
v_l_2 = random_2D_position(c_bx, c_by, r, region_side)
plot_region(c_bx, c_by, r, v_l_1, v_l_2, region_side)
plt.show()