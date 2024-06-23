import os
# root: Prints out directories only from what you specified.
# dirs: Prints out sub-directories from the root.
# files: Prints out all files from root and directories.

# iterate over files in
# that directory
directory = "/Users/valeria/src/intel/intel-basic-python-jun-24/meeting2"
for root, dirs, files in os.walk(directory):
    # for filename in files:
        print(f"""
        Root: {root}
        dirs: {dirs}
        filename: {files}""")
        # print(os.path.join(root, filename))