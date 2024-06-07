import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    AzureTextCompletion,
    OpenAITextCompletion,
)
from semantic_kernel.orchestration.context_variables import ContextVariables

useAzureOpenAI = True


def main():
    kernel = sk.Kernel()

    # Configure AI service used by the kernel. Load settings from the .env file.
    # the deployment for completion should be gpt-35-turbo-instruct
    if useAzureOpenAI:
        deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
        kernel.add_text_completion_service(
            "dv", AzureTextCompletion( deployment_name= deployment, endpoint= endpoint, api_key= api_key)
        )

    else:
        api_key, org_id = sk.open_ai_settings_from_dot_env()
        kernel.add_text_completion_service(
            "dv", OpenAITextCompletion("gpt-35-turbo-16k", api_key, org_id)
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
    result = joke_function(variables=context_variables)

    print(result)
    
    # Now let's create excuses
    excuse_function = fun_skill["Excuses"]
    context_variables = ContextVariables(
        content="I am late because i got attack by a T-REX coming from another planet on a flying saucer", variables={"input": "for missing my dentist appointment"}
    )
    result = excuse_function(variables=context_variables)
    
    print("An excuse for a T-REX attack: ", result)
    
    # You can also invoke functions like this
    # result = await jokeFunction.invoke_async("time travel to dinosaur age")
    # print(result)


if __name__ == "__main__":
    main()
