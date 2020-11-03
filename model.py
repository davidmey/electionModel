import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
from scipy.stats import binom
from random import random

# data is of the form: stateName, sampleSize, pBiden, pTrump, pBidenWinsState, color, electoralValue, timesBidenWon, timesTrumpWon

data = {
    'New Jersey':       [721, 56, 36, 0, 'red', 14, 0, 0],
    'Rhode Island':     [517, 62, 36, 0, 'red', 4, 0, 0],
    'Massachusetts':    [929, 62, 28, 0, 'red', 11, 0, 0],
    'Connecticut':      [1000, 51, 26, 0, 'red', 7, 0, 0],
    'Maryland':         [820, 58, 33, 0, 'red', 10, 0, 0],
    'New York':         [450, 61, 33, 0, 'red', 29, 0, 0],
    'Delaware':         [588, 61, 38, 0, 'red', 3, 0, 0],
    'Florida':          [1657, 47, 42, 0, 'red', 29, 0, 0],
    'Ohio':             [1440, 47, 43, 0, 'red', 18, 0, 0],
    'Pennsylvania':     [502, 50, 45, 0, 'red', 20, 0, 0],
    'Illinois':         [450, 55, 38, 0, 'red', 20, 0, 0],
    'California':       [800, 62, 31, 0, 'red', 55, 0, 0],
    'Hawaii':           [988, 61, 28, 0, 'red', 4, 0, 0],
    'Virginia':         [690, 54, 43, 0, 'red', 13, 0, 0],
    'Michigan':         [450, 50, 43, 0, 'red', 16, 0, 0],
    'Indiana':          [1147, 42, 53, 0, 'red', 11, 0, 0],
    'North Carolina':   [707, 49, 48, 0, 'red', 15, 0, 0],
    'Georgia':          [749, 50, 50, 0, 'red', 16, 0, 0],
    'Tennessee':        [485, 41, 58, 0, 'red', 11, 0, 0],
    'New Hampshire':    [757, 53, 43, 0, 'red', 4, 0, 0],
    'South Carolina':   [880, 44, 53, 0, 'red', 9, 0, 0],
    'Louisiana':        [755, 36, 59, 0, 'red', 8, 0, 0],
    'Kentucky':         [625, 36, 56, 0, 'red', 8, 0, 0],
    'Wisconsin':        [1253, 52, 41, 0, 'red', 10, 0, 0],
    'Washington':       [591, 55, 34, 0, 'red', 12, 0, 0],
    'Alabama':          [1045, 38, 58, 0, 'red', 9, 0, 0],
    'Missouri':         [1109, 43, 52, 0, 'red', 10, 0, 0],
    'Texas':            [763, 49, 50, 0, 'red', 38, 0, 0],
    'West Virginia':    [450, 39, 53, 0, 'red', 5, 0, 0],
    'Vermont':          [584, 62, 32, 0, 'red', 3, 0, 0],
    'Minnesota':        [770, 54, 43, 0, 'red', 10, 0, 0],
    'Mississippi':      [561, 41, 55, 0, 'red', 6, 0, 0],
    'Iowa':             [814, 41, 48, 0, 'red', 6, 0, 0],
    'Arkansas':         [591, 32, 65, 0, 'red', 6, 0, 0],
    'Oklahoma':         [379, 35, 60, 0, 'red', 7, 0, 0],
    'Arizona':          [717, 48, 48, 0, 'red', 11, 0, 0],
    'Colorado':         [709, 54, 42, 0, 'red', 9, 0, 0],
    'Maine':            [301, 50, 47, 0, 'red', 4, 0, 0],
    'Oregon':           [342, 60, 37, 0, 'red', 7, 0, 0],
    'Kansas':           [755, 41, 48, 0, 'red', 6, 0, 0],
    'Utah':             [660, 44, 51, 0, 'red', 6, 0, 0],
    'Nebraska':         [1666, 43, 55, 0, 'red', 5, 0, 0],
    'Nevada':           [809, 49, 43, 0, 'red', 6, 0, 0],
    'Idaho':            [824, 40, 58, 0, 'red', 4, 0, 0],
    'New Mexico':       [1180, 54, 42, 0, 'red', 5, 0, 0],
    'South Dakota':     [625, 40, 51, 0, 'red', 3, 0, 0],
    'North Dakota':     [460, 37, 61, 0, 'red', 3, 0, 0],
    'Montana':          [758, 43, 49, 0, 'red', 3, 0, 0],
    'Wyoming':          [330, 33, 66, 0, 'red', 3, 0, 0],
    'Alaska':           [800, 45, 50, 0, 'red', 3, 0, 0],
    'District of Columbia': [457, 94, 5, 0, 'red', 3, 0, 0]}

reps = 100
bias = 0

# extract args
l = len(sys.argv)
for i in range(0, len(sys.argv)):
    if sys.argv[i] == '-i':
        reps = int(sys.argv[i + 1])
    if sys.argv[i] == '-b':
        bias = float(sys.argv[i + 1])

