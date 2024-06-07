import math
from semantic_kernel.skill_definition import ( sk_function, sk_function_context_parameter)
from semantic_kernel.orchestration.sk_context import SKContext

class MathSK:

    @sk_function(
            description="Show the number",
            name="show_number",
            input_description="The number to be shown is: ",
    )
    def show_number(self, input:str )-> str:
        return input


    @sk_function(
        description="Takes the square root of a number",
        name="Sqrt",
        input_description="The value to take the square root of",
    )
    def Sqrt(self, number: str) -> str:
        return str(sqrt(float(number)))

    @sk_function(
        description="Adds two numbers together",
        name="add",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to add",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to add",
    )
    def add(self, context: SKContext) -> str:
        return str(context["input"] + context["number2"])

    @sk_function(
        description="Subtract two numbers",
        name="Subtract",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to subtract from",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to subtract away",
    )
    def subtract(self, context: SKContext) -> str:
        return str(float(context["input"]) - float(context["number2"]))

    @sk_function(
        description="Multiply two numbers. When increasing by a percentage, don't forget to add 1 to the percentage.",
        name="Multiply",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to multiply",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to multiply",
    )
    def multiply(self, context: SKContext) -> str:
        return str(float(context["input"]) * float(context["number2"]))

    @sk_function(
        description="Divide two numbers",
        name="Divide",
    )
    @sk_function_context_parameter(
        name="input",
        description="The first number to divide from",
    )
    @sk_function_context_parameter(
        name="number2",
        description="The second number to divide by",
    )
    def divide(self, context: SKContext) -> str:
        return str(float(context["input"]) / float(context["number2"]))