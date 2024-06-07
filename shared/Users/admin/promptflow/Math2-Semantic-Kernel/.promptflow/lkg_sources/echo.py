from promptflow import tool
import semantic_kernel as sk
import config.add_completion_service
from semantic_kernel.planning.sequential_planner import SequentialPlanner
from plugins.MathPlugin.Math import Math
import asyncio



#from plugins import MathPlugin
#import config.add_completion_service



@tool
async def mathtest(input: str) -> str:
       # Initialize the kernel
    kernel = sk.Kernel()
    # Add a text or chat completion service using either:
    # kernel.add_text_completion_service()
    # kernel.add_chat_service()
    kernel.add_completion_service()

    # Import the MathPlugin.
    math_plugin = kernel.import_skill(skill_instance=Math(), skill_name="MathPlugin")
   # math_plugin = kernel.import_skill(MathPlugin(), skill_name="MathPlugin")

    planner = SequentialPlanner(kernel)
    ask = input
    #ask = "If my investment of 2130.23 dollars increased by 23%, how much would I have after I spent $5 on a latte?"

    # Create a plan
    plan = await planner.create_plan_async(ask)

    # Execute the plan
    result = await plan.invoke_async()
    print("Plan results:")
    print(result)
    value =  result.result
    return value

