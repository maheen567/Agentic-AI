# Agent Level Configuration

from agents import OpenAIChatCompletionsModel, AsyncOpenAI, Agent, Runner, set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
base_url=os.getenv("BASE_URL")

set_tracing_disabled(disabled=True)

external_client = AsyncOpenAI( 
    api_key=gemini_api_key, 
    base_url=base_url
)

model= OpenAIChatCompletionsModel( 
    model = "gemini-2.5-flash", 
    openai_client=external_client
)

agent = Agent( 
    name = "General Assistant", 
    instructions= "You are a helpful assistant.", 
    model=model # In Agent Level Configuration, we pass the model here.
)

res = Runner.run_sync(
    starting_agent = agent,
    input = "Tell me about recursion in programming.",
)

print(res.final_output)