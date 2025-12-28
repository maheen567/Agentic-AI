import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("BASE_URL")

gemini_client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= gemini_base_url
)

gemini_model = OpenAIChatCompletionsModel(
    model = "gemini-2.5-flash",
    openai_client = gemini_client
)
recipe_agent = Agent(
    name = "RecipeBot",
    instructions = 
    """ You are a helpful recipe assistant. A user will give you a few ingredients
    they have at home, and you will suggest one simple and quick recipe using only those items.Keep it short, step-by-step, and easy for beginners to cook.""",
    model = gemini_model,
)

ingredients = "eggs, tomatoes, onion, bread"
result = Runner.run_sync(
    recipe_agent,
    input="I have the following ingredients: " + ingredients + ". What can I cook with them?"
)
print(result)