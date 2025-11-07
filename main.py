def main():
    print("Hello from hello-world!")

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.litellm import LiteLLMProvider

model = OpenAIChatModel(
    'gemini/gemini-2.5-flash-preview-09-2025',
    provider=LiteLLMProvider(
        api_base='http://localhost:4000/',
        api_key='sk-UD9zG2pjPEzIs6M865L_Gw'
    )
)
agent = Agent(model)

result = agent.run_sync('What is the capital of France?')
print(result.output)
#> The capital of France is Paris.
...
if __name__ == "__main__":
    main()


  git config --global user.email "kumarsuraj9450@gmail.com"
  git config --global user.name "Kumar Suraj"
