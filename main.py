import os

from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env file


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("GROQ_API_KEY"))
    print(os.environ.get("OPENAI_API_KEY"))
    print(os.environ.get("GOOGLE_API_KEY"))


if __name__ == "__main__":
    main()
