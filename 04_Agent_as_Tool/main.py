from agents import OpenAIChatCompletionsModel, AsyncOpenAI, Agent, Runner, set_tracing_disabled
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
base_url=os.getenv("BASE_URL")

set_tracing_disabled(disabled=True)

external_client = AsyncOpenAI(
    api_key=groq_api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    model = "llama-3.1-8b-instant",
    openai_client=external_client,
)

chinese = Agent(
    name="Chinese agent",
    instructions="You translate the user's message to Chinese",
)

german = Agent(
    name="German agent",
    instructions="You translate the user's message to German",
)

# Using agents as tools
translate_to_german = german.as_tool(
    tool_name="translate_to_german",
    tool_description="Use this tool to translate the user's message to German",
)
translate_to_chinese = chinese.as_tool(
    tool_name="translate_to_chinese",
    tool_description="Use this tool to translate the user's message to Chinese",
)

agent = Agent(
    name="General Agent",
    instructions="You are a general assistant. Always use the tools to translate the user's message",
    model=model,
    tools=[translate_to_german, translate_to_chinese] #Registering tools here
)

async def main():
    prompt = "Translate 'Hello, how are you?' to German and Chinese"
    res = await Runner.run(
        starting_agent = agent,
        input = prompt
    )
    print(res.final_output)
if __name__ == "__main__":
    asyncio.run(main())
