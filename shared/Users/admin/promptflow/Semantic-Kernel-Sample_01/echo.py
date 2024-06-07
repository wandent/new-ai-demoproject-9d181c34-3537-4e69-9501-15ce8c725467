from promptflow import tool
from promptflow.connections import CustomConnection
import semantic_kernel as sk
import asyncio

from semantic_kernel.connectors.ai.open_ai import AzureOpenAIChatCompletion

#from semantic_kernel.connectors.ai.open_ai import (
#    AzureTextCompletion,
#    OpenAITextCompletion,
#    OpenAIChatCompletion,
#    AzureOpenAIChatCompletion
#)
import asyncio


# Run your prompt
# Note: functions are run asynchronously

async def respond(prompt: str, deployment: str, conn: CustomConnection ) -> str:
    kernel =sk.Kernel()
    # Define the request settings
    req_settings = kernel.get_prompt_execution_settings_from_service_id(service_id)
    req_settings.max_tokens = 2000
    req_settings.temperature = 0.7
    req_settings.top_p = 0.8

    prompt = """
    1) A robot may not injure a human being or, through inaction, allow a human being to come to harm.
    2) A robot must obey orders given it by human beings except where such orders would conflict with the First Law.
    3) A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.
    Give me the TLDR in exactly 5 words.
    """

    prompt_template_config = sk.PromptTemplateConfig(
        template=prompt,
        name="tldr",
        template_format="semantic-kernel",
        execution_settings=req_settings,
    )

    function = kernel.create_function_from_prompt(
        function_name="tldr_function",
        plugin_name="tldr_plugin",
        prompt_template_config=prompt_template_config,
    )


    kernel.add_chat_completion_service(
        "dv", AzureOpenAIChatCompletion( deployment_name= deployment, endpoint= conn.AZURE_OPENAI_ENDPOINT, api_key= conn.AZURE_OPENAI_KEY)
        )

    text_compl = await kernel.invoke(prompt)
    return text_compl

@tool
def run_prompt(prompt: str, deployment: str, conn: CustomConnection) -> str:      
    result = asyncio.run(respond(prompt, deployment, conn))
    return result


