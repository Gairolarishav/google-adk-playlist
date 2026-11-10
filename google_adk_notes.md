# Google ADK Course Notes

**Contents**
1. Lecture 1: Introduction (Agents, Multi-Agent Systems, Why ADK)
2. Lecture 2: Build Your First Agent
3. Lecture 3: Tools in Google ADK

> **Note:** The transcripts say "Genkit", "AI SDK", "EDK" and "SDK" in many places. These are speech-to-text mistakes. The tool is **Google ADK (Agent Development Kit)**.

---

# Lecture 1: Introduction to Agents, Multi-Agent Systems and Google ADK

## 1. Why This Course?

- Agents are everywhere. Everyone is building and deploying them.
- Two main frameworks are used in the industry: **LangGraph** and **Google ADK**.
- **LangGraph** gives more low-level control.
- **Google ADK** gives more abstraction, so building agents is easier. It is a natural fit for companies already in the Google ecosystem.

**Two goals of this course:**
1. Teach ADK fundamentals (using **ADK version 2**, the latest).
2. Teach how to build **multi-agent systems** (ADK supports them by default, which is easier than in LangGraph).

**Topics coming up:** state, memory, tools, A2A protocol, multi-agent systems, evaluation, deployment.

---

## 2. What Is an Agent?

> **An agent is what you get when you let a model take actions in a loop toward a goal.**
> It decides what to do, does it, looks at the result, and decides again, until the goal is done or it gives up.

- An LLM alone is **text in, text out**. It cannot take actions.
- An agent can act and moves toward a goal on its own.

### 3 properties of an agent

| Property | Meaning |
|----------|---------|
| **Tools** | Can search the web, call APIs, read and write files, run code. It changes things in the real world |
| **Autonomy over control flow** | The agent decides its own steps |
| **Feedback loop** | Acts → observes result → adjusts plan → acts again |

### Parts of an agent

- **LLM** = the brain
- **Tools** = hands and legs
- **Memory** = memory
- All three work in the **agent loop** to reach the **goal**.

---

## 3. What Is a Multi-Agent System?

Several AI agents work together on one task. Each agent has its own LLM, tools, memory and loop, but usually a **narrower role**.

**Example (coding):** Planning, writing, reviewing and testing code are different jobs. One agent doing all of them may struggle. Four specialist agents (planner, coder, reviewer, tester) do better as a team.

### Benefits

| Benefit | Why it helps |
|---------|--------------|
| **Focus** | Each agent has a small task, a clear prompt and only the tools it needs |
| **Context window** | Each agent has its own context window, so none fills up too fast. A sub-agent returns only a **summary** to the parent |
| **Speed** | Independent tasks can run **in parallel** |
| **Less bias** | A separate reviewer judges the work more fairly than the agent that wrote it |

### Trade-offs

| Trade-off | Why it hurts |
|-----------|--------------|
| **Complexity** | Hard to make many agents work together |
| **Cost** | More model calls and more tokens |
| **Coordination problems** | Agents misunderstand each other, repeat work or miss details |
| **Harder debugging** | Hard to tell who did what and who changed the state |

---

## 4. Common Multi-Agent Patterns

1. **Orchestrator-Worker**
   - A lead agent splits the task, gives parts to worker agents, then merges their results.
   - Example: a research agent splits a blog topic into 4 sub-topics. Four workers research in parallel. The orchestrator writes the blog.
   - Example: understanding a new codebase (one agent each for backend, frontend, database).

2. **Sequential Pipeline**
   - Agents work one after another.
   - Example: Research agent → Writer agent → Editor agent.

3. **Parallel**
   - Many agents work on the same input at the same time. Results are merged.
   - Example: grading a student answer. One agent checks marks, one checks plagiarism, one checks profanity.

4. **Debate / Critic**
   - One agent proposes. Another criticizes. They repeat until the critic is happy.
   - Example: coder agent and reviewer agent.

