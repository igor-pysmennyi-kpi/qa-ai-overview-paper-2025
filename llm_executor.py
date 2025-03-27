import os
import datetime
from dotenv import load_dotenv
import logging

from mistralai import Mistral, UserMessage
from openai import OpenAI
import google.generativeai as genai

from promt_generator import read_prompts

load_dotenv()

TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

class ModelConfig:
    def __init__(self, name, api_key, output_file):
        self.name = name
        self.api_key = api_key
        self.output_file = output_file
        
MISTRAL_LARGE = ModelConfig(
    name="mistral-large-latest", #24.11
    api_key=os.getenv("MISTRAL_API_KEY"),
    output_file=f"mistral_large_output_{TIMESTAMP}.txt"
)

MISTRAL_COST = ModelConfig(
    name="ministral-8b-latest", #24.10
    api_key=os.getenv("MISTRAL_API_KEY"),
    output_file=f"mistral_8b_output_{TIMESTAMP}.txt"
)

OPENAI_LATEST = ModelConfig(
    name="gpt-4.5-preview-2025-02-27" ,
    api_key=os.getenv("OPENAI_API_KEY"),
    output_file=f"openai_45_output_{TIMESTAMP}.txt"
)

OPENAI_LARGE = ModelConfig(
    name="gpt-4o-2024-08-06" ,
    api_key=os.getenv("OPENAI_API_KEY"),
    output_file=f"openai_4o_output_{TIMESTAMP}.txt"
)

OPENAI_COST = ModelConfig(
    name="gpt-4o-mini-2024-07-18" ,
    api_key=os.getenv("OPENAI_API_KEY"),
    output_file=f"openai_4o_mini_output_{TIMESTAMP}.txt"
)

GEMINI_LATEST = ModelConfig(
    name="gemini-2.5-pro-exp-03-25",
    api_key=os.getenv("GOOGLE_API_KEY"),
    output_file=f"gemini_25_pro_output_{TIMESTAMP}.txt"
)

GEMINI_COST = ModelConfig(
    name="gemini-2.0-flash-lite",
    api_key=os.getenv("GOOGLE_API_KEY"),
    output_file=f"gemini_2_flash_output_{TIMESTAMP}.txt"
)


def save_to_file(file_path, content, tokens_used):
    content = content+f"\n\nTotal tokens used: {tokens_used}"
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.debug(f"Successfully saved output to {file_path}")
    except IOError as e:
        logging.error(f"Error saving file {file_path}: {e}")


def call_mistral(config, prompt):
    logging.info(f"Calling Mistral ({config.name})... for {promt.name}")
    try:
        client = Mistral(api_key=config.api_key)
        chat_response = client.chat.complete(
            model=config.name,
            messages=[
                UserMessage(content=prompt.content)
            ],
            temperature=0.7 
        )
        if chat_response.choices:
            token_usage = chat_response.usage.total_tokens
            logging.info(f"{config.name} response received. Total tokens used: {token_usage}")
            response = chat_response.choices[0].message.content
            save_to_file(promt.output_dir+"/"+config.output_file, response, token_usage)
        else:
            logging.error(f"Error: No response received from {config.name}.")
    except Exception as e:
        logging.error(f"Error calling Mistral API: {e}")

def call_openai(config, prompt):
    logging.info(f"Calling OpenAI ({config.name})... for {promt.name}")
    try:
        client = OpenAI(api_key=config.api_key)
        response = client.chat.completions.create(
            model=config.name,
            messages=[{"role": "user", "content": prompt.content}],
            temperature=0.7 
        )
        if response.choices:
            token_usage = response.usage.total_tokens
            logging.info(f"{config.name} response received. Total tokens used: {token_usage}")
            save_to_file(promt.output_dir+"/"+config.output_file, response.choices[0].message.content, token_usage)     
        else:
            logging.error(f"Error: No response received from {config.name}.")
    except Exception as e:
        logging.error(f"Error calling OpenAI API: {e}")

def call_gemini(config, prompt):
    logging.info(f"Calling Gemini ({config.name})... for {promt.name}")
    try:
        genai.configure(api_key=config.api_key)
        generative_model = genai.GenerativeModel(config.name)
        response = generative_model.generate_content(
            prompt.content,
            generation_config=genai.GenerationConfig(
                temperature=0.7
            ),
        )
        if not response.parts:
             block_reason = response.prompt_feedback.block_reason if response.prompt_feedback else 'Unknown'
             safety_ratings = response.prompt_feedback.safety_ratings if response.prompt_feedback else 'N/A'
             logging.error(f"Gemini response might be empty or blocked. Reason: {block_reason}, Safety Ratings: {safety_ratings}")
             return 
         
        token_usage = response.usage_metadata.total_token_count
        logging.info(f"{config.name} response received. Total tokens used: {token_usage}")
        save_to_file(promt.output_dir+"/"+config.output_file, response.text, token_usage)     
    except Exception as e:
        logging.error(f"Error calling Google Gemini API: {e}")

    
if __name__ == "__main__":
    
    for promt in read_prompts("stories"):
        logging.info(f"Executing prompt: '{promt.content}'\n")

        call_gemini(GEMINI_COST, promt)
        call_gemini(GEMINI_LATEST, promt)

        call_mistral(MISTRAL_LARGE, promt)
        call_mistral(MISTRAL_COST, promt)

        call_openai(OPENAI_COST, promt)
        call_openai(OPENAI_LARGE, promt)
        call_openai(OPENAI_LATEST, promt)

    