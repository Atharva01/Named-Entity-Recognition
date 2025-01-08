import subprocess
import argparse

class Login:
    def __init__(self):
        pass

    def configure_huggingface_token(self,token):
        """
        Configure Hugging Face CLI with a token programmatically.
        :param token: Hugging Face access token as a string.
        """
        self.token = token
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
    parser = argparse.ArgumentParser(description="Hugging Face login thorugh CLI")
    parser.add_argument('--token',type=str,help='Your Hugging Face Access Token')
    args = parser.parse_args()
    login = Login()
    login.configure_huggingface_token(args.token)

if __name__ == "__main__":
    main()
