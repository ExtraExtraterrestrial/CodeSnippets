from pathlib import Path
from json import dumps

### Tree.tree is a json of files within dir
class Tree():
    def __init__(self, folderName: str):
        self.target     = Path(folderName)
        self.tree       = self.make_json_tree(self.target)
 
    def make_json_tree(self, folder: Path):
        tree = {folder.name : []}
        for file in folder.iterdir():
            if file.is_dir():
                tree[folder.name].append([self.make_json_tree(file)])
            else:
                tree[folder.name].append(file.name)
        return tree

    def __str__(self):
        return dumps(self.tree, indent = 2)


if __name__ == '__main__':
    tree = Tree(r"..")
    print(tree)
