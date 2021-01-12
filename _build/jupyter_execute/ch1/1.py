#!/usr/bin/env python
# coding: utf-8

# # 1.1 Conda

# Anaconda is your quarterback. Set it up correctly, and life is good.
# 
# ````{margin}
# MYST special code blocks are really easy. This one's a warning, and below you see a tip and hint which use the same styling.
# ````
# 
# ````{warning}
# The name Miniconda seems like it might be great option that's easier to use, but Anaconda Navigator is best for beginners.
# ````

# ## Download Anaconda. Use Navigator
# 
# Go to [Anaconda.com](https://www.anaconda.com/products/individual) and dowload the free individual package of Anaconda. Once it's installed, find **Anaconda Navigator**. Don't just open it, put the icon in your start menu. You'll neeed it often.
# 
# ````{tip}
# Always open Anaconda using the "Run as administrator" option  (right click, then "more" menu). You don't need administrator level access for most things, but it's annoying to have correct commands fail for no apparent reason.
# ````
# 
# Conda is an environment manager which can handle multiple complex coding environments. We don't need that. We just want one simple coding environment. We'll create a new environment and keep things simple.
# 
# ````{margin}
# To create the hint, we just use the following:
# ```
# ````{hint}
# ```
# ````
# 
# 
# 
# ````{hint}
# Don't make any changes to the base(root) environment. That's the control center.
# ````

# ### Python Environment
# I suggest you begin with a Python environment, just to get started. My entire Geometry Juypyterbook was built in a plain vanilla Python envrionment. Why not get everything working properly in less than an hour, then work on other environments and engines? Wish I had.
# 
# To create your new environment, click the "Environments" tab on the left menu bar, then create as shown below.
# 
# ````{margin}
# Check out this [wiki](https://wiki.math.ntnu.no/_media/anaconda) for pretty good instructions about installing and setting up Anaconda.
# ````
# 
# ![Conda Navigator Illustrion](https://wiki.math.ntnu.no/_media/anaconda/navigator-create-environment.png?w=550&tok=9ef301)
# 

# In the pop-up, select the most recent stable version of Python which, as of January, 2021, is Python 3.8. That's your engine. If you want to use R, MATLAB or SciLab as your engine I'll try to help with that later. The install will take a minute or two. When it's ready, click back to "Home" from the top-left menu and use the drop-down to make sure you are in the new environment.
# 
# You'll have the option to install several packages, all of which have their uses. For JupyterBooks, we only need to install JupyterLabs and the CMD.exe Prompt.

# ### Installing packages
# 
# We need to get the **JupyterBooks** and **github** packages installed, and the Python installer program **pip** helps with that. Open the CMD.exe Prompt and execute these commands:

# ````
# conda install pip
# ````
# ````
# conda install git
# ````
# ````
# pip install -U jupyter-book
# ````
# ````
# pip install ghp-import
# ````

# Now we have all the tools we need to throw this JupyterBooks touchdown.
