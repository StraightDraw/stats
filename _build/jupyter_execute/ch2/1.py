#!/usr/bin/env python
# coding: utf-8

# # 2.1 Embedding with `<iframe>`

# Embedding with `<iframe>` is easy for YouTube. Click to play the video, and down near the bottom right you'll see a "share" button. Click there, and the whole `<iframe>` code pops up. Just paste that into your HTML, and *viola*!
# 
# Geogebra is a powerful tool for creating animations and dynamic figures, and the `<iframe>` will embed them anywhere a YouTube video can be embedded:
# 
# * LMS software (e.g. D2L)
# * In a blog
# * In your new JupyterBook
# 
# ## Geogebra Embedding Example
# 
# First let's show a nice animation that visually describes the definition of convex polygons.
# 
# <iframe scrolling="no" title="Convex"
# src="https://www.geogebra.org/material/iframe/id/yevmvetn/width/1180/height/360/border/888888/ai/false/ctl/falseld/false/rc/false/sdz/true/sfsb/true/smb/false/sri/false/stb/false/stbh/false/" width="100%" height="100%" style="display:block;" allowfullscreen=""> </iframe>
# 
# ## How to Code It
# 
# The code below is broken into sections to better illustrate what produced the animation above. One key point to understand is the two height/width arguments. The first pair sets the viewing window on Geogebra in your actual drawing itself. Play around with these until you get the viewing rectangle you want. The baseline point is the top-left corner of the Geogebra window. Increase width to more content to the right. Increase height to more content at the bottom.
# 
# ```
# <iframe scrolling="no" title="Convex"
# src="https://www.geogebra.org/material/iframe/id/yevmvetn/
# width/1180/height/360/border/888888/
# ai/false/
# ctl/false
# ld/false/
# rc/false/
# sdz/true/
# sfsb/true/
# smb/false/
# sri/false/
# stb/false/
# stbh/false/" 
# width="100%" height="100%" style="display:block;" allowfullscreen=""> </iframe>
# ```
# 
# Every Geogebra file saved online has an 8-letter ID code which, in the example, is shown at the end of the 2nd line: `id/yevmvetn`. You can get one animation working, then just copy it's code in where you want a new one. Just swap out the 8-letter ID for a new one, and *viola*!
# 
# The `888888` controls the color of the border. I leave the default alone, but you can enter a different hexadecimal color code if you'd like. I found out how to use the following features using the [Geogebra help file for Embedding](https://wiki.geogebra.org/en/Reference:Material_Embedding_(Iframe)).
# 
# ai
# : Activiate input bar
# 
# ctl
# : Show play button that starts/pauses animation
# 
# ld
# : Enables label-dragging
# 
# rc
# : Enables right-clicking
# 
# sdz
# : Enable shift-drag and zoom
# 
# sfsb
# : Show full screen button
# 
# smb
# : Show menu bar
# 
# sri
# : Show reset icon (top-right)
# 
# stb
# : Show tool bar
# 
# stbh
# : Show tool bar help
# 
# szb
# : Show zoom button
# 
# Set them true or false yourself and see what happens. It's trial and error, and you get to decide what you want.
# 
# 
# 
# 
# 
# 
