from promptflow import tool
from promptflow.connections import AzureOpenAIConnection
import semantic_kernel as sk

import asyncio
from semantic_kernel.connectors.ai.open_ai import (
    AzureChatCompletion,
    AzureTextCompletion,
)
kernel = sk.Kernel()    

async def chat(history: str, prompt: str, system: str)-> str:
    service_id = "chat-gpt"
    full_prompt = "system:" + system + " " + history + "  user:" + prompt
    print(full_prompt)      
    chat_function = kernel.create_semantic_function(full_prompt)      
    answer = chat_function(full_prompt)    
    return answer
@tool
def sk_chat(history: str, system: str, prompt: str, deployment_name: str, conn: AzureOpenAIConnection) -> str:
    kernel.add_chat_service(
        "chat_completion",
        AzureChatCompletion(
        deployment_name=deployment_name,
        endpoint=conn.api_base,
        api_key=conn.api_key,
        ))
    chat_result =  asyncio.run(chat(history, prompt, system))
    return str(chat_result)