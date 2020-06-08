---
layout: article
title:  "Enabling auto-reload in Jupyter"
categories: [cheatsheets]
tags: [python, jupyter]
---

```python
%load_ext autoreload
%autoreload 2

# %autoreload 0 : disable automatic reloading
# %autoreload 1 : auto-reload all modules imported with %aimport 
# %autoreload 2 : auto-reload all modules
```

Reference: [https://ipython.org/ipython-doc/stable/config/extensions/autoreload.html](https://ipython.org/ipython-doc/stable/config/extensions/autoreload.html)