5. **Peer Collaboration**
   - Agents talk freely with **no boss**.
   - Less common. Example: experimental "village" projects with hundreds of agents living together.
   - Not covered in this course.

---

## 5. Why Use a Framework (Not Plain Code)?

For a simple project, plain Python is fine and good for learning. For complex agents, a framework is needed.

**Three reasons:**

1. **Complex control flow.** You need retries, timeouts, fallbacks, tool-failure handling, memory, MCP tools and more. This "plumbing" code takes a lot of time. Frameworks give it ready-made.
2. **Multi-agent orchestration.** Routing work, handoffs between agents, passing state, parallel runs and merging results are hard to write by hand.
3. **Provider lock-in.** Every LLM provider (OpenAI, Anthropic) has its own message format, tool calling, streaming and caching. Switching providers means rewriting code. Frameworks hide these differences, so you become **model agnostic**.

---

## 6. Other Frameworks (Quick Look)

| Framework | Key point |
|-----------|-----------|
| **LangGraph** | From LangChain. Python and JS. Low-level control, checkpointing, pause/resume, human-in-the-loop, long-running agents. Most mature |
| **CrewAI** | Quickly build multi-agent "crews" |
| **Agno** | Fast, lightweight, easy, built-in memory |
| **Pydantic AI** | Type-safe, validated inputs and outputs |
| **OpenAI Agents SDK** | Simple, good for small and medium agents |
| **Microsoft Agent Framework** | Improved AutoGen, strong Azure support, close competitor to ADK |
| **Bedrock Agents** | From AWS |
| **Claude Agent SDK** | Uses the same loop as Claude Code, not very popular in enterprise |

**Instructor's view:** LangGraph is the clear winner. Others are chosen based on the company's existing stack (Microsoft, OpenAI, AWS).

---

## 7. What Is Google ADK?

> **ADK = Agent Development Kit.** An open-source framework from Google to **build, evaluate and deploy** AI agents and multi-agent systems.

- **Open source**, even though Google made it.
- **Code-first.** It is not a visual builder or a no-code tool.

### History

- Built **inside Google first**, for two internal systems:
  - **Agent Space** (internal research platform)
  - **Customer Engagement Suite (CES)** (customer service)
- Later made open source.
- Launched on **April 9, 2025** at **Google Cloud Next**. First it was Python-only. The promise was an agent in under 100 lines. More languages were added later.
- **ADK V2** came at **Google Cloud Next 2026**. It added **graph-based agents**, similar to LangGraph.

### The bigger Google ecosystem (launched together)

| Part | What it is |
|------|-----------|
| **ADK** | Framework to build agents |
| **A2A (Agent-to-Agent) protocol** | A standard way for one agent to talk to another, even across frameworks. About 50 partners at launch |
| **Agent Engine** | Managed runtime on **Vertex AI** to deploy agents to production. Works with **any framework** (LangGraph, CrewAI, etc.) |

Google released ADK partly because it felt it was falling behind (Microsoft had AutoGen, OpenAI had its SDK).

---

## 8. Strengths of ADK

1. **Built for multi-agent systems** from day one.
2. **Works with any model.** Best with Gemini, but OpenAI, Anthropic and others work too.
3. **Many languages.** Python, TypeScript, Java, Go, Kotlin and Android.
4. **Native A2A support.** Built-in functions, no extra code.
5. **Great developer experience.** Web UI, traces, evaluation and deployment tools come out of the box.
6. **Built-in evaluation** for each agent.
7. **Structured context.** Sessions, memory, tool outputs and artifacts are stored properly, not as raw chat.
8. **Google backing.** Likely to be actively maintained with new features.

## 9. Trade-offs of ADK

1. **Opinionated structure.** You must organize the project and its lifecycle in ADK's way. Unusual designs may feel restricted.
2. **Ecosystem lock-in feeling.** It nudges you to Google models and Google Cloud, though other things still work.

### Which one to choose?

