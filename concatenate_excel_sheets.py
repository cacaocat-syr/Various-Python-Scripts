import xlrd
import os

### Create Directory to hold output file(s)
# if the directory already exists, skip
output_directory = "combined_sheet"
try:
    os.mkdir(output_directory)
except:
    print("Directory already exists. Continuing...")


### Get all sheets from input directory
def get_names_of_files():
    sheets_location = "sheets"                                          # If excel sheets are in a directory
    for file in os.listdir(sheets_location):
        if os.path.isfile(os.path.join(sheets_location, file)):
            #print(file)
            sheet_names.append("./" + sheets_location + "/" + file)
    print(sheet_names)

### Read first sheet of each workbook and append all rows excluding the first
def pull_first_sheet():
    for workbook in sheet_names:
        wb = xlrd.open_workbook(workbook)
        sheet = wb.sheet_by_index(0)                #Refers to which sheet in the workbook
        print(workbook)
        print(sheet.nrows)
        for x in range(sheet.nrows):
            #print(x)
            if sheet.cell_value(x, 0) == "<Title>": #Ignore the first row, usually headers and titles
                continue
            datarows = []
            for y in range(10):                      #Only want to append the first 10 columns
                datarows.append(((sheet.cell_value(x, y)).replace('\n',' ').replace(',',' ')))  #To remove newlines and commas which will interfere with csv format
                # print((sheet.cell_value(x, y)).replace('\n',' ').replace(',',' '))
            datasets.append(datarows)

### Take the populated nested list and append it to a file
def print_data_to_file():
    with open("./concated_sheet/combined.csv","a+") as o_file:
        for l in datasets:
            for c in l:
                print(c + ",", file=o_file, end='')
            print("\n", file=o_file, end='')
    o_file.close()

sheet_names = [];
datasets = [];
get_names_of_files();
pull_first_sheet();
print_data_to_file();