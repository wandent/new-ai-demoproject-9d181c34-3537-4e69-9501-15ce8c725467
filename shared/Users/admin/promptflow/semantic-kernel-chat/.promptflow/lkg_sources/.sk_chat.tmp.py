from promptflow import tool
from promptflow.connections import AzureOpenAIConnection
import semantic_kernel as sk
#import semantic_kernel.contents
#from semantic_kernel.contents.chat_history import ChatHistory


import asyncio
from semantic_kernel.connectors.ai.open_ai import (
    AzureChatCompletion,
    AzureTextCompletion,
)

from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.prompt_template.input_variable import InputVariable
from semantic_kernel.prompt_template.prompt_template_config import PromptTemplateConfig

kernel = sk.Kernel()

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


    
#req_settings = kernel.get_prompt_execution_settings()
#req_settings.max_tokens = 2000
#req_settings.temperature = 0.7
#req_settings.top_p = 0.8
#req_settings.auto_invoke_kernel_functions = True
#chat_function = kernel.create_semantic_function(
#prompt= system + """{{$chat_history}}{{$user_input}}""",
#function_name="chat",
#plugin_name="chat",
#prompt_execution_settings=req_settings,
    

async def chat(prompt: str, system: str)-> str:
    service_id = "chat-gpt"
    full_prompt = "system:" + system + " user: " + prompt
    print(full_prompt)
    
    
    template = """

    Previous information from chat:
    {{$chat_history}}
    
    User: {{$request}}
    Assistant: 
    """

    prompt_template_config = PromptTemplateConfig(
        template=template,
        name="chat",
        description="Chat with the assistant",
        template_format="semantic-kernel",
        input_variables=[
            InputVariable(name="chat_history", description="The conversation history", is_required=False, default=""),
            InputVariable(name="request", description="The user's request", is_required=True),
        ],
        execution_settings=kernel.OpenAIChatPromptExecutionSettings(
            service_id=service_id, max_tokens=4000, temperature=0.2
        ),
    )

    chat_function = kernel.create_function_from_prompt(
        function_name="chat",
        plugin_name="ChatBot",
        prompt_template_config=prompt_template_config,
    )
    
    #chat_function = kernel.create_semantic_function(full_prompt)
    #history = ChatHistory()
    #history.add_user_message("Hi there, who are you?")
    #history.add_assistant_message("I am a chatbot made in semantic kernel.")    
    
  
    answer = chat_function(chat_history="", request = full_prompt)
    #history.add_user_message(user_input)
    #history.add_assistant_message(str(answer))  
    
    return answer
@tool
def sk_chat(system: str, prompt: str, deployment_name: str, conn: AzureOpenAIConnection) -> str:
    kernel.add_chat_service(
        "chat_completion",
        AzureChatCompletion(
        deployment_name=deployment_name,
        endpoint=conn.api_base,
        api_key=conn.api_key,
        ))
    chat_result =  asyncio.run(chat(prompt, system))
    return str(chat_result)