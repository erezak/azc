from .llm_provider import LLMProvider
import anthropic



class AnthropicClient(LLMProvider):
    def __init__(self, config={}, primer=None):
        self.provider = 'anthropic'
        self.client = anthropic.Anthropic()
        self.models = self.list_models()
        self.config = config
        self.model = self.config.get("anthropic", {}).get("model", "claude-3-5-sonnet")
        self.messages = []
        self.primer = primer
          

    def list_models(self):
        """ No way to list models in anthropic? """
        return ["claude-3-5-sonnet-20240620"]
    

    def chat(self, message):
        if self.primer and len(self.messages) == 0:
            self.messages.append({"role": "user", "content": self.primer + "\n\n" + message})
        else:
            self.messages.append({"role": "user", "content": message})
        with self.client.messages.stream(
            max_tokens=1024,
            messages=self.messages,
            model=self.model,
                ) as stream:
            for text in stream.text_stream:
                yield text


    def new_chat(self, primer=None):
        self.messages = []
        if primer:
            self.primer = primer


if __name__ == "__main__": # pragma: no cover
    client = AnthropicClient(primer="Limit your response to 300 characters or less")
    for text in client.chat("I'm traveling to Madrid soon (mid-October) with my wife. We love food, history and shopping. We've been there before. Can you recommend a few destinations/activities off the beaten path? We're staying in the city center and will be there for 3 days. We're looking for authentic experiences, not tourist traps."):
        print(text, end="", flush=True)
    print()