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
        # I chose to include the identifier as it allows for a file & directory of the same name to be present.
        self.dir_contents.append((item, item.identifier))

def search(target_dir, dir):
    global current_dir

    # Base case if the target directory is the current directory that we're in
    if dir.name == target_dir:
        current_dir = dir
        return True
    
    # Check contents of directory for the requested directory
    for dir_obj in dir.dir_contents:
        # Unpack the tuple
        obj = dir_obj[0]
        if isinstance(obj, Directory):
            if obj.name == target_dir:
                current_dir = obj
                return True
    # Deprecating the below code as it was used to recursively search for a directory.
    # For the purposes of "cd" this is not necessary. It may be necessary in the future
    # as part of a function to search possible files/directories as part of a query
    #        elif dir_child.name != target_dir:
    #            if search(target_dir, dir_child):
    #                return True

    # We did not find the requested directory.
    return False

def function_ls():
    # Lists the current objects located within the directory that the user is currently in
    for dir_obj in current_dir.dir_contents:
        # Printing the 1st part of the tuple which is the actual object itself
        print(dir_obj[0])

def function_cd(target_dir, dir):
    global current_dir

    if target_dir == "..":
        current_dir = current_dir.parent_dir
        return True

    if target_dir == "~":
        current_dir = root
        return True
    
    if not search(target_dir, dir):
        print("Cannot find directory", target_dir,"because it does not exist.")
        return False
    else:
        return True


def function_mkdir(name):
    # Creates new directory within the current directory
    global current_dir

    new_dir = Directory(name, current_dir)
    if (new_dir, "Directory") not in current_dir.dir_contents:
        # Checks if there is already a directory with the same name
        current_dir.add_to_directory(new_dir)
    else:
        print("Directory not created as a directory with the same name already exists in the current directory.")
    

def function_touch(file_name):
    # Used to create a file within the current directory
    new_file = File(file_name)
    if (new_file, "File") not in current_dir.dir_contents:
        # Checks if there is already a file with the same name
        current_dir.add_to_directory(new_file)
    else:
        print("File not created as a file with the same name already exists in the current directory.")

def main():
    # Create root directory as the current and only directory within the filesystem on program start.
    global root
    global current_dir
    
    root = Directory("root")
    current_dir = root
    while(True):
        cmd = input().split(" ")
        function = cmd[0]
        if function == "ls":
            function_ls()
        elif function == "mkdir":
            if len(cmd) > 1:
                function_mkdir(cmd[1])
            else:
                print("No parameter was given. Function was not run.")
        elif function == "cd":
            if len(cmd) > 1:
                path_list = cmd[1].split(sep = "/")
                if len(path_list) >= 1:
                    if path_list[0] == '':
                        # This means that the first part of the path following the command cd was '/' indicating an absolute path starting at the root.
                        path_list[0] = "~"
                pending_dir = current_dir
                cmd_success = True
                for path in path_list:
                    cmd_success = function_cd(path, current_dir)
                if cmd_success:
                    current_dir.access_timestamp = datetime.datetime.now()
                else:
                    current_dir = pending_dir
            else:
                print("No parameter was given. Function was not run.")
        elif function == "touch":
            if len(cmd) > 1:
                function_touch(cmd[1])
            else:
                print("No parameter was given. Function was not run.")
        elif function == "exit":
            break
        else:
            print("Unknown command provided. Please try another command.")

    

if __name__ == "__main__":
    main()