- Only two premium choices: **LangGraph** and **Google ADK**.
- Locked into AWS → Bedrock Agents. Locked into Microsoft → Microsoft Agent Framework.
- Framework-neutral or already in Google ecosystem → **Google ADK**.

---

## 10. Course Plan (about 15 to 16 videos, may change)

1. Intro (this video)
2. Setup and first agent
3. Tools (different types)
4. Structured output
5. ADK internals (runner, events, context)
6. MCP tools
7. Session and state management
8. Memory
9. RAG agent
10. Workflows: sequential, parallel, loop
11. First multi-agent system
12. Graph-based workflows (ADK 2)
13. A2A (the transcript says "E2E", which is likely a mistake)
14. Human-in-the-loop
15. Evaluation
16. Deployment

Most videos are free on YouTube. Notes and some extras are for CampusX members.

---

## 11. Quick Revision (Lecture 1)

1. **Agent** = LLM + tools + memory, running in a loop toward a goal.
2. **Multi-agent system** = several focused agents working together.
3. Benefits: focus, separate context windows, speed, less bias.
4. Costs: complexity, money, coordination, debugging.
5. Patterns: Orchestrator-Worker, Sequential, Parallel, Debate/Critic, Peer.
6. Frameworks save you from writing plumbing, orchestration and provider-specific code.
7. **ADK** = Google's open-source, code-first agent framework, with A2A and Agent Engine around it.
8. Main picks today: **LangGraph** or **Google ADK**.

---
---

# Lecture 2: Build Your First Agent (Google ADK)

---

## 1. What You Learn in This Video

- Set up a basic agent (a simple chatbot) in ADK
- Run it in **3 ways**: terminal, web UI, API server
- Switch from Gemini to **OpenAI** using LiteLLM
- Change model settings like temperature and max tokens

**Good to know:** ADK works best with Gemini, but you are **not locked in**. You can use OpenAI, Anthropic, or open-source models (for example through Ollama).

---

## 2. Setup Steps

| Step | What to do | Command |
|------|-----------|---------|
| 1 | Make a folder and open it in VS Code | e.g. folder named `course` |
| 2 | Create a virtual environment | `python3 -m venv venv` |
| 3 | Activate it (different on Mac and Windows) | Mac: `source venv/bin/activate`<br>Windows: `venv\Scripts\activate` |
| 4 | Install ADK | `pip install google-adk` |
| 5 | Check the version (should be **2.x**) | `adk --version` |
| 6 | Create the agent | `adk create campusx_bot` |

**Why a virtual environment?** It keeps this project's packages separate from other projects.

### Useful `adk` commands (seen in the course)

- `adk create` → make a new agent
- `adk run` → chat in the terminal
- `adk web` → open the web UI
- `adk api_server` → start an API server
- `adk eval` → test the agent (later)
- `adk deploy` → deploy the agent (later)

---

## 3. What `adk create` Asks You

1. **Which model?** (Gemini 1.5 Flash, Gemini 2.0 Flash, or others)
2. **Which backend?** Choose **Google AI** (others: Vertex AI, Login with Google)
3. **API key?** Get a free one from **Google AI Studio** → *API keys* → *Create API key*, then paste it

> Tip: Newer Gemini models may be available now. If an older model is not found, pick a newer Flash model.

---

## 4. Files Created

```
course/
└── campusx_bot/
    ├── __init__.py   # makes the folder a Python package
    ├── .env          # stores your API key (keep it secret)
    └── agent.py      # main agent file (the "root agent")
```

- `__init__.py` has one line. It lets Python treat the folder as a module.
- `.env` holds secrets such as `GOOGLE_API_KEY`. **Never upload it to GitHub.**
- `agent.py` is the most important file.

---

## 5. Understanding `agent.py`

The **root agent** is the starting point. In bigger projects you can build many agents (a **multi-agent system**), and the root agent is the first one.

