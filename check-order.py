import frontmatter
from pathlib import Path, PosixPath
import sys

categories = ["file_settings", "basic", "statistical", "scientific", "maps", "3d_charts", "multiple_axes"]
try:
    path = str(sys.argv[1])
except:
    raise Exception("You need to specify a path!")

for category in categories:
    postFamily = []
    #get all posts with frontmatter in md format
    for md_path in Path(path).glob("**/*.md"):
        post = frontmatter.load(str(md_path))
        if len(post.metadata.keys()) > 0:
            if "display_as" in post.metadata['jupyter']['plotly']:
                if post.metadata['jupyter']['plotly']['display_as'] == category:
                    postFamily.append({'path':str(md_path), 'order' : post.metadata['jupyter']['plotly']['order']})
                
    sortedPostFamily = sorted(postFamily, key = lambda i: i['order'])

    order = []

    for post in sortedPostFamily:
        if post['order'] == 5:
            raise Exception("Order Check Failed! Post {} cannot have order 5!".format(post['path']))
        order.append(post['order'])

    print(order)

    if order[0] != 1:
        raise Exception("Order Check Failed! First post in {} display_as does not have order 1!".format(category))

    def checkConsecutive(l): 
        return sorted(l) == list(range(min(l), max(l)+1)) 

    try:
        checkConsecutive(order)
    except:
        raise Exception("Order Check Failed! Orders in {} display_as are not consecutive integers!!".format(category))

    if len(order) != len(set(order)):
        raise Exception("Order Check Failed! {} display_as has duplicate order frontmatter!!".format(category))


    print("Order Checks Passed for {} display_as!".format(category))
    order = []