from promptflow import tool
from promptflow.connections import CustomConnection
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    AzureTextCompletion,
    OpenAITextCompletion,
)
from semantic_kernel.orchestration.context_variables import ContextVariables

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

@tool
def jokes_sk(topic: str, conn: CustomConnection)-> str: 
    kernel = sk.Kernel()

    # Configure AI service used by the kernel. Load settings from the .env file.
    # the deployment for completion should be gpt-35-turbo-instruct
    endpoint = conn.AZURE_OPENAI_ENDPOINT
    api_key = conn.AZURE_OPENAI_KEY
    deployment = "gpt-35-turbo-instruct"
    kernel.add_text_completion_service(
        "dv", AzureTextCompletion( deployment_name= deployment, endpoint= endpoint, api_key= api_key)
    )    
    
    # run the completion from a prompt
    # result = kernel.text_completion("dv", "Hello, my name is")   


    skills_directory = "skills"

    fun_skill = kernel.import_semantic_skill_from_directory(
        skills_directory, "FunSkill"
    )

    joke_function = fun_skill["Joke"]

    # The "input" variable in the prompt is set by "content" in the ContextVariables object.
    context_variables = ContextVariables(
        content="time travel to dinosaur age", variables={"style": "funny story"}
    )
    result = str(joke_function(variables=context_variables))    
    # Now let's create excuses
    #excuse_function = fun_skill["Excuses"]
    #context_variables = ContextVariables(
    #    content="I am late because i got attack by a T-REX coming from another planet on a flying saucer", variables={"input": "for missing my dentist appointment"}
    #)
    #result = excuse_function(variables=context_variables)
    #print("An excuse for a T-REX attack: ", result)
    return result


   