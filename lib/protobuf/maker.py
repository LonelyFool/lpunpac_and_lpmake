import os

def list_cc_files(path):
    cc_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.cc'):
                cc_files.append(os.path.join(root, file))
    return cc_files

def create_make_command(cc_files, cc, cflags):
    # Create the basic command
    command = f"{cc} -std=c++17 -Isrc -Iandroid -DHAVE_ZLIB=1 {cflags} -c \\\n"
    
    # Add each .cc file to the command
    command += " \\\n".join(cc_files)
    
    return command

# Replace with the path you want to search
path = 'src'
cc_files = list_cc_files(path)

# Replace with your CC and CFLAGS variables
cc = "$CC"
cflags = "${CFLAGS}"

make_command = create_make_command(cc_files, cc, cflags)

# Output the generated make command
print(make_command)