```python
from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-1.5-flash",
    name="root_agent",
    description="A helpful assistant",
    instruction="Answer the user's questions politely.",
)
```

| Field | Meaning |
|-------|---------|
| `model` | Which LLM the agent uses |
| `name` | Name of the agent (you can change it) |
| `description` | Short summary of what it does. In multi-agent systems, other agents read this to decide **who should get a task** |
| `instruction` | How the agent should behave |

**Key point:** ADK does a lot of work for you (abstraction). In LangGraph you write much more code by hand. Right now this agent is only a **chatbot**. Tools, memory, and more come in later videos.

---

## 6. Three Ways to Run Your Agent

### Way 1: Terminal

```bash
adk run campusx_bot
```

- Chat directly in the terminal.
- Sometimes you get an error like "model overloaded." This happens with the **free tier** of Gemini 1.5 Flash. It is **not your mistake**. Just run it again.

### Way 2: Web UI (most powerful)

```bash
adk web
```

- Run it from the **parent folder** (no agent name needed).
- Open the URL it prints in your browser.

**Features of the web UI:**

- **Chat window** with **short-term memory** (it remembers your name inside one conversation)
- **Multiple sessions**: start new chats and switch between them
- **Events**: every message (from you or the agent) is an event. Click one to see:
  - Agent graph (useful for multi-agent systems)
  - Request and response details
  - Metadata such as tokens in and out
  - Who sent it (user or root agent)
- **Tracing**: shows time taken by each LLM call (no need for a separate tool like LangSmith)
- **State**: see variables and how they change over turns
- **Artifacts**: view any files or items the agent makes
- **Evaluation**: create evaluation sets
- **Multiple agents**: switch between different bots

> In LangGraph this would need a lot of custom code. In ADK it is built in.

### Way 3: API Server

```bash
adk api_server --port 8003
```

- ADK automatically builds an API using **FastAPI**.
- If port 8000 is busy (the web UI uses it), choose another port.
- Open `http://localhost:8003/docs` to see all endpoints.
- You can **deploy it** or connect it to your own backend.

---

## 7. Using Other Models (OpenAI, Anthropic) with LiteLLM

**Problem:** Every provider has its own SDK. Switching providers means rewriting code.

**Solution: LiteLLM.** One common interface for many providers. ADK has strong support for it.

### Steps

**1. Install LiteLLM**

```bash
pip install litellm
```

**2. Change the model in `agent.py`**

```python
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),   # any supported model
    name="root_agent",
    description="A helpful assistant",
    instruction="Answer the user's questions politely.",
)
```

**3. Add your OpenAI key in `.env`**

```
OPENAI_API_KEY=your_key_here
```

- Get the key at **platform.openai.com** → *API keys* → *Create new secret key*.

**Result:** The agent is the same, only the model changed. Anthropic works the same way (use an Anthropic model name and `ANTHROPIC_API_KEY`).

---

## 8. Changing Model Settings

Add a config to your agent to control how the model behaves.

```python
from google.genai import types

root_agent = Agent(
    model="gemini-1.5-flash",
    name="root_agent",
    description="A helpful assistant",
    instruction="Answer the user's questions politely.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=800,
    ),
)
```

| Setting | Meaning |
|---------|---------|
| `temperature` | Lower (like 0.3) = more focused and predictable. Higher = more creative |
| `max_output_tokens` | Maximum length of the reply (here, 800 tokens) |
| Retry options | You can also add retry settings for failures |

---

## 9. Quick Revision

1. ADK = Google's Agent Development Kit. Install with `pip install google-adk`.
2. `adk create <name>` builds the agent folder with `__init__.py`, `.env`, `agent.py`.
3. The **root agent** is the starting point. It needs `model`, `name`, `description`, and `instruction`.
4. Run it three ways: `adk run` (terminal), `adk web` (UI), `adk api_server` (API).
5. The web UI gives sessions, events, tracing, state, and evaluation for free.
6. Use **LiteLLM** to switch to OpenAI, Anthropic, or open-source models.
7. Set `temperature` and `max_output_tokens` through the content config.
8. Right now it is just a chatbot. **Tools, memory, and multi-agent** features come next.

