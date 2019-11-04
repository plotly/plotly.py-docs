import frontmatter
from pathlib import Path, PosixPath
import sys

allPosts = [];
  
#get all posts with frontmatter in md format
for md_path in Path("python").glob("**/*.md"):
    post = frontmatter.load(str(md_path))
    if len(post.metadata.keys()) > 0:
        allPosts.append(post); 

for post in allPosts:
    meta = post.metadata
    if "display_as" not in meta['jupyter']['plotly']:
        print(meta['jupyter']['plotly']['name'])