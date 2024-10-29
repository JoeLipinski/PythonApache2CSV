# PythonApache2CSV
PythonApache2CSV is a Python script designed to parse Apache log files in both Common Log Format (CLF) and Combined Log Format (which includes User-Agent and Referrer details). The script processes the log file and outputs the data in a well-structured CSV file. This parser is flexible, handling different Apache log formats and providing meaningful defaults for missing data.

## Features
- Parses both Common Log Format (CLF) and Combined Log Format
- Outputs parsed data into a CSV file with clear column names
- Handles missing data fields gracefully
- Provides command-line arguments for specifying input and output file paths

## Requirements
- Python 3.x
- `pandas` library for DataFrame operations
- `argparse` for handling command-line arguments

Install `pandas` if you haven't already:

```bash
pip install pandas
```

## Usage
To run the script, use the following syntax:

```bash
python apache2csv.py <input_file> <output_file>
```

### Arguments
- `<input_file>`: Path to the Apache log file you want to parse.
- `<output_file>`: Path where the resulting CSV file will be saved.

## CSV Output
The resulting CSV file will have the following columns:

- **ip**: IP address of the client
- **user**: User identifier (typically `-` if not set)
- **datetime**: Date and time of the request
- **method**: HTTP method (GET, POST, etc.)
- **resource**: Requested resource or URL path
- **http_version**: HTTP version (e.g., 1.0 or 1.1)
- **status**: HTTP status code returned by the server
- **size**: Size of the response in bytes (or `0` if unavailable)
- **referrer**: Referring URL (in Combined Log Format)
- **user_agent**: Client’s user agent string (in Combined Log Format)

## Error Handling
- Lines that do not match either format are printed to the console for inspection, allowing you to address inconsistencies.
- Missing or `-` values in the `size` column are set to `0` to avoid issues in downstream data processing.

## Example Log Format
Here’s an example of what Common and Combined Log Formats look like:

- **Common Log Format (CLF):**
  ```
  127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
  ```

- **Combined Log Format:**
  ```
  127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"
  ```

## Development
To extend this parser or adjust for other log formats, you can modify the regex patterns used in the script:

```python
combined_pattern = re.compile(r'...')
clf_pattern = re.compile(r'...')
```

## License

This project is open-source and available under the MIT License.

## Contributions
Feel free to submit issues or pull requests. Contributions are welcome!
