import frontmatter
from pathlib import Path, PosixPath
import sys

# the goal of this program is to take the current order and remap it to be continuous integers

# will contain all posts with display_as: file_settings
fileSettings = []
basic = []
statistical = []
scientific = []
financial = []
maps = []
threedee = []
subplots = []

  
#get all posts with frontmatter in md format
for md_path in Path("python").glob("**/*.md"):
    post = frontmatter.load(str(md_path))
    if len(post.metadata.keys()) > 0:
        if "display_as" in post.metadata['jupyter']['plotly']:
            if post.metadata['jupyter']['plotly']['display_as'] == 'file_settings':
                fileSettings.append(post); 
            if post.metadata['jupyter']['plotly']['display_as'] == 'basic':
                basic.append(post);
            if post.metadata['jupyter']['plotly']['display_as'] == 'statistical':
                statistical.append(post);
            if post.metadata['jupyter']['plotly']['display_as'] == 'scientific':
                scientific.append(post);
            if post.metadata['jupyter']['plotly']['display_as'] == 'financial':
                financial.append(post);
            if post.metadata['jupyter']['plotly']['display_as'] == 'maps':
                maps.append(post);
            if post.metadata['jupyter']['plotly']['display_as'] == '3d_charts':
                threedee.append(post);
            if post.metadata['jupyter']['plotly']['display_as'] == 'subplots':
                subplots.append(post);

for post in fileSettings:
    print(post.metadata['jupyter']['plotly']['order'])
print('888888888888888888888888888888888')

for post in basic:
    print(post.metadata['jupyter']['plotly']['order'])
print('888888888888888888888888888888888')

for post in statistical:
    print(post.metadata['jupyter']['plotly']['order'])
print('888888888888888888888888888888888')

for post in scientific:
    print(post.metadata['jupyter']['plotly']['order'])
print('888888888888888888888888888888888')

for post in financial:
    print(post.metadata['jupyter']['plotly']['order'])
print('888888888888888888888888888888888')

for post in maps:
    print(post.metadata['jupyter']['plotly']['order'])
print('888888888888888888888888888888888')

for post in threedee:
    print(post.metadata['jupyter']['plotly']['order'])

print('888888888888888888888888888888888')

for post in subplots:
    print(post.metadata['jupyter']['plotly']['order'])