### File_To_String
# This script will take a text file and save it as a long string
# Each line will be delimited by a comma

def combine_lines_to_one():
    filename = "<input filename>"
    with open(filename,"r") as i_file:
        for ip in i_file:
            list.append(ip.rstrip())
            print(ip.rstrip())
        print(list)


def print_to_file():
    with open("combined_lines.txt","a+") as o_file:
        for item in list:
            print(item, file=o_file, end=",")


list = [];

combine_lines_to_one();
print_to_file();
