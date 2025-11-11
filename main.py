from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.litellm import LiteLLMProvider
from dotenv import load_dotenv
import os

load_dotenv()


def main():
    print("Hello from hello-world!")

    model = OpenAIChatModel(
        'gemini/gemini-2.5-flash-preview-09-2025',
        provider=LiteLLMProvider(
            api_base=LITELLM_GEMINI_URL,
            api_key=LITELLM_GEMINI_VIRTUAL_KEY
        )
    )
    agent = Agent(model)

    result = agent.run_sync('What is the capital of France?')
    return result

if __name__ == "__main__":
    LITELLM_GEMINI_VIRTUAL_KEY = os.environ.get("LITELLM_GEMINI_VIRTUAL_KEY","")
    LITELLM_GEMINI_URL = os.environ.get("LITELLM_GEMINI_URL","")
    print(LITELLM_GEMINI_VIRTUAL_KEY,LITELLM_GEMINI_URL)
    result = main()
    print(result.output)


