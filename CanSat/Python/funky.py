from scipy.spatial.transform import Rotation as R
import numpy as np 
r = R.from_quat([0, 0, 0, 1])

print(r.as_euler('xyz'))