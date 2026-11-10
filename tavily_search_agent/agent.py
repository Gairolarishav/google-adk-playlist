from google.adk.agents.llm_agent import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_tavily import TavilySearch

# Create the Langchain tavily tool
tavily_search = TavilySearch(
    max_result = 5,
    topic = "general"
)

# Wrap it so ADK can use it
tavily_tool = LangchainTool(tool=tavily_search)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search the web.',
    instruction="""Answer user question accurately.
        Use Tavily Search when you need current information or need to verify the facts""",
    tools= [tavily_tool]
)
