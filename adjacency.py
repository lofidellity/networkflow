# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python
from node import Node
from nodeandlabel import NodeAndLabel


class Adjacency:
    """
    Represent an adjacency object
    """
    def __init__(self, node, *args):
        """
        ; node,listof(nodeandlabel) -> Adjacency
        """
        self.node = node
        self.successors = args[0]

    def __str__(self):
        """
        ; -> String
        """
        successors = ''
        for successor in self.successors:
            successors += "%s" % str(successor)
        return "%s successor ( %s )" % (self.node, successors)

    def __repr__(self):
        """
        ; -> String
        """
        return str(self)

    def __name__(self):
        """
        ; -> String
        """
        return "Adjancency"

    def __eq__(self, otherAdjacency):
        if self.node == otherAdjacency.node and self.successors == otherAdjacency.successors:
            return True
        else:
            return False
