import pathlib
import sys

test_root = pathlib.Path(__file__).parent
sys.path.insert(0, str(test_root.parent / "src"))
sys.path.insert(0, str(test_root))
