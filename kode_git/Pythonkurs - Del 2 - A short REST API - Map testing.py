#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%pip install folium


# In[ ]:


import folium
# pip install folium, xyzservices, branca


# In[ ]:


icon_lat = 60.39
icon_lon = 5.32
icon_desc = "Bergen?"


# In[ ]:


map = folium.Map(location=[60.39, 5.32], zoom_start=4, control_scale=True)


# In[ ]:


folium.Marker(
    location=[icon_lat, icon_lon],
    popup=icon_desc,
    icon=folium.Icon(color="green", icon="ok-sign"),
).add_to(map)


# In[ ]:


map


# In[ ]:


output_map = "base_map.html"
map.save(output_map)


# In[ ]:




