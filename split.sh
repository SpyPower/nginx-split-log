#!/bin/bash

# Read the input file name from the command line argument
input_file=$1

# Loop through each line in the input file
while read line; do
  # Extract the date from the line using a regular expression
  if [[ $line =~ \[([0-9]{2})/([A-Za-z]{3})/([0-9]{4}): ]]; then
    day=${BASH_REMATCH[1]}
    month=${BASH_REMATCH[2]}
    year=${BASH_REMATCH[3]}
    # Convert the month name to a number
    case $month in
    "Jan") month_num="01" ;;
    "Feb") month_num="02" ;;
    "Mar") month_num="03" ;;
    "Apr") month_num="04" ;;
    "May") month_num="05" ;;
    "Jun") month_num="06" ;;
    "Jul") month_num="07" ;;
    "Aug") month_num="08" ;;
    "Sep") month_num="09" ;;
    "Oct") month_num="10" ;;
    "Nov") month_num="11" ;;
    "Dec") month_num="12" ;;
    esac
    # Create the output file name
    output_file="$year-$month_num-$day.txt"
    mkdir -p ./results
    # Check if the line starts with an IP address
    if [[ $line =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ ]]; then
      # Append the line to the output file
      echo $line >>./results/$output_file
    else
      # Append the line to the unknown file
      echo $line >>./results/unknown.txt
    fi
  else
    # Append the line to the unknown file if date is not between the brackets
    echo $line >>./results/unknown.txt
  fi
done <$input_file
