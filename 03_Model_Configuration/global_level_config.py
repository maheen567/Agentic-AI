# Global Level Configuration
from agents import AsyncOpenAI, Agent, Runner, set_tracing_disabled, set_default_openai_client, set_default_openai_api
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
base_url=os.getenv("BASE_URL")

set_default_openai_api("chat_completions")

set_tracing_disabled(True)

external_client = AsyncOpenAI( 
    api_key=gemini_api_key, 
    base_url=base_url 
)
set_default_openai_client(external_client)

agent = Agent( 
    name = "General Assistant", 
    instructions= "You are a helpful assistant.",
    model = "gemini-2.5-flash",    # In Global Level Configuration, we set the model here.
)

res = Runner.run_sync( 
    agent, 
    "What is the result of 15 + 27 - 10?" 
)

print(res.final_output)