# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab
#!/usr/bin/env python

class NodeAndLabel:
    """
    Represents a node and label
    """
    def __init__(self, node, label1, label2):
        self.node = node
        self.label1 = label1
        self.label2 = label2

    def __str__(self):
        return (str(self.node), self.label1, self.label2)