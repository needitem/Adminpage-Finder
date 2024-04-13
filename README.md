# Admin Finder

This Python script is designed to find the admin page of a given website using a wordlist.

## Usage

1. Place the `wordlist.txt` file in the same directory as the script.
2. Open the script in a Python environment.
3. Run the script.

The script will attempt to find the admin page by appending each word from the `wordlist.txt` file to the base URL and checking the response status. If a 200 or 302 status code is returned, the script will print the URL of the admin page.

## Requirements

- Python 3.x
- `http.client` and `urllib.parse` modules

## Code Explanation

1. The script imports the necessary modules: `sys`, `http.client`, `socket`, and `urllib.parse`.
2. The script opens the `wordlist.txt` file and reads the contents into a list called `wordlist`.
3. The `site` variable is set to the base URL of the website to be tested.
4. The `AdminFinder` class is defined, which contains the `adminLocate()` method.
5. The `adminLocate()` method iterates through the `wordlist` and constructs the admin page URL by joining the base URL and the current word from the list.
6. The script checks the response status for the constructed URL using either an `HTTPSConnection` or `HTTPConnection` object, depending on the URL scheme.
7. If the response status is 200 (OK) or 302 (Redirect), the script prints the URL of the admin page.
8. If the response status is 404 (Not Found) or 410 (Gone), the script prints a message indicating that the admin page was not found.
9. If any other error occurs, the script prints a generic error message.
10. The script includes a `try-except` block to handle keyboard interrupts and other exceptions.
11. The script checks if it is the main module and, if so, creates an instance of the `AdminFinder` class.

## Note

This script is intended for educational and research purposes only. Unauthorized access to websites or systems may be illegal in some jurisdictions. Use this script responsibly and at your own risk.
