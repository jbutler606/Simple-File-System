import datetime

root = None
current_dir = None

class Node:
    # Class generalized to "Node" to allow for additions such as files which arent directories

    # A basic file/directory needs a name and a timestamp indicator
    def __init__(self, name = None):
        self.name = name
        self.access_timestamp = datetime.datetime.now()

    def __str__(self):
        return self.name + "\t" + self.access_timestamp.strftime("%c") + "\t" + self.identifier

    def __eq__(self, other):
        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        return not self == other

class File(Node):
    # Very basic file interpretation. Allows for the ability to add things specdcific to files in the future.
    def __init__(self, name):
        # Inherit all methods and properties from the Node class
        super().__init__(name)
        self.identifier = "File"

class Directory(Node):
    # Very basic directory interpretation. Performs distinct functions from a file object, with still similar properties.
    def __init__(self, name, parent_dir = None):
        # Inherit all methods and properties from the Node class
        super().__init__(name)

        # Provides list of objects located in directory
        self.dir_contents = []
        # Provides pointer to the parent directory.
        self.parent_dir = parent_dir
        self.identifier = "Directory"

    def add_to_directory(self, item):
        self.dir_contents.append(item)

def search(target_dir, dir):
    global current_dir

    # Base case if the target directory is the current directory that we're in
    if dir.name == target_dir:
        dir.access_timestamp = datetime.datetime.now()
        current_dir = dir
        return True

    for dir_child in dir.dir_contents:
        if isinstance(dir_child, Directory):
            if dir_child.name == target_dir:
                dir_child.access_timestamp = datetime.datetime.now()
                current_dir = dir_child
                return True
            elif dir_child.name != target_dir:
                if search(target_dir, dir_child):
                    return True

    return False

def function_ls():
    # Lists the current children directories of the directory that the user is currently in
    print(*current_dir.dir_contents, sep = "\n")

def function_cd(target_dir, dir):
    global current_dir

    if target_dir == "..":
        current_dir = current_dir.parent_dir
        return

    if target_dir == "~":
        current_dir = root
        return
    
    if not search(target_dir, dir):
        print("Cannot find directory", target_dir,"because it does not exist.")


def function_mkdir(name):
    global current_dir

    new_dir = Directory(name, current_dir)
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
            function_cd(cmd[1], root)
        elif function == "touch":
            function_touch(cmd[1])
        else:
            print("Unknown command provided. Please try another command.")

    

if __name__ == "__main__":
    main()