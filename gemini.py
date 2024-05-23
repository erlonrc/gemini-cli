import os.path
import argparse
import google.generativeai as genai

from dotenv import load_dotenv


def gemini(prompt: str) -> None:
    try:
        load_dotenv()
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        if os.path.splitext(prompt)[1].startswith('.'):
            print(response.text)
        else:
            print(response.text.replace('*', ''))
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
        exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Command Line Interface for Gemini.',
    )
    parser.add_argument('prompt', help='prompt for gemini')
    parser.add_argument('-f', '--file', help='file upload to gemini')
    args = parser.parse_args()

    if args.file:
        try:
            with open(os.path.abspath(args.file), 'r', encoding='utf-8') as file:
                file_content = ''.join(file.readlines())
            gemini(f'{args.prompt} {file_content}')
        except Exception as e:
            print(f'{type(e).__name__}: {e}')
            exit(1)
    else:
        gemini(args.prompt)


if __name__ == '__main__':
    main()
