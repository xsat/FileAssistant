from tkinter import Tk, Frame, Label, Button, filedialog
from os import walk


def merge(dict1, dict2):
    print(dict1, dict2)
    return {**dict1, **dict2}


def test():
    tree = {}
    directory = filedialog.askdirectory()

    for (directory_path, directories, files) in walk(directory):
        prev = tree

        for inner_directory in directory_path.replace("\\", "/").split("/"):
            if inner_directory not in tree:
                tree[inner_directory] = {}

            tree = tree[inner_directory]

        for file in files:
            tree[file] = file

        # tree["__files__"] = files

        tree = prev

    print(tree)


if __name__ == "__main__":
    root = Tk()
    frm = Frame(root)
    frm.grid()

    Label(frm, text="Hello World!").grid(column=0, row=0)
    Button(frm, text="Quit", background="red", command=root.destroy).grid(column=1, row=0)

    Button(frm, text="Test", background="green", command=test).grid(column=0, row=1)

    root.mainloop()
