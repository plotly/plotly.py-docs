import frontmatter
from pathlib import Path, PosixPath
import sys

# the goal of this program is to take the current order and remap it to be continuous integers
# take in a list that is sorted, and map to integers



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
                fileSettings.append(post.metadata['jupyter']['plotly']['order'])
            if post.metadata['jupyter']['plotly']['display_as'] == 'basic':
                basic.append(post.metadata['jupyter']['plotly']['order'])
            if post.metadata['jupyter']['plotly']['display_as'] == 'statistical':
                statistical.append(post.metadata['jupyter']['plotly']['order'])
            if post.metadata['jupyter']['plotly']['display_as'] == 'scientific':
                scientific.append(post.metadata['jupyter']['plotly']['order'])
            if post.metadata['jupyter']['plotly']['display_as'] == 'financial':
                financial.append(post.metadata['jupyter']['plotly']['order'])
            if post.metadata['jupyter']['plotly']['display_as'] == 'maps':
                maps.append(post.metadata['jupyter']['plotly']['order'])
            if post.metadata['jupyter']['plotly']['display_as'] == '3d_charts':
                threedee.append(post.metadata['jupyter']['plotly']['order'])
            if post.metadata['jupyter']['plotly']['display_as'] == 'multiple_axes':
                subplots.append(post.metadata['jupyter']['plotly']['order'])


sortedPlotlyFundamentals = sorted(fileSettings)
sortedBasic = sorted(basic)
sortedStatistical = sorted(statistical)
sortedScientitic = sorted(scientific)
sortedFinancial = sorted(financial)
sortedMaps = sorted(maps)
sorted3d = sorted(threedee)
sortedSubplots = sorted(subplots)

order = list(range(0,100))

# starts with 1, increase by 1
def sortList(posts):
    for index, post in enumerate(posts):
        if index+1 != post:
            post = index+1

sortList(sortedBasic)


for index, md_path in enumerate(Path("python").glob("**/*.md")):
    post = frontmatter.load(str(md_path))
    if "display_as" in post.metadata['jupyter']['plotly']:
        if post.metadata['jupyter']['plotly']['display_as'] == 'basic':
            print(post.metadata['jupyter']['plotly']['order'])

    