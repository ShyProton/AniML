from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

from animl.tree import DecisionTree

from manim import Scene, Create
from manim.utils.commands import capture

# testing by running the TreeTest class using manim
def test_tree():
    scene_path = 'tests/test_tree.py'
    scene_name = 'TreeTest'
    test_output = 'tests/media'

    command = [
        'python3',
        '-m',
        'manim',
        scene_path,
        scene_name,
        '-pqh',
        '--media_dir',
        test_output
    ]

    out, err, exit_code = capture(command)

    print(out)

    assert exit_code == 0, err

class TreeTest(Scene):
    def construct(self):
        max_depth = 5
        tree = DecisionTreeClassifier(random_state=0, max_depth=max_depth)
        iris = load_iris()

        tree.fit(iris.data, iris.target)

        tree_manim = DecisionTree(tree, node_radius=0.16, node_spacing=0.5, layer_spacing=1)
        assert tree_manim.tree_depth == max_depth

        self.play(Create(tree_manim, run_time=5.0))
        self.wait()

        self.clear()

        self.play(Create(DecisionTree(tree, show_keys=True)), run_time=1.0)
        self.wait()

