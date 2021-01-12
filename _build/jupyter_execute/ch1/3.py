#!/usr/bin/env python
# coding: utf-8

# # 1.3 JupyterBooks

# The hard part is over, and let's be real. It was not that hard. It wasn't that hard when I spent twenty hours of my life figuring it out, either, but it felt that way. I like understanding the tools I'm using and how they work, but these are super powerful tools with lots of applications, so you can spend a lot of time digging around and not getting anywhere. If you've made it here, give yourself a big pat on the back.

# Make sure to open Conda in Administrator mode. If you didn't, close it and reopen. Open the CMD.exe Prompt from Conda Navigator, and use the **cd** command (change directory) to get to the "newbook" folder on your local machine. For me, it looked like this:
# 
# ```
# cd documents/conda/newbook
# ```
# 
# Now we're ready to use JupyterBooks to build out all the ipynb source files into HTML a browser can understand.
# 
# ```
# jb build content
# ```
# 
# The "jb" is short for jupyter-book, so this version also works (but you'll never use it).
# 
# ```
# jupyter-book build content
# ```
# 
# We're asking the jupyter-book package to run its build command on everything inside the content folder.

# ## Add, Commit, Push
# 
# These commands work exactly as before. Now that we've built out our JupyterBook, we have a bunch of new files in our repo folder. Check out the \_build folder, and you'll see tons of stuff. Go to the html folder and click on the file "Introduction.html" to preview your JupyterBook compile locally. You'll be doing this often as you update your JupyterBook.
# 
# Still, your repos have no idea the new files exist, so we use the same process as before.
# 
# ```
# git add ./*
# ```
# ```
# git commit -m "Put a note here"
# ```
# ```
# git push
# ```
# 
# ## Lauch your JupyterBook Online
# 
# The **ghp-import** script is a wonderful tool. While building a website on GitHub using Jekyll isn't impossible, it can be tricky to get all the settings exactly right. Not for us, though.
# 
# ````{margin}
# ```{warning}
# My Norton firewall prevented this command from executing, and I had to click on the pop-up warning and create an exception. Depending on your settings, you firewall may object earlier or later.
# ```
# ````
# 
# ```
# ghp-import -n -p -f _build/html
# ```
# 
# We have three options indicated by the dashes.
# 
# * -n means to **not** use Jekyll to build out the HTML on GitHub Pages. JupyterBooks has handled that part already.
# * -p is a push
# * -f forces the push
# 
# The script does not work for me without all three options included. If it doesn't bonk, you're website is live.
# 
# ````{warning}
# Soon, you will be able to reference your URL without case sensivity, and various shortcuts will work like leaving off the .html on web references. For now, only the perfect URL will link you up, and GitHub's default point to the "index.html" probably will throw a 404 error code at you.
# ````
# For the first few minutes your website is live, you will have to locate it using the Introduction.html page. Since my username is Straightdraw, the URL looks like this:
# 
# ```
# https://straightdraw.github.io/newbook/Introduction.html
# ```
# 
# Tweak the username, and copy-paste into your web browser. Congratulations! You now have a live JupyterBook published on the interwebs.
