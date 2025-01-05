from attrdict import AttrDict as AD
import os

# Make map_ configuration
map_config = dict(
    geoms=(
        ('norm_box', AD(center=[2.0, 1.5], size=[2.0, 2.0])),
        ('norm_box', AD(center=[-2.5, 2.5], size=[1.25, 1.25])),
        ('norm_box', AD(center=[-5.0, -5.0], size=[1.875, 1.875])),
        ('norm_box', AD(center=[5.0, -6.0], size=[3.0, 3.0])),
        ('norm_box', AD(center=[-7.0, 5.0], size=[2.0, 2.0])),
        ('norm_box', AD(center=[6.0, 7.0], size=[1.8, 1.8])),
        ('norm_boundary', AD(center=[0.0, 0.0], size=[10.0, 10.0])),
    ),
    velocity=(2, [-1.0, 9.0]),
)

current_root = os.getcwd()
map_path = os.path.join(current_root, 'map.png')
map_config2 = dict(
    image=(map_path),
)