# initialize pBidenWins
for state in data:
    n = data[state][0]
    probsum = (data[state][1] + data[state][2])
    probVoteBiden = data[state][1] / probsum
    k = n * (.5 + (bias / 100))
    data[state][3] = 1 - binom.cdf(k, n, probVoteBiden)

# run simulations
results_tallies = [0, 0, 0]
for i in range(0, reps):
    biden_votes = 0
    trump_votes = 0

    # determine who wins each state
    for state in data:
        if random() <= data[state][3]:
            biden_votes += data[state][5]
            data[state][6] += 1
        else:
            trump_votes += data[state][5]
            data[state][7] += 1

    # determine who won election
    if biden_votes > trump_votes:
        results_tallies[0] += 1
    elif biden_votes == trump_votes:
        results_tallies[2] += 1
    else:
        results_tallies[1] += 1

    # print race results
    if '-v' in sys.argv:
        title = ""
        if biden_votes > trump_votes:
            title += "Biden Wins: "
        elif biden_votes == trump_votes:
            title += "It is a Tie: "
        else:
            title += "Trump Wins: "
        title += str(biden_votes) + " to " + str(trump_votes)
        print(title)

# plot
if '-p' in sys.argv:
    biden_votes = 0
    trump_votes = 0

    # calculate state agregate results over simulations
    for state in data:
        biden_votes += data[state][5] * data[state][6]
        trump_votes += data[state][5] * data[state][7]
        if data[state][7] < data[state][6]:
            data[state][4] = 'blue'
        elif data[state][7] == data[state][6]:
            data[state][4] = 'yellow'
    biden_votes /= reps
    trump_votes /= reps

    # calculate who is favored to win
    if results_tallies[0] + results_tallies[2] > results_tallies[1]:
        title = "Biden Wins in " + str(results_tallies[0]) + " of " + str(
            reps) + " Simulations (" + str(round(100 * results_tallies[0] / reps, 2)) + "%)\n"
    elif results_tallies[0] + results_tallies[2] == results_tallies[1]:
        title = "Trump Wins in " + str(results_tallies[1]) + " of " + str(
            reps) + " Simulations (" + str(round(100 * results_tallies[1] / reps, 2)) + "%)\n"
    else:
        title = "Biden and Trump Each Win " + \
            str(reps / 2) + " Simulations (50%)\n"
    title += "Expected Electoral College Results: " + \
        str(round(biden_votes, 2)) + " to " + str(round(trump_votes, 2))

    # Use this handy dandy code I only slightly modified to plot chart
    ATOLL_CUTOFF = 0.005
    m = Basemap(llcrnrlon=-121, llcrnrlat=20, urcrnrlon=-62, urcrnrlat=51,
                projection='lcc', lat_1=32, lat_2=45, lon_0=-95)

    # Mercator projection, for Alaska and Hawaii
    m_ = Basemap(llcrnrlon=-190, llcrnrlat=20, urcrnrlon=-143, urcrnrlat=46,
                 projection='merc', lat_ts=20)  # do not change these numbers

    # load the shapefile, use the name 'states'
    m.readshapefile('st99_d00', name='states', drawbounds=True)

    colors = {}
    statenames = []
    cmap = plt.cm.hot  # use 'hot' colormap
    ax = plt.gca()  # get current axes instance
    for i, shapedict in enumerate(m.states_info):
        # Translate the noncontiguous states:
        if shapedict['NAME'] in ['Alaska', 'Hawaii']:
            seg = m.states[int(shapedict['SHAPENUM'] - 1)]
            # Only include the 8 main islands of Hawaii so that we don't put dots in the western states.
            if shapedict['NAME'] == 'Hawaii' and float(shapedict['AREA']) > ATOLL_CUTOFF:
                seg = list(
                    map(lambda xy: (xy[0] + 5200000, xy[1]-1400000), seg))
                poly = Polygon(
                    seg, facecolor=data['Hawaii'][4], edgecolor='black', linewidth=.5)
                ax.add_patch(poly)
            # Alaska is large. Rescale it.
            elif shapedict['NAME'] == 'Alaska':
                seg = list(
                    map(lambda xy: (0.35*xy[0] + 1100000, 0.35*xy[1]-1300000), seg))
                poly = Polygon(
                    seg, facecolor=data['Alaska'][4], edgecolor='black', linewidth=.5)
                ax.add_patch(poly)
        statename = shapedict['NAME']
        # skip Puerto Rico.
        if statename not in ['Puerto Rico']:
            colors[statename] = data[statename][4]
        statenames.append(statename)
    # cycle through state names, color each one.
    for nshape, seg in enumerate(m.states):
        # skip DC and Puerto Rico.
        if statenames[nshape] not in ['Puerto Rico']:
            color = rgb2hex(colors[statenames[nshape]])
            poly = Polygon(seg, facecolor=color, edgecolor='black')
            ax.add_patch(poly)
    plt.title(title)
    plt.show()

# report findings
if (results_tallies[0]):
    print("Biden wins: " + str(results_tallies[0]))
if (results_tallies[1]):
    print("Trump wins: " + str(results_tallies[1]))
if (results_tallies[2]):
    print("Tied: " + str(results_tallies[2]))
