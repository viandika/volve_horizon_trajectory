import pathlib as path
import pandas as pd
from lxml import etree as et
from collections import defaultdict
import plotly.express as px

witsml = path.Path(r'D:\codes\python\volve_things\witsml')
data = defaultdict(list)
for file in witsml.rglob('*.xml'):
    tree = et.parse(str(file))
    for elem in tree.getiterator():
        elem.tag = et.QName(elem).localname
    for traj in tree.findall('trajectory/trajectoryStation'):
        data['nameWell'].append(tree.find('trajectory/nameWell').text)
        data['dispNs'].append(float(traj.find('dispNs').text))
        data['dispEw'].append(float(traj.find('dispEw').text))
        data['tvd'].append(float(traj.find('tvd').text)*-1)
        data['incl'].append(traj.find('incl').text)
trajectory = pd.DataFrame(data)
fig = px.line_3d(trajectory, x="dispNs", y="dispEw", z="tvd", color='nameWell')
fig.show()

# tree = et.parse(r'D:\codes\python\volve_things\witsml\4.xml')
#
# for elem in tree.getiterator():
#     elem.tag = et.QName(elem).localname
#
# data = defaultdict(list)
#
# for traj in tree.findall('trajectory/trajectoryStation'):
#     data['dispNs'].append(float(traj.find('dispNs').text))
#     data['dispEw'].append(float(traj.find('dispEw').text))
#     data['tvd'].append(float(traj.find('tvd').text))
#     data['incl'].append(traj.find('incl').text)
#
# trajectory = pd.DataFrame(data)
#
# fig = px.line_3d(trajectory, x="dispNs", y="dispEw", z="tvd")
# fig.show()
