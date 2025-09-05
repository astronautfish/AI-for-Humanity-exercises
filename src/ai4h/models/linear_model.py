from pathlib import Path


def test():
    project_root = Path(__file__).resolve().parents[3]
    relative_path = Path(__file__).resolve().relative_to(project_root)
    print(f"Hello from `{relative_path}` <3")