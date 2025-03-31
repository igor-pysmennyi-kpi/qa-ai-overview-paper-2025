from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser 
import asyncio
from dotenv import load_dotenv
import logging
import datetime
from promts_e2e import *

TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

load_dotenv()

browser = Browser()


llm_4o_mini = ChatOpenAI(
	model='gpt-4o-mini-2024-07-18',
	temperature=0.7,
)


llm_4o = ChatOpenAI(
	model='gpt-4o-2024-08-06',
	temperature=0.7,
)


async def main(llm, model_name, promt):
    logging.info(f"Running agent with model: {model_name}")
    agent = Agent(
     task=promt.content,
     llm=llm,
     browser=browser,
     generate_gif=True, 
     use_vision=True,
     save_conversation_path=f"e2elogs/{model_name}/{promt.scenario_name}/{TIMESTAMP}"  
     )
    await agent.run()
    input("Press Enter to close the browser...")
    await browser.close()

if __name__ == '__main__':
    # asyncio.run(main(llm_4o_mini, "gpt-4o-mini", MUTANT_LOGIN_PROMT))
    asyncio.run(main(llm_4o, "gpt-4o", LOGIN_NEGATIVE_PROMT))