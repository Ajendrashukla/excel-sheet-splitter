# excel-sheet-splitter
# Excel Sheet Splitter

Excel Sheet Splitter is a web application built with Flask that allows you to upload an Excel file, split its sheets into individual Excel files, and save them in a designated folder. It also returns links to the split files after the process. This project is designed to fulfill the requirements of splitting Excel sheets into separate files using a Python interface, receiving input in JSON format for POST submissions, and returning output in JSON format.

## Features

- Upload an Excel file.
- Split the sheets of the Excel file into separate Excel files.
- Save the split files in a designated folder.
- Display links to the split files.

## Installation and Setup

1. Clone the repository:

2. Create a virtual environment and activate it
   
3. Install the required packages:

4. Run the Flask application:


## Usage

1. Access the web application by navigating to `http://localhost:5000` in your web browser.

2. Click the "Choose Excel File" button and select an Excel file to upload.

3. Click the "Split Sheets" button to split the sheets into individual Excel files.

4. The output to the split files will be displayed in the directory "project\app\static\split_files"
   you can change it in the app

## Contributing

Contributions are welcome! If you find any issues or want to improve the project, feel free to create a pull request.


*This project was created as part of a demonstration. It might not cover all production-level considerations.*

