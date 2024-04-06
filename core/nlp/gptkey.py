import openai


def generate_prompt(prompt):
# Set up your OpenAI API key
    openai.api_key = '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'

    
    # Generate response
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user','content':prompt}],
        max_tokens=400,
        temperature=0.7,
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].message.content.strip()

    # Print the generated text
    
    return generated_text

