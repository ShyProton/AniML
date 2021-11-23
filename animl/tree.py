from typing import Union

from sklearn.tree import BaseDecisionTree

from manim import VGroup, VDict, Mobject
from manim import Circle, Line
from manim import GREEN
from manim import DOWN, LEFT, RIGHT

class DecisionTree(VDict):
    """
    Manim representation of a simple Decision Tree using an Sklearn tree as reference

    Attributes:
        decision_tree: Copy of the sklearn Decision Tree passed into the constructor
        tree_depth: Depth of the Decision Tree (number of layers)
    """

    def __init__(
        self,
        tree: BaseDecisionTree,
        node_radius: float = 0.1,
        node_spacing: float = 1,
        layer_spacing: float = 1,
        color: str = GREEN,
        **kwargs
    ):
        """
        Initializes DecisionTree using an Sklearn Decision Tree

        Args:
            tree: Sklearn Decision Tree to draw reference from for creating the tree representation
            node_radius: Radius of each node composing the Decision Tree
            node_spacing: Spacing between nodes on the last layer
                [1 = 1 node space between nodes]
            layer_spacing: Spacing between layers
                [1 = 1 node space betwen layers]
            color: Color of the decision tree
        """

        self.decision_tree = tree
        self.tree_depth = self.decision_tree.get_depth()

        pairs = self._build_tree_layers(node_radius, node_spacing, layer_spacing, color)
        super().__init__(pairs, **kwargs)

    def _build_tree_layers(
        self,
        radius: float,
        n_space_factor: float,
        v_space_factor: float,
        color: str,
    ) -> list[tuple[int, Union[VGroup, Mobject]]]:
        # stores key-value pairs of VGroups
        pairs = []

        # keeps track of how many nodes to remove per layer traversed
        removed = 0

        # iterating from the bottom layer to the top layer
        for layer in range(self.tree_depth - 1, -1, -1):
            # group of Mobjects to store all nodes for the current layer
            nodes = VGroup()

            # width of the layer in nodes
            layer_width = pow(2, self.tree_depth) - removed - 1

            # number of nodes in the layer
            node_count = pow(2, layer)

            # node_spacing is the space between nodes for the current layer (in nodes)
            try:
                node_spacing = (layer_width - 1) / (node_count - 1)
            except ZeroDivisionError as _:
                # set to zero when we are at the top layer
                node_spacing = 0

            for node in range(node_count):
                # add a new node to the node group
                nodes += (
                    Circle(radius=radius, color=color)
                    # sets the spacing of the nodes correctly
                    .shift((RIGHT * radius * 2) * (node * node_spacing) * n_space_factor)
                    # shifts the layer to the left to position it correctly
                    .shift((LEFT * radius * 2) * (layer_width / 2) * n_space_factor)
                    # moves the layer down depending on the layer
                    .shift((DOWN * radius * 2) * (layer * 2) * v_space_factor)
                )

            # the number of nodes that will be removed for the next layer up is updated
            removed = removed * 2 + 2

            # append the node group to the pair list
            pairs.append((layer, nodes))

        # TODO: Add lines between layers

        # return the pairs in reverse order since we constructed it from bottom up
        return pairs[::-1]

