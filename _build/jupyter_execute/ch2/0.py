#!/usr/bin/env python
# coding: utf-8

# # Things I've Learned

# ### This page is still under construction.

# 1. Don’t leave a blank cell at the bottom of your JupyterLab notebook. If the JupyterBook compiler interprets it as an un-executed code block, your book will fail to compile. Which brings up a good point, before debugging and bunch of code, always try re-executing all code blocks from top to bottom first to see if the book will compile. If not, then start debugging.
# 2. Config file
#   1. Edit using Jupyterlab
#   2. Set recompile to “auto,” not “force,” so that only files that have changed get compiled. Speeds up the process.
#   3. Control logo file by finding a pic or creating a graphic and saving a logo.png file. Add this line in the config.yml file below your name.
#     
#     ```
#     logo: logo.png
#     ```
#     
# 3. Content folder
#   1. Only the config.yml file exists at the root, everything else goes inside the content folder.
#   2. Content folder structure: toc.yml, logo.png, introduction.ipynb, and chapter folders.
# 4. Using git at the command shell, you will be asked for your password when you are first linking or pushing content from your laptop out to github. YOU WON’T SEE YOUR PASSWORD AS YOU TYPE. In fact, nothing happens at all. It’s a security feature of the command prompt to not show your password. It would be really helpful if it showed the typical **** as you were typing so you could know your keystrokes were making a difference, but it doesn’t. Trust the force.
# 5. Your online html will be MUCH easier to find after several hours. Initially, you have type the EXACT URL to see anything (use the Introduction.html page url for best results initially).
# 6. The chapter and section file titles are a pain – they work correctly in JupyterBooks if you use something 1.1 for chapter 1, section 1.
# 7. Since the / key escapes characters in MYST, leaving a / on the tail end of a URL will cause the link to display improperly 
# 8. The broader community has embraced LaTeX so much that they’ve given it a hip new hacker name: dollar sign math (DSM). When using double-dollar sign math (DDSM) in MYST markdown, put two hard returns above and below the DDSM code. If not, it tends to display incorrectly.
# 9. Don't get freaked out by using the command prompt with admin privileges. You probbly won't create a rift in the time-space continuum. No guarantees, though.
# 
# 

# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# 1
# ```
# 
