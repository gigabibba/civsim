import pyglet

#---SETTINGS---
global fullscreen
fullscreen = None

global resolution
resolution = None


#---COMMON-------------------------------------------------------------------------------------------------------------

#---UI---
global selected
global click_selected #cleared on mouse release

selected = None
click_selected = None

#---SWITCHING GAME STATE---

global gs_entries

gs_entries = [None] * 20

#---COLLISIONBOXES, EVENT HANDLING---
global scene_objects
global scene_objects_size

global update_queue
global update_queue_size

scene_objects_size = 2000
scene_objects = [None] * scene_objects_size #objects that are on screen are added to this list for box checks and event handling

update_queue_size = 100
update_queue = [None] * update_queue_size

#---RESOURCES---
global sprite_textures

sprite_textures = {}

# ---WINDOWING---
global window
global aa

aa = None
window = None

#---BATCHES AND GROUPS---
global batch
global groups
global front_group_index

batch = pyglet.graphics.Batch()

global_transformation_group = None
scene_ordered_group = None
scene_transformation_group = None
menu_ordered_group = None

num_scene_groups = 7
num_menu_groups = 6
groups = []

texture_groups = {}
line_groups = {}

