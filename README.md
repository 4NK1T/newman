# Newman Report Redaction Script

This Python script takes a Newman report file as input and generates a new file with all sensitive information redacted. This is useful for security purposes as it prevents the exposure of pre-production and production credentials and other PII (personally identifiable information) to unauthorized personnel.

## Prerequisites

Python 3.x <br>
Newman report file in HTML format

## Usage

To use this script, follow these steps: <br>

1. Clone this repository to your local machine using git clone https://github.com/4nk1t/newman/ <br>
2. Navigate to the repository folder using cd newman-report-redaction <br>
3. Install the required packages using pip install -r requirements.txt <br>
4. Run the script using python3 script.py -i inputfile.html -o outputfile.html <br>
5. Replace inputfile.html with the name of your Newman report file, and outputfile.html with the desired name of your redacted report file. <br>

## Configuration

This script uses an array called parameters to specify which sensitive parameters should be redacted. You can modify this array by editing the script.py file and adding or removing parameters as needed.

## Contributing

If you find any issues with this script or would like to suggest improvements, please feel free to open a new issue or submit a pull request.
