import anthropic
import random
import re

# Initialize client
client = anthropic.Anthropic()

# BOTEC questions list
questions = [
    "How many piano tuners are there in a city like New York?",
    "What is the total weight of the atmosphere above a single square meter of Earth's surface?",
    "How many grains of rice are consumed worldwide in a year?",
    "How much energy does it take to power all the smartphones in the world for a day?",
    "How many liters of water does it take to produce a kilogram of beef?",
    "How many basketballs would fit inside an Olympic-sized swimming pool?",
    "What is the annual global production of plastic waste per person?",
    "How many times does a person blink in their lifetime?",
    "How much area would be needed to supply the world's energy needs with solar panels?",
    "How many satellites could orbit Earth without interfering with each other?",
    "What is the total amount of data generated globally each day?",
    "How many breaths does a blue whale take in an hour?",
    "How much would all the gold ever mined fit into a single Olympic swimming pool?",
    "How many people could stand shoulder to shoulder on the island of Manhattan?",
    "What is the total distance driven by all cars in the world in a year?",
    "How much would it cost to print all the pages on the internet?",
    "How many Lego bricks have been produced since they were first made?",
    "How long would it take to count to one billion aloud without stopping?"
]

def get_random_question():
    """Get a random BOTEC question."""
    return random.choice(questions)

def prompt_user_for_botec(question):
    """Prompt the user to input their BOTEC calculation response."""
    return input(f"Write a BOTEC for the following question:\nQuestion: {question}\n\nBe as verbose in your reasoning as possible.\n")

def llm_response(prompt):
    """Generate an AI response using the provided prompt."""
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def evaluate_botec_response(question, user_response):
    """Evaluate the user's response by passing it to the AI."""
    prompt = f"""
    You are an AI assistant helping a user develop their skills in BOTEC (Back-of-the-Envelope Calculation) estimations.
    
    Evaluate the user's response based on completeness, relevance, specificity, and measurability.
    Provide feedback and assign a grade from 1 to 10.
    
    <scenario>
    {question}
    </scenario>
    
    <user_response>
    {user_response}
    </user_response>
    """
    
    # Get response from the model
    response_text = llm_response(prompt)
    
    print(response_text)
    # Extract scenario, feedback, and grade using regex
    # scenario = re.search(r"<scenario>\s*(.*?)\s*</scenario>", response_text, re.DOTALL).group(1)
    # user_resp = re.search(r"<user_response>\s*(.*?)\s*</user_response>", response_text, re.DOTALL).group(1)
    # feedback = re.search(r"<feedback>\s*(.*?)\s*</feedback>", response_text, re.DOTALL).group(1)
    # grade = re.search(r"<grade>\s*(.*?)\s*</grade>", response_text, re.DOTALL).group(1)

    # # Format and display the evaluation
    # formatted_response = f"""
    # **Scenario:**
    # {scenario}
    
    # **User Response:**
    # {user_resp}
    
    # **Feedback:**
    # {feedback}
    
    # **Grade:**
    # {grade}
    # """
    # print(formatted_response)

# Main workflow
if __name__ == "__main__":
    botec_question = get_random_question()
    user_response = prompt_user_for_botec(botec_question)
    evaluate_botec_response(botec_question, user_response)
