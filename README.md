This file system is extremely basic and each function currently only performs the most default form of the function as seen in a typical linux shell. There are a lot of improvements and optimizations that can be made.
For the purposes of this exercise, the current functionality seems appropriate.

NOTE: The README file on github seems to be forcing items on separate lines to be bunched together. The raw/source output shows the information I am trying to convey much cleaner. My apologies for this.

ls    - Currently only lists out the files/directories within the current directory that's being accessed.
touch - Currently only creates a new file within the current directory that's being accessed.
        This will only succeed if there is not already a file with that name (caps insensitive) present in the current directory.
mkdir - Currently only supports the creation of a directory within the current directory. Function will only take 1 parameter
        which is the name. If a directory path is provided, it will simply be set as the name of the directory created and will not actually create a directory at that path.
cd    - This function is slightly more involved than the previous functions. It will change directories using the current directory as a baseline for searching. However, it
        also is able to parse a path to traverse down the file system and change to a directory outside the current directory. cd currently supports '~' for the root directory
        and '..' for the previous directory. This parsing could theoretically be used for the other functions as well to provide further functionality to them in the future.

OUTPUT:

ls
mkdir 1
mkdir 2
cd 1
mkdir 1-1
cd ..
ls   
1       Fri May 13 11:38:07 2022        Directory
2       Fri May 13 11:38:06 2022        Directory
cd 2
mkdir 2-1
mkdir 2-2
ls
2-1     Fri May 13 11:38:38 2022        Directory
2-2     Fri May 13 11:38:39 2022        Directory
cd ..
touch 1
ls
1       Fri May 13 11:38:07 2022        Directory
2       Fri May 13 11:38:34 2022        Directory
1       Fri May 13 11:38:59 2022        File
cd 1
cd ..
ls
1       Fri May 13 11:41:44 2022        Directory
2       Fri May 13 11:38:34 2022        Directory
1       Fri May 13 11:38:59 2022        File
cd 1/1-1
ls
cd ..
ls
1-1     Fri May 13 11:42:01 2022        Directory
cd ..
ls
1       Fri May 13 11:42:06 2022        Directory
2       Fri May 13 11:38:34 2022        Directory
1       Fri May 13 11:38:59 2022        File
cd 2/2-1
mkdir 2-1-1
cd ~
cd 2/2-1/2-1-1
ls
cd .
Cannot find directory . because it does not exist.
cd ..
ls
2-1-1   Fri May 13 11:42:45 2022        Directory
cd ..
ls
2-1     Fri May 13 11:42:50 2022        Directory
2-2     Fri May 13 11:38:39 2022        Directory
cd ..
ls
1       Fri May 13 11:42:06 2022        Directory
2       Fri May 13 11:42:53 2022        Directory
1       Fri May 13 11:38:59 2022        File
cd 3
Cannot find directory 3 because it does not exist.
cd 1/1-2
Cannot find directory 1/1-2 because it does not exist.
cd ../../../..
ls
1       Fri May 13 11:42:06 2022        Directory
2       Fri May 13 11:42:53 2022        Directory
1       Fri May 13 11:38:59 2022        File
mkdir 1
Directory not created as a directory with the same name already exists in the current directory.
touch 1
File not created as a file with the same name already exists in the current directory.
cd 1
ls
1-1     Fri May 13 11:42:01 2022        Directory
cd /2/2-1
ls
2-1-1   Fri May 13 11:42:45 2022        Directory

If you'd like to run this test, here are the command line by line that can be thrown into a bash file and piped as user input:
ls
mkdir 1
mkdir 2
cd 1
mkdir 1-1
cd ..
ls 
cd 2
mkdir 2-1
mkdir 2-2
ls
cd ..
touch 1
ls
cd 1
cd ..
ls
cd 1/1-1
ls
cd ..
ls
cd ..
ls
cd 2/2-1
mkdir 2-1-1
cd ~
cd 2/2-1/2-1-1
ls
cd .
cd ..
ls
cd ..
ls
cd ..
ls
cd 3
cd 1/1-2
cd ../../../..
ls
mkdir 1
touch 1
cd ~
cd 1
ls
cd /2/2-1

This test demonstrates everything that the basic filesystem can do. It shows that touch creates a file and mkdir creates a directory within the current directory. It also shows that there can be a file and directory with the same name, but that the file system
errors when it tries to create a new file/directory with the same name of one that already exists within the current_directory. It also displays ls and the information that it shows (which is a little more than the traditional ls in linux shows by default).
I wanted ls to display more information for demo purposes. This also shows that cd has the functionality to go up to a parent_directory as well as return to the root. It also shows (near the end of the demo output) that the filesystem can take the absolute path.