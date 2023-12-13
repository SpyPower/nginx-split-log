import re
import sys
import os

# Read the input file name from the command line argument
input_file = sys.argv[1]

# Loop through each line in the input file
with open(input_file, 'r') as f:
    for line in f:
        # Extract the date from the line using a regular expression
        match = re.search(r'\[([0-9]{2})/([A-Za-z]{3})/([0-9]{4}):', line)
        if match:
            day = match.group(1)
            month = match.group(2)
            year = match.group(3)
            # Convert the month name to a number
            month_dict = {
                "Jan": "01",
                "Feb": "02",
                "Mar": "03",
                "Apr": "04",
                "May": "05",
                "Jun": "06",
                "Jul": "07",
                "Aug": "08",
                "Sep": "09",
                "Oct": "10",
                "Nov": "11",
                "Dec": "12"
            }
            month_num = month_dict[month]
            # Create the output file name
            output_file = f"{year}-{month_num}-{day}.log"
            # Create folder for the results

            if not os.path.exists("./resultsPy"):
                os.makedirs("./resultsPy")
            # Check if the line starts with an IP address
            if re.match(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', line):
                # Append the line to the output file
                with open(f"./resultsPy/{output_file}", 'a') as out_f:
                    out_f.write(line)
            else:
                # Append the line to the unknown file
                with open("./resultsPy/unknown.log", 'a') as unknown_f:
                    unknown_f.write(line)
        else:
            # Append the line to the unknown file if date is not between the brackets
            with open("./resultsPy/unknown.log", 'a') as unknown_f:
                unknown_f.write(line)
