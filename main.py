import os
from dotenv import load_dotenv
import replicate

# Load environment variables from .env.local file
load_dotenv(dotenv_path='.env.local')

# Retrieve the API token from the environment
api_token = os.getenv("REPLICATE_API_TOKEN")

# Create a client with the API token
client = replicate.Client(api_token=api_token)

# Run the model
output = client.run(
    "black-forest-labs/flux-schnell:f2ab8a5bfe79f02f0789a146cf5e73d2a4ff2684a98c2b303d1e1ff3814271db",
    input={
        "prompt": "an olympic athlete who just won a gold medal singing the USA anthem on the podium",
        "num_outputs": 1,
        "aspect_ratio": "1:1",
        "output_format": "webp",
        "output_quality": 80
    }
)

print(output)
