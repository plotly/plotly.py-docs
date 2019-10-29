import frontmatter
from pathlib import Path, PosixPath

allPosts = [];

#get all frontmatter from posts
for md_path in Path("python").glob("*.md"):
    post = frontmatter.load(str(md_path))
    if len(post.metadata.keys()) > 0:
        allPosts.append(post)

#make sure that every post that is not a redirect has a name tag in the front matter
noNamePaths = [];
for post in allPosts:
    if len(post.metadata.keys()) > 0:
        try:
            name = post.metadata['jupyter']['plotly']['name']
        
        except:
            noNamePaths.append(post.metadata)

if (len(noNamePaths) > 0):
    raise Exception("CI Check #1 Not Passed: following permalinks:'{}' are not redirects but are missing a name frontmatter\n".format(', '.join([str(item['jupyter']['plotly']['permalink']) for item in noNamePaths])))

print("CI Check #1 Passed: All non-redirect posts have names!")