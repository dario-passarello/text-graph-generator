from graphviz import Digraph


def build_graph(node_struct: dict):
    graph = Digraph(comment=node_struct["name"])
    for i, node in enumerate(node_struct["nodes"]):
        graph.node(node)
    for i, node in enumerate(node_struct["edges"]):
        graph.edge(node[0], node[1])
    return graph


def render_graph(graph: Digraph, out_filename: str = "out/out"):
    graph.render(out_filename, view=True)
