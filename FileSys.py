import datetime
from re import L

root = None
current_dir = None

class Node:
    # Class generalized to "Node" to allow for additions such as files which arent directories

    # A basic file/directory needs a name and a timestamp indicator
    def __init__(self, name = None, prev_dir = None):
        self.name = name
        self.prev_dir = prev_dir
        self.access_timestamp = datetime.datetime.now()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        return not self == other

class File(Node):
    def __init__(self, name):
        # Inherit all methods and properties from the Node class
        super().__init__(name)

class Directory(Node):
    def __init__(self, name):
        # Inherit all methods and properties from the Node class
        super().__init__(name)
        self.dir_contents = []

    def add_to_directory(self, item):
        self.dir_contents.append(item)

def function_ls():
    # Lists the current children directories of the directory that the user is currently in
    print(*current_dir.dir_contents, sep = "\n")

def function_cd(visited, target_dir, dir):
    if target_dir not in visited:
        visited.add(dir.name)
    for dir_child in dir.dir_contents:
        function_cd(visited, target_dir, dir_child)
    current_dir = dir
    return current_dir.name


def function_mkdir(name):
    new_dir = Directory(name)
    if new_dir not in current_dir.dir_contents:
        current_dir.add_to_directory(new_dir)
    return True

def function_touch(file_name):
    # Used to create file(s) within a directory
    new_file = File(file_name)
    if new_file not in current_dir.dir_contents:
        current_dir.add_to_directory(new_file)

def main():
    # Create root directory as the current and only directory within the filesystem on program start.
    global root
    global current_dir
    
    root = Directory("root")
    current_dir = root
    quit = False
    while(not quit):
        cmd = input().split(" ")
        function = cmd[0]
        if function == "ls":
            function_ls()
        elif function == "mkdir":
            function_mkdir(cmd[1])
        elif function == "cd":
            visited = set()
            print(function_cd(visited, cmd[1], root))
        elif function == "touch":
            function_touch(cmd[1])
        else:
            print("Unknown command provided. Please try another command.")

    

if __name__ == "__main__":
    main()