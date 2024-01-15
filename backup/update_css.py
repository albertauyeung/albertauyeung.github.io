import os

css = """
<style>
.docs-markdown h1 { font-size: 1.75rem; }
.docs-markdown h2 { font-size: 1.45rem; }
.text-base { font-size: 0.95rem; }
</style>
"""

for path, subdirs, files in os.walk("."):
    for name in files:
        if name == "index.html":
            full_path = os.path.join(path, name)
            with open(full_path, "r", encoding="utf-8") as infile:
                content = infile.read()

            content = content.replace("\n</head>", css + "</head>")
            with open(full_path, "w", encoding="utf-8") as outfile:
                outfile.write(content)

print("Successfully updated all index.html")
