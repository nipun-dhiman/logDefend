import replicate

def run_chatbot(prompt):
    model_path = "meta/llama-2-70b-chat"
    input_data = {"prompt": prompt}
    # api_token = 'r8_BKlGGflVnhPzMR9axL23VftE3p9IIdO2awFa1'
    # headers = {"Authorization": f"Token {api_token}"}
    output = replicate.run(model_path, input=input_data)
    
    # Combine all output items into a single string
    output_line = ' '.join(output)
    
    return output_line

# Example usage:
# prompt = "Hello, I'm a chatbot. What's your name?"
# output_line = run_chatbot(prompt)

# # Print the entire output line
# print(output_line)
# export REPLICATE_API_TOKEN=r8_BKlGGflVnhPzMR9axL23VftE3p9IIdO2awFa1

