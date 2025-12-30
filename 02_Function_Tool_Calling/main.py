from agents import OpenAIChatCompletionsModel, AsyncOpenAI, Agent, Runner, function_tool, set_tracing_disabled
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
base_url=os.getenv("BASE_URL")

set_tracing_disabled(disabled=True)   # Helps to disable tracing, only needed if you are using api key other than OpenAI

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.5-flash",
    openai_client=external_client
)

# Using python function as a tool in the agent
@function_tool
def add(a: int, b: int):
    """This is a plus function that adds two numbers. Use this tool for addition operations."""
    return a + b

@function_tool
def sub(a: int, b: int):
    """This is a subtract function that subtract two numbers. Use this tool for subtraction."""
    return a - b

math_agent = Agent(
    name = "Math Assistant",
    instructions= "You are a helpful math assistant. Use tools for solving math questions. Explain answers clearly and briefly for beginners.",
    model=model,
    tools=[add, sub]     #<- Registering the tools here
)

prompt = "What is the result of 15 + 27 - 10?"
res = Runner.run_sync(
    starting_agent = math_agent,
    input = prompt
)
print(res.final_output)