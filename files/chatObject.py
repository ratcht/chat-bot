class ChatObject:
  def __init__(self, prompt, response):
    self.prompt = prompt
    self.response = response

  def get_prompt(self, prompt):
    return prompt
  
  def get_response(self, response):
    return response