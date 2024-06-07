from promptflow import tool
from promptflow.connections import CustomConnection

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

# In Python tool you can do things like calling external services or
# pre/post processing of data, pretty much anything you want


@tool
def echo(conn: CustomConnection) -> str:
    #llm_service=conn.GLOBAL_LLM_SERVICE
    #key = conn.AZURE_OPENAI_KEY
    #endpoint=conn.AZURE_OPENAI_ENDPOINT
    return conn.AZURE_OPENAI_ENDPOINT

    