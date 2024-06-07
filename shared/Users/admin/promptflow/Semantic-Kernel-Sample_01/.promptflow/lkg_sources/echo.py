from promptflow import tool
from promptflow.connections import CustomConnection
import semantic_kernel as sk
import asyncio

from semantic_kernel.connectors.ai.open_ai import (
    AzureTextCompletion,
    OpenAITextCompletion,
)

def respond(prompt: str, deployment: str, conn: CustomConnection ) -> str:
    kernel = sk.Kernel()      
    kernel.add_text_completion_service(
        "dv", AzureTextCompletion( deployment_name= deployment, endpoint= conn.AZURE_OPENAI_ENDPOINT, api_key= conn.AZURE_OPENAI_KEY)
        )
    text_compl =  kernel.invoke("dv","Hello, i'd like you to explain the following topic: " + prompt)
    return text_compl


@tool
def run_prompt(prompt: str, deployment: str, conn: CustomConnection) -> str:      
    result = respond(prompt, deployment, conn)
    return result


