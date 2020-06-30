---
layout: article
title:  "Using Google Colaboratory"
tags: [colaboratory, google, python, notebook]
---

## Mounting Google Drive

```python
# The following will result in a prompt for authentication
# Go to the link, sign in and obtain the verification code
from google.colab import drive
drive.mount('/content/drive')
```
