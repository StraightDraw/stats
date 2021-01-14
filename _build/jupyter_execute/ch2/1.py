#!/usr/bin/env python
# coding: utf-8

# # 2.1 Embedding using `<iframe>`

# Embedding YouTube videos using the `<iframe>` tag is easy. Just go to [YouTube](YouTube.com) and start playing your video. At the bottom, click share, and the entire `<iframe>` code you need is in the pop-up window complete with a "copy" button. Paste that code in between two paragraphs of text with a blank line above and below, and viola!

# For Geogebra animations, life is good, but it takes a bit more work. Here's the animation I'll work with.
# 
# <iframe scrolling="no" title="Convex" src="https://www.geogebra.org/material/iframe/id/yevmvetn/width/1280/height/360/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/false/ctl/false/sfsb/true/szb/false/" width="100%" height="100%" style="display:block;" allowfullscreen=""> </iframe>
# 
# ````{margin}
# ```{seealso}
# Check out Geogebra.org's help center where they explain each codeword option below and what features it controls: [Embedding Using `<iframe>`](https://wiki.geogebra.org/en/Reference:Material_Embedding_(Iframe))
# ```
# ````
# 
# ## Code for the Imbedding
# 
# ````{margin}
# ```{Tip}
# The same code will work in D2L. Go full screen to show extended menu. Type some text (helps place `<iframe>` accurately), then click on the `<code>` button bottom right. Paste the `<iframe>` and *voila*!
# ```
# ````
# 
# 
# Below, we have a URL inside quotes. I have broken it across multiple lines to explain what parts mean what.
# 
# ```
# <iframe scrolling="no" title="Convex"
# src="https://www.geogebra.org/material/iframe/id/yevmvetn/
# width/1280/height/360/border/888888/
# rc/false/
# ai/false/
# sdz/true/
# smb/false/
# stb/false/
# stbh/false/
# ld/false/
# sri/false/
# ctl/false/ 
# sfsb/true/
# szb/false"
# width="100%" height="100%" style="display:block;" allowfullscreen=""> </iframe>
# ```
# 
# 

# ## Explanations
# 
# There is an 8-letter ID for each Geogebra drawing shown at the end of the code block below. To create a new embedding, just copy-paste one that you already got to work.
# 
# ````{margin}
# ```{seealso}
# Check out Geogebra.org's help center where they explain each codeword option below and what features it controls: [Embedding Using `<iframe>`](https://wiki.geogebra.org/en/Reference:Material_Embedding_(Iframe))
# ```
# ````
# 
# ```
# src="https://www.geogebra.org/material/iframe/id/yevmvetn/
# ```
# 
# Choose your height and width to match what your drew. This takes some exprimenting. Geogebra starts at the Top-Left corner of your drawing window and expands the "width" number of pixels right and "height" number of pixels down. Play around with these unitl you get zoomed in on exactly what you want to show.
# 
# ```
# width/1280/height/360/border/888888/
# ```
# 
# The width and height options at the **end** of the `<iframe>` call are what determine how it displays. Use percents to keep it mobile-optimized. Things can get funky if you try using something different than 100%. You'll have to have someone else tell you why.
# 
# The 8's at the end are a color code in hexadecimal allowing to set the border color. Here are the options. You can see my preferences above.
# 
# rc
# : Right-click enabled
# 
# ai
# : Allow input bar
# 
# sdz
# : Shift-drag and zoom enabled
# 
# smb
# : Show menu bar
# 
# stb
# : Show tool bar
# 
# stbh
# : Show tool bar help
# 
# ld
# : Label-dragging enabled
# 
# sri
# : Show reset icon top-right
# 
# ctl
# : Enabled play button to start animation. If set to false, animation starts automatically.
# ````{margin}
# ```{warning}
# If you set "show full-screen button" to true, make sure to put an `allowfullscreen` in your `<iframe>` call, too.
# ```
# ````
# 
# sfsb
# : Show full-screen button
# 
# szb
# : Show zoom buttons
# 
# ## Why is there Five Inches of White Space below my `<iframe>`?
# 
# That's the purpose of this happy little piece of the call. For whatever reason, the default puts a **ton** of white space below an embedding, and this piece of code is just the ticket.
# 
# ```
# style="display:block;"
# ```
