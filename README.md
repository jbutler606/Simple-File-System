This file system is extremely basic and each function currently only performs the most default form of the function as seen in a typical linux shell.

ls    - Currently only lists out the files/directories within the current directory that's being accessed.
touch - Currently only creates a new file within the current directory that's being accessed.
        This will only succeed if there is not already a file with that name (caps insensitive) present in the current directory.
mkdir - Currently only supports the creation of a directory within the current directory. Function will only take 1 parameter
        which is the name. If a directory path is provided, it will simply be set as the name of the directory created and will not actually create a directory at that path.
cd    - This function is slightly 