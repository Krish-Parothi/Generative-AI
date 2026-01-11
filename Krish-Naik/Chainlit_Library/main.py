from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema import StrOutputParser
from langchain_classic.schema.runnable import Runnable
from langchain_classic.schema.runnable.config import RunnableConfig
from typing import cast
from dotenv import load_dotenv
import os

load_dotenv()

import chainlit as cl

parser = StrOutputParser()

@cl.on_chat_start
async def on_chat_start():
    model = ChatGroq(model="openai/gpt-oss-120b", api_key=os.getenv("GROQ_API_KEY"), temperature=0.8)
    prompt = PromptTemplate(
        template="""
                Question: {question},
                Answer: Act like a normal person.

"""
    )
    chain = prompt | model | parser
    cl.user_session.set("chain", chain)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cast(Runnable, cl.user_session.get("chain"))  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()