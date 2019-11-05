import frontmatter
from pathlib import Path, PosixPath
import sys

try:
    category = str(sys.argv[1])
except:
    raise Exception("You need to specify a display_as category!")

# will contain all posts with display_as: file_settings
postFamily = []
  
#get all posts with frontmatter in md format
for md_path in Path("python").glob("**/*.md"):
    post = frontmatter.load(str(md_path))
    if len(post.metadata.keys()) > 0:
        if "display_as" in post.metadata['jupyter']['plotly']:
            if post.metadata['jupyter']['plotly']['display_as'] == category:
                postFamily.append({'path':str(md_path), 'order' : post.metadata['jupyter']['plotly']['order']})
            
sortedPostFamily = sorted(postFamily, key = lambda i: i['order'])

order = []
for post in sortedPostFamily:
    order.append(post['order'])

if order[0] != 1:
    raise Exception("Order Check Failed! First post does not have order 1!")

def checkConsecutive(l): 
    return sorted(l) == list(range(min(l), max(l)+1)) 

try:
    if not checkConsecutive(order):
        raise Exception("Order Check Failed! Posts are Not in Consecutive Order!")
except:
    raise Exception("Order Check Failed! Orders are not all integers!!")

print("Order Checks Passed!")