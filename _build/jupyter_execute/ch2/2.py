#!/usr/bin/env python
# coding: utf-8

# # 2.2 Different Engines in JupyterBooks

# The three programs (engines) in the name Jupyter are Julie, Python and R. For data science, Python and R are by far the most popular choices over the past few years. But mathematicians may prefer using other engines that produce the same features as Mathematica, Maple and MATLAB. This section is about how to install engines for MATLAB and SciLab, two math-science programming languages that support courses from programming to physics, math to chemistry, calculus to PDE's, linear algebra to numerical analysis.

# ## Installing MATLAB API for Python

# MATLAB comes with a Python engine installer, but we have to get there to activate it. That means we have to find the MATLAB root. I found mine clicking through File Explorer. After using the
# 
# ```
# cd..
# ```
# command half a dozen times to return to the `c:\>` prompt, the following path led my MATLAB root.
# 
# ```
# cd program files/matlab/r2019b
# ```
# No, I didn't want a 2020 version. Believe it or not.
# 
# ````{warning}
# MATLAB is not compatible with the latest releases of Python. I had to create an environment in Conda with a Python 3.6 kernel. Then I used the Python 3.6 environment to install the MATLAB engine. For reference, that was in January, 2021.
# ````

# Now I can find my way through my MATLAB files to the Python engine. This should work if you're at the version root directory for your MATLAB program files.
# 
# ```
# cd extern/engines/python
# ```
# 
# If you type `dir` and Enter, you'll see the directory includes a file called `setup.py` which is what we came here for.
# 
# ```
# pip install setup.py
# ```
# 
# The final step is to create the MATLAB kernel for the environment.
# 
# ```
# pip install matlab_kernel
# ```
# Now, when you open a new JupyterLab file, you will have the option to run either the Python kernel or the MATLAB kernel, whichever works best for your current project.

# ## Installing the SciLab Engine
# 
# This page is still under construction.
