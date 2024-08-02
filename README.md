# Selenium Web Automation Script

This repository contains a Selenium WebDriver script written in Python to automate the process of logging into a web application, navigating to a specific section, uploading a file, and taking a screenshot of the result. 

## Features
- Automated login to the web application.
- Navigation to the "Orders" section.
- Bulk order file upload.
- Validation of the uploaded file.
- Capture and save a screenshot of the result.

## Requirements
- Python 3.x
- Chrome WebDriver
- Selenium library

## Setup
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/HasanRaihan2000/selenium-web-automation.git
    ```
2. **Install Dependencies**:
    ```sh
    pip install selenium
    ```
3. **Download Chrome WebDriver**:
    - Ensure that the Chrome WebDriver version matches your Chrome browser version.
    - Download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system PATH.

## Usage
1. **Prepare the File for Upload**:
    - Ensure that `demo-data.xlsx` is placed in the specified directory: `demo-data.xlsx`.

2. **Run the Script**:
    ```sh
    python script.py
    ```

3. **Script Actions**:
    - The script will navigate to the login page of the web application.
    - Enter the username and password.
    - Navigate to the "Orders" section and attempt to upload the specified file.
    - Validate the upload and take a screenshot of the result.

## File Structure
- `script.py`: The main automation script.

## Screenshots
- Screenshots are saved in the `screenshots` folder with a timestamp.

## Note
- Ensure the element locators (like class names and XPaths) used in the script match the current structure of the web application. Update them if necessary.

## Contributing
Feel free to submit issues or pull requests for any improvements or additional features.

## License
This project is licensed under the MIT License.

