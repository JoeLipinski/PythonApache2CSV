import re
import pandas as pd
import argparse

def parse_apache_log(log_file_path, csv_output_path):
    # Define regex patterns for Combined and Common Log Format
    combined_pattern = re.compile(r'(?P<ip>\S+) - (?P<user>\S+) \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<resource>\S+) HTTP/(?P<http_version>\S+)" (?P<status>\d+) (?P<size>\S+) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"')
    clf_pattern = re.compile(r'(?P<ip>\S+) - (?P<user>\S+) \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<resource>\S+) HTTP/(?P<http_version>\S+)" (?P<status>\d+) (?P<size>\S+)')
    
    # Initialize list to hold parsed data
    parsed_logs = []
    
    # Open and parse the log file
    with open(log_file_path, 'r') as file:
        for line in file:
            # Try to match with Combined Log Format pattern first
            match = combined_pattern.match(line)
            if not match:
                # Fallback to Common Log Format pattern
                match = clf_pattern.match(line)
            
            # If a pattern matches, add the parsed data to the list
            if match:
                log_data = match.groupdict()
                # Convert size field from '-' to 0 for cases where size is unavailable
                if log_data['size'] == '-':
                    log_data['size'] = 0
                parsed_logs.append(log_data)
            else:
                # Log or handle lines that couldn't be parsed
                print(f"Unable to parse line: {line}")

    # Create a DataFrame from parsed logs and save to CSV
    df_logs = pd.DataFrame(parsed_logs)
    df_logs.to_csv(csv_output_path, index=False)
    print(f"Log data successfully parsed and saved to {csv_output_path}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Parse an Apache log file into CSV format.")
    parser.add_argument("input_file", help="Path to the Apache log file to be parsed")
    parser.add_argument("output_file", help="Path to save the parsed CSV file")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Run the log parsing function with command-line arguments
    parse_apache_log(args.input_file, args.output_file)
