import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


# define the geometry of a path:
verts = [(0.0, 0.0), # P0
         (0.2, 1.0), # P1
         (1.0, 0.8), # P2
         (0.8, 0.0), # P3
        ]

codes = [Path.MOVETO, # put the "pen" at P0
         Path.CURVE4, # and draw bezier curves
         Path.CURVE4, # from P0 to P1, to P2
         Path.CURVE4, # to P3.
        ]

path = Path(verts, codes) # build path from vertices & command codes


# build stylizeable "patch" to visualize geometric "path":
patch = patches.PathPatch(path, facecolor='none', 
                                edgecolor='blue', lw=4)


ax = plt.axes() # gca = get current plot's "axes"

ax.add_patch(patch)

# draw control points:
xs, ys = zip(*verts)
ax.plot(xs, ys, 'o--', lw=2, color='black', ms=10)


# label the control points:
ax.text( 0.05, -0.05, 'P0')
ax.text( 0.15,  1.05, 'P1')
ax.text( 1.05,  0.85, 'P2')
ax.text( 0.85, -0.05, 'P3')

# resize the plot:
ax.set_xlim(-0.1, 1.15)
ax.set_ylim(-0.1, 1.15)
ax.set_aspect("equal")
plt.show()