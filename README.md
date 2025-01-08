# smolagents and LiteLLM Demos with Amazon Bedrock

This repository demonstrates how to use Hugging Face's smolagents and LiteLLM's model abstraction with Amazon Bedrock's language models. These examples show how to leverage these libraries for both agent-based interactions (Bedrock + smolagents + LiteLLM) and direct model access (Bedrock + LiteLLM).

## Prerequisites

- Python 3.8+
- AWS account with Bedrock access
- AWS credentials configured locally

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Ensure AWS credentials are properly configured in `~/.aws/credentials` or via environment variables:
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-west-2
```

2. The provided configuration uses:
- Model: bedrock/us.amazon.nova-lite-v1:0
- Region: us-west-2 (or whatever is in `AWS_DEFAULT_REGION`)

## Project Structure

- `smol-demo.py`: Example using SmoL Agents with Bedrock
- `litellm-demo.py`: Basic example of using LiteLLM with Bedrock
- `x-bonus-litellm-bedrock-openai-demo.py`: Advanced LiteLLM example with OpenAI-compatible interface

## Usage Examples

### smolagents Integration
The primary demo shows how to create an agent with search capabilities using smolagents. The code was taken and adapted from Hugging Face's great blog post here: https://huggingface.co/blog/smolagents

```python:smol-demo.py
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

model = LiteLLMModel(model_id="bedrock/us.amazon.nova-lite-v1:0")
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
```

This example demonstrates:
- Integration with Amazon Bedrock's Nova model
- Use of smolagents' simple CodeAgent for complex reasoning

### Basic LiteLLM Usage
The smolagents library introduced me to LiteLLM (https://www.litellm.ai/). LiteLLM provides an SDK and/or a proxy enabling you to access 100's of different LLMs from different providers all via an OpenAI compatible interface. Here is a simple completion example using LiteLLM with Bedrock's Nova model:

```python:litellm-demo.py
from litellm import completion
import json

response = completion(
  model="bedrock/us.amazon.nova-lite-v1:0",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

### Advanced LiteLLM Features
As a bonus demo, here is sample code from OpenAI with minimal changes working with Amazon Bedrock. This shows OpenAI-compatible streaming and non-streaming completions from Amazon Bedrock's Nova models.

`x-bonus-litellm-bedrock-openai-demo.py`

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
