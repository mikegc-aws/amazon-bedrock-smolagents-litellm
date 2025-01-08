from litellm import completion
import json

response = completion(
  model="bedrock/us.amazon.nova-lite-v1:0",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)

print(json.dumps(response.model_dump(), indent=2))