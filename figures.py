# FOR CREATING VARIOUS PLOTLY FIGURES
# ===================================

# LIBRARIES AND MODULES
# ----------------------
import plotly.graph_objects as charts
import plotly.offline as offline

# FUNCTIONS

def testChart():
    """Creates a Sankey chart for testing

    Returns:
        obj: plotly figure object
    """
    # An HTML file for saving the plot when offline
    htmlFileName = 'meatstreams.html'

    # Labels for the sankey chart (from a view)
    sourceLabels = ['Hirvi', 'Peura'] # Where the meat is coming from
    targetLabels = ['Ryhmä 1', 'Ryhmä 2', 'Ryhmä 3'] # Which group has received meat
    allLabels = sourceLabels + targetLabels # All labels for the chart in a single list

    # Simulation Data (list of tuples), in reality the data should come from the database view 
    dBdata = [('Hirvi', 'Ryhmä 1', 100),
        ('Hirvi', 'Ryhmä 2', 200),
        ('Hirvi', 'Ryhmä 3', 100),
        ('Peura', 'Ryhmä 2', 50)
        ]

    # Define colors for meat sources (animals) -> for sending nodes ie. left side boxes in the chart
    sourceNodeColors = ['rgba(128, 128, 128, 0.75)', 'rgba(150, 50, 0, 0.75)' ] # Alpha (opacity) 0 - 1 

    # Define colors for meat targets (group) -> for receiving nodes ie. right side boxes in the chart
    targetNodeColors = ['red', 'orange', 'green'] # CSS named colors

    # All label colors in a single list for the chart
    allColors = sourceNodeColors + targetNodeColors 

    # Empty lists for label indexes and values
    sankeySources = []
    sankeyTargets = []
    sankeyValues = []

    # Create indexes for the Sankey chart
    for row in dBdata:
        tupleSource = row[0]
        tupleTarget = row[1]
        tupleValue = row[2]
        sourceIx = allLabels.index(tupleSource)
        targetIx = allLabels.index(tupleTarget)
        sankeySources.append(sourceIx)
        sankeyTargets.append(targetIx)
        sankeyValues.append(tupleValue)

    figure = charts.Figure(data=[charts.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = allLabels,
            color = allColors
        ),
        link = dict(
            source = sankeySources, 
            target = sankeyTargets,
            value = sankeyValues,
            color = 'rgba(255, 128, 0, 0.5)'
    ))])

    figure.update_layout(title_text="Lihanjakotilanne", font_size=16)
    # figure.update_traces(orientation='v', selector=dict(type='sankey'))
    offline.plot(figure, filename= htmlFileName) # Write the chart to an html file
    

def createSankeyChart(dBData, sourceColors, targetColors, linkColors, heading):
    """Creates a Sankey chart from database data

    Args:
        dBData (list): List of tuples (source, target, value)
        sourceColors (list): list of CSS colors or rgba values
        targetColors (list): list of CSS colors or rgba values
        linkColors (list): list of CSS colors or rgba values
        heading (str): A heading for the chart

    Returns:
        obj: plotly figure
    """
    # Labels for the sankey chart (from dBData)
    
    allLabels = [] # All sources and targets in a single list <- dBdata
    

    

    # Define colors for meat sources (animals) -> for sending nodes ie. left side boxes in the chart
    sourceNodeColors = sourceColors # Alpha (opacity) 0 - 1 

    # Define colors for meat targets (group) -> for receiving nodes ie. right side boxes in the chart
    targetNodeColors = targetColors # CSS named colors

    # All label colors in a single list for the chart
    allColors = sourceNodeColors + targetNodeColors 

    # Empty lists for label indexes and values
    sankeySources = []
    sankeyTargets = []
    sankeyValues = []

    # Create indexes for the Sankey chart
    for row in dBData:
        tupleSource = row[0]
        tupleTarget = row[1]
        tupleValue = row[2]
        sourceIx = allLabels.index(tupleSource)
        targetIx = allLabels.index(tupleTarget)
        sankeySources.append(sourceIx)
        sankeyTargets.append(targetIx)
        sankeyValues.append(tupleValue)

    print(sankeySources)

    figure = charts.Figure(data=[charts.Sankey(
            node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = allLabels,
            color = allColors
        ),
        link = dict(
            source = sankeySources, 
            target = sankeyTargets,
            value = sankeyValues,
            color = linkColors
    ))])

    figure.update_layout(title_text=heading, font_size=16)
    # figure.update_traces(orientation='v', selector=dict(type='sankey'))
    return figure
    
def createOfflineFile(figure, htmlFileName):
    """Creates an html file from the chart for offline use
    Args:
        figure (obj): The chart to bring offline
        htmlFileName (str): name of the file to save into disk
    """
    offline.plot(figure, filename=htmlFileName) # Write the chart to an html file