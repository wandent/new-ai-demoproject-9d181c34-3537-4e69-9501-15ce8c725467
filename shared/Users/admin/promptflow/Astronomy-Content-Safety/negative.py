from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def create_response(state: str, model_state: str,  message:str): 
    if state == "Reject":
        return "Your request has been rejected"
    else:        
        if model_state == "Reject" :
            return "The chat was unable to respond to your request approprietely"
        else:
            return message
