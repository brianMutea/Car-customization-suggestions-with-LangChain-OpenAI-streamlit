# from langchain.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.agents import load_tools
# from langchain.agents import initialize_agent
# from langchain.agents import AgentType

# from dotenv import load_dotenv

# load_dotenv()


# def generate_suggestions(car_model, use_case):
#     llm = OpenAI(temperature=0.7)

#     # car_models = llm(
#     #     "I have a lot of money. Suggest 5 of the best car models I can purchase.")

#     # replace the code above with PromptTemplates
#     prompt_template = PromptTemplate.from_template(
#         inpute_variable=['car_model'],
#         template="I have a {car_model} car. I want to make it capable for {use_case}. Suggest five best customizations I can do on it for that use case."
#     )

#     car_model_chain = LLMChain(
#         llm=llm, prompt=prompt_template, output_key='customizations')

#     # create an agent to do the reasoning for which actions to take and in which order instead of hardcoding them
#     # def langchain_agent(car_model, use_case):

#     # tools = load_tools(["wikipedia"], llm=llm)
#     # agent = initialize_agent(
#     #     tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     #     verbose=True
#     # )

#     # response = agent.run(
#     #     "I have a {car_model} car. I want to make it capable for {use_case}. Suggest the best customizations I can do on it for that use case.")

#     # return response

#     response = car_model_chain({'car_model': car_model, 'use_case': use_case})

#     return response


# if __name__ == "__main__":
#     print(generate_suggestions('Tesla model s', 'off-roading'))
