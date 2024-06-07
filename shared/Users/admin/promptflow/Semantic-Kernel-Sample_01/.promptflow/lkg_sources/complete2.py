from promptflow import tool
from promptflow.connections import CustomConnection

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def complete2(conn: CustomConnection, prompt: str) -> str:
   

    from semantic_kernel import Kernel
    from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
    #from semantic_kernel.connectors.ai.azure_text_completion import AzureTextCompletion



    # Replace with your actual Azure OpenAI credentials
    api_key = conn.AZURE_OPENAI_KEY
    endpoint = conn.AZURE_OPENAI_ENDPOINT
    deployment = "gpt-35-turbo-instruct"
    #openai_text_model_id = "text-davinci-001"  # Choose the appropriate model

    # Create the Semantic Kernel
    from semantic_kernel import Kernel


    # Replace with your actual Azure OpenAI credentials
    #openai_api_key = "YOUR_OPENAI_API_KEY"
    openai_text_model_id = "text-davinci-001"  # Choose the appropriate model

    # Get user input
    user_request = "Translate 'Hello World' to French"

    # Create a prompt that detects intent
    prompt = f"What is the intent of this request? {user_request}"

    # Create the Semantic Kernel with Azure OpenAI service
    kernel = Kernel()
    kernel = kernel.AddAzureOpenAITextCompletion(openai_text_model_id, api_key, endpoint).Build()

    # Invoke the prompt
    result = kernel.InvokePromptAsync(prompt).result()

    print(f"The intent of this request is: {result}")

    return result