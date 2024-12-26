from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools
from dotenv import load_dotenv
import os
from constants import SYSTEM_PROMPT, INSTRUCTIONS

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API")
GOOGLE_API_KEY = os.getenv('GEMINI_API')

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API key not found in environment variables.")
if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API key not found in environment variables.")

# Construct the absolute path to image
# make sure 'images' folder is in the same directory as the script
image_path = os.path.join(os.path.dirname(__file__), "images", "lays.jpg")

# Verify that image file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file not found at: {image_path}")

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp", api_key=GOOGLE_API_KEY),  # Explicitly pass the API key here
    tools=[TavilyTools(TAVILY_API_KEY)],
    markdown=True,
    system_prompt=SYSTEM_PROMPT,
    instructions=INSTRUCTIONS,
)


try:
    agent.print_response(
        "Analyze the product image",
        images=[image_path],
        stream=True,
    )
except Exception as e:
    print(f"An error occurred: {e}")