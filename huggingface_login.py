import subprocess
# Replace 'your_token_here' with your Hugging Face token
token = 'your_token_here'

def configure_huggingface_token(token):
    """
    Configure Hugging Face CLI with a token programmatically.
    :param token: Hugging Face access token as a string.
    """
    try:
        # Set the token in Hugging Face CLI configuration
        subprocess.run(
            ["huggingface-cli", "login", "--token", token]
        )
        print("Login successful! Hugging Face CLI is now configured.")
    except subprocess.CalledProcessError as e:
        print("Error during login:")
        print(e.stderr)

configure_huggingface_token(token)