---

## 10. Common Problems

| Problem | Fix |
|---------|-----|
| Model times out or overloaded | Free tier is busy. Run again or switch model |
| Port already in use | Use a different port: `--port 8003` |
| `adk` command not found | Activate your virtual environment first |
| API key error | Check the `.env` file and the key name |

---
---

# Lecture 3: Tools in Google ADK

> **Note:** "SDK" in the transcript means **ADK**. Tools are what turn a chatbot into a real **agent**.

## 1. Recap and Plan

- Lecture 1: intro to ADK. Lecture 2: first chatbot (no actions, so not yet a real agent).
- **Today:** add **tools** so the LLM can take actions. Learn what tools are, the tool types in ADK, try them, and build a mini-project (refund agent).

---

## 2. What Are Tools?

- **LLM strength:** smart, knows a lot about the world.
- **LLM weakness:** text in, text out. It cannot take actions (send email, get today's weather).
- Think of an LLM as a **brain**. Tools are its **hands and legs**.
- In practice, a tool is just a **function** (written by you or by a third party).

### 4 common types of tools

| Type | Examples |
|------|----------|
| **Information retrieval** | Web search, database query, RAG over your documents |
| **Computation** | Code interpreter (data analysis on CSV), calculator |
| **File and system access** | File read/write (file manager agent), shell tool (coding agent) |
| **External actions** | Send email, create calendar event, call APIs, control a browser |

---

## 3. How Tools Work: Function Calling

**Example:** weather agent. Question: "Will it rain in Gurgaon today?"

| Step | What happens |
|------|--------------|
| 1 | Your code sends the **question + tool description** (what it does, inputs, outputs) to the LLM |
| 2 | LLM decides it needs the tool and returns a **tool request**: `get_weather("Gurgaon")` |
| 3 | Your code **calls the function**. The API runs and returns e.g. "32°C, clear" |
| 4 | Your code sends the **tool result** back to the LLM |
| 5 | LLM writes the **final answer** |

**Key point:** The LLM **cannot call a tool itself**. It only decides **which tool** and **which arguments**. Something else must run it.

### What ADK changes

- Without a framework, **you** write all the glue code (LLM → code → tool → code → LLM).
- In ADK, the **Runner** does this for you.
- You only say: "this is my LLM, this is my tool, these are my instructions."

---

## 4. Types of Tools in ADK

### A. Function tools (you write them)

| Kind | Meaning |
|------|---------|
| **Regular function tool** | Runs once, gives the result (e.g. `get_weather`) |
| **Long-running function tool** | For slow tasks. Example: refund above ₹10,000 needs human approval that may come after days. The agent keeps working meanwhile. Mainly used for **human-in-the-loop** (later lecture) |
| **Agent as a tool** | One agent calls another agent. Example: a support agent calls a refund agent. This makes a multi-agent system |

### B. Built-in tools (come with ADK, no code to write)

- **Google Search**
- **Code Execution** (run Python, for example for data analysis)
- **RAG tool** (later)

### C. Third-party tools

- ADK has a wrapper to reuse tools from **LangChain**, **CrewAI**, etc.
- Examples: **Tavily Search**, **Arxiv**, **Wikipedia**.

### D. Tools without writing tools

- **MCP tools:** connect to existing MCP servers (e.g. GitHub MCP server). Covered in a later lecture.
- **OpenAPI tools:** give ADK your OpenAPI documentation and it uses your existing APIs as tools. Great for companies.

**Covered today:** regular function tools, agent-as-tool (mentioned), Google Search, Code Execution, Tavily (LangChain). **Not today:** long-running tools and MCP.

---

## 5. Built-in Tools

**Two important points:**

1. They work **only with Gemini models**. They are Gemini features, not ADK features. With OpenAI or Anthropic they will not work (there are workarounds).
2. The instructor found they **did not work on the free tier**. You may need to add a small amount of money (₹300 to ₹400 is enough) in billing. Your experience may differ.

### Google Search

```python
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="A helpful assistant that can search the web.",
    instruction="Answer user questions accurately.",
    tools=[google_search],
)
```

- Run with `adk web`, choose the agent, ask "Top AI news today".
- The UI shows the root agent **called the Google Search tool**.
- No glue code needed.

### Code Execution

```python
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="A helpful assistant that can write and run Python code.",
    instruction="Answer user questions accurately.",
    code_executor=BuiltInCodeExecutor(),   # NOT inside tools=[...]
)
```

- **Syntax difference:** code execution uses `code_executor=`, not `tools=`. It runs a different pipeline (it actually runs Python and returns the result).
- **Demo:** paste 100 rows of Titanic CSV and ask for "univariate analysis". The agent writes and runs Python code, then gives a report per column.
- Small oddity: the invocation graph did not show the code-execution tool.

---

## 6. Third-Party Tool: Tavily Search (from LangChain)

**Steps:**

1. Create a **Tavily** account and get an API key. Put it in `.env` as `TAVILY_API_KEY`.
2. Install: `pip install langchain-tavily`
3. Wrap the LangChain tool so ADK can use it:

```python
from google.adk.agents import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_tavily import TavilySearch

tavily = TavilySearch(max_results=5, topic="general")   # a LangChain tool
tavily_tool = LangchainTool(tool=tavily)                # now an ADK tool

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="Search agent",
    instruction="Answer user questions accurately.",
    tools=[tavily_tool],
)
```

- Works like Google Search, but works with **any model** (not only Gemini).
- So **Tavily is a workaround** when you use non-Gemini models and need web search.

---

## 7. Custom Function Tool (Regular)

**Example:** World Clock agent. Ask for the current time in any city.

```python
def get_current_time(timezone: str) -> dict:
    """Returns the current date and time for a given IANA timezone,
    for example 'Europe/London'. Use this when the user asks about the time."""
    # ... use datetime + zoneinfo ...
    return {
        "status": "success",
        "timezone": timezone,
        "date": "2026-01-01",
        "time": "12:30",
        "weekday": "Thursday",
    }

root_agent = Agent(..., tools=[get_current_time])
```

### Rules for writing function tools

1. Add **type hints**, including the **return type** (here `dict`).
2. Write a **clear docstring**. The LLM reads it to know what the tool does and when to use it.
3. Return a **descriptive dictionary** (status, timezone, date, time, weekday). Do **not** return just a plain string.
4. Pass the function in `tools=[...]`. Same syntax as built-in tools.

**Demo:** "Time in London?" works. "Is it day or night in Zurich?" also works. The LLM figures out the timezone, calls the tool, reads the time, and reasons about day or night.

---

## 8. Using Multiple Tools Together

Give one agent many tools at once. Example agent has:

- `google_search` (built-in)
- `tavily_tool` (third-party)
- `get_current_time` (function tool)
- Code executor (built-in)

```python
from google.genai import types

root_agent = Agent(
    ...,
    tools=[google_search, tavily_tool, get_current_time],
    code_executor=BuiltInCodeExecutor(),
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(include_server_side_tool_invocations=True)
    ),
)
```

> The exact field name for the extra config can differ by version. If it errors, check the ADK docs for "server-side tool invocations".

### Why the extra config is needed

- **Google Search and code execution** run on **Gemini's servers**.
- **Tavily and your own functions** run inside **ADK**.
- Without the config, context gets **split** between Gemini and ADK.
- The config tells Gemini to **send server-side tool details back** so ADK has the full context.
- Needed **only when mixing built-in tools** with other tools. If you use only your own function tools, you do not need it.

Ask the agent "List the tools you have" and it lists all four.

---

## 9. Mini-Project: Refund Agent (CampusX)

**Goal:** automate course refunds that admins normally do by hand.

### Refund policy

- Request within **7 days** of purchase, **and**
- Watched **less than 20%** of the course.

### Flow

1. Student asks for a refund → agent asks for **registered email**.
2. Agent checks the student exists and finds their **enrollments**.
3. If many courses, ask **which course**.
4. Check **eligibility** (within 7 days and under 20%).
5. **Not eligible:** explain why (too late, or watched too much).
6. **Eligible:** ask for the **reason**, confirm the request, **save it in the database**.
7. (Not built) Call a payment provider like Razorpay to send the money back.

### Dummy database (SQLite, `campusx.db`)

| Table | Content |
|-------|---------|
| `students` | 5 students |
| `courses` | 3 courses (Google ADK, LLM Ops, Advanced Track) |
| `enrollments` | 10 rows: enrollment ID, student ID, course ID, purchase date, amount paid, completion %, status (active, refund requested, refunded), refund reason |

### The 6 function tools

| Tool | Job |
|------|-----|
| `identify_student` | Check the email exists |
| `get_my_enrollments` | List courses the student bought |
| `get_refund_policy` | Return the policy (kept in a tool, not the prompt, because real policies can be long) |
| `check_refund_eligibility` | Check 7-day and 20% rules |
| `place_refund_request` | Save the reason and change status from **active** to **refund requested** |
| `get_refund_status` | Let the student check later: **refunded** or **refund requested** |

### Project files

| File | Purpose |
|------|---------|
| `__init__.py`, `.env`, `agent.py` | Same as before |
| `setup_database.py` | Run once to create and fill `campusx.db` |
| `tools.py` | All 6 tools (simple database code). Tools can live in a **separate file** and be imported into `agent.py` |
| `campusx.db` | The dummy database |

### Inside `agent.py`

- Imports the tools from `tools.py`.
- Has a **name**, **model**, **description** and a detailed **system prompt** (the instruction).
- The prompt contains the **workflow**: identify student, fetch enrollments, ask which course if unclear, check eligibility, explain if not eligible, ask for reason if eligible, save the reason **as given** (do not judge or invent), then confirm.
- All 6 tools are listed in `tools=[...]`.
- Tool **docstrings** also help the agent understand each tool.

### Demo summary

- Student: Rahul Sharma, 2 active courses (ADK at 15%, LLM Ops at 5%).
- The agent calls tools one by one: identify student → get enrollments → check eligibility.
- LLM Ops (bought more than 7 days ago) is **not eligible**. The ADK course is eligible.
- After the reason and confirmation, the database shows **Refund Requested** with the reason.
- In a **new session** later, "refund status?" calls `get_refund_status` and gives the update.

### Why this is nice

- No plumbing or control-flow code, unlike LangGraph.
- Just a **system prompt + tool imports + your tools**.
- Code is well organized: agent code in one place, tools and database code in another.

---

## 10. Quick Revision (Lecture 3)

1. LLMs cannot act. **Tools** give them hands. A tool is a **function**.
2. **Function calling:** the LLM only **chooses the tool and arguments**. The framework runs it. In ADK the **Runner** does this.
3. ADK tool types: **function tools** (regular, long-running, agent-as-tool), **built-in**, **third-party**, plus **MCP** and **OpenAPI**.
4. Built-in tools (**Google Search**, **Code Execution**) need **Gemini** and may need a **paid account**.
5. Google Search: `tools=[google_search]`. Code execution: `code_executor=BuiltInCodeExecutor()`.
6. Use **LangchainTool** to wrap LangChain tools like **Tavily** (works with any model).
7. For your own functions: **type hints + return type + good docstring + descriptive dict output**.
8. When mixing **built-in tools with other tools**, add the **server-side tool invocation** config.
9. The **refund agent** shows a real use: 6 function tools over a database plus a clear system prompt.
10. Next up: more tools, structured output, MCP, state and memory.