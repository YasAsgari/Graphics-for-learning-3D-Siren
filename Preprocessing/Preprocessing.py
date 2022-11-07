#!/usr/bin/env python
# coding: utf-8

# In[2]:


import trimesh
for string in ['cow','airplane','sofa']:
    mesh = trimesh.load(f'{string}.obj')
    mesh.show()
    mesh.export(f'{string}-mesh.stl')

