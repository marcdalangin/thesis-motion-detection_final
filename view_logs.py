from ann_visualizer.visualize import ann_viz
import graphviz
from edensenet import model

ann_viz(model, title="edensenet", filename="edensenet.gv", view=True)
graph_file = graphviz.Source.from_file("edensenet.gv")
graph_file.view()