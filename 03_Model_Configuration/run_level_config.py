# Run Level Configuration
from agents import OpenAIChatCompletionsModel, AsyncOpenAI, Agent, Runner, RunConfig
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
base_url=os.getenv("BASE_URL")

external_client = AsyncOpenAI( 
    api_key=gemini_api_key, 
    base_url=base_url 
)

model = OpenAIChatCompletionsModel( 
    model = "gemini-2.5-flash", 
    openai_client=external_client
)

agent = Agent( 
    name = "General Assistant", 
    instructions= "You are a helpful assistant."
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

res = Runner.run_sync(
    starting_agent = agent,
    input = "What is the result of 15 + 27 - 10?",
    run_config= config,  # In Run Level Configuration, we pass the model and client here.
)

print(res.final_output)