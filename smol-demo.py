# Modified from https://huggingface.co/blog/smolagents

from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

model = LiteLLMModel(model_id="bedrock/us.amazon.nova-lite-v1:0")

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
