import os
import subprocess
from dotenv import load_dotenv
load_dotenv()

class Login:
    def __init__(self):
        pass

    def configure_huggingface_token(self):
        """
        Configure Hugging Face CLI with a token programmatically.
        :param token: Hugging Face access token as a string.
        """
        self.token = os.getenv('HUGGINGFACE_TOKEN')
        try:
            # Set the token in Hugging Face CLI configuration
            subprocess.run(
                ["huggingface-cli", "login", "--token", self.token]
                )
            print("Login successful! Hugging Face CLI is now configured.")
        except subprocess.CalledProcessError as e:
            print("Error during login:")
            print(e.stderr)


def main():
    login = Login()
    login.configure_huggingface_token()

if __name__ == "__main__":
    main()
