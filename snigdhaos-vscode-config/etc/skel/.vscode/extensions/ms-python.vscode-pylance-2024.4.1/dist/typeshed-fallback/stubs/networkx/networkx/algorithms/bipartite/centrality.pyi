from networkx.utils.backends import _dispatch

@_dispatch
def degree_centrality(G, nodes): ...
@_dispatch
def betweenness_centrality(G, nodes): ...
@_dispatch
def closeness_centrality(G, nodes, normalized: bool = True): ...
