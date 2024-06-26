# Gemini CLI

## Use Gemini from the Command Line

This Python script allows you to use Gemini from the command line in a simple and efficient way. You can enter a single command and receive a text response, or use the `-f` option to pass the contents of a text file along with the command.

## Requirements:

- Python 3
- Gemini API key (generated by you)

## How to Use:

1. **Get your Gemini API key:**
    Go to the [Google developer website](https://ai.google.dev/aistudio) and create an account. Once you have created your account, you will be able to generate an API key.

2. **Create a .env file in the project folder with the following content:**
    ```bash
    GEMINI_API_KEY=your_api_key
    ```

3. **Run the script:**
    ```bash
    python gemini.py <prompt> [-f <text_file>]
    ```
    - **\<prompt\>**: The command you want to run on Gemini.
    - **-f <text_file>**: (optional) The text file that contains the content you want to send to Gemini (returns text in markdown format).

## Usage Examples:

- **Translate the following text into simplified Chinese:**
    ```bash
    python gemini.py "translate the following text into simplified Chinese" -f text.txt
    ```
    In this example, the contents of the `text.txt` file will be sent to Gemini and translated into simplified Chinese.

- **Get information about a topic:**
    ```bash
    python gemini.py "summary of the movie The Godfather"
    ```
    In this example, Gemini will provide a summary of the movie "The Godfather".

## Contributions:

Feel free to contribute to this project! You can submit suggestions, bug fixes, or new features.

## License:

This project is licensed under the MIT license.

## Notes:

This file (README.md) was generated by Gemini and modified by the project developer.
