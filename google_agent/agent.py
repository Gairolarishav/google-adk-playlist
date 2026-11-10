from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import google_search

root_agent = Agent(
    model='gemini-3.6-flash',
    name='root_agent',
    description='A helpful assistant that can search the web.',
    instruction="""
    Answer user question accurately.
    Use Google Search when you need current information or need to verify the facts. 
    """,
    tools=[google_search]
)
