try:
    from ..llm import get_model
    from ..utils.db import *
    from ..llm_settings import llm_settings
    from ..tooler import *
    from ..display_tools import *
    from ..cu.computer import *
    from ..teams import *
    from .agent_tools import get_tools
    from ..mcp.tool import mcp_tools
    from ..standard_tools import get_standard_tools
    from .Memory_System import add_tool,search_tool

except ImportError:
    from core.llm import get_model
    from core.utils.db import *
    from core.llm_settings import llm_settings
    from core.tooler import *
    from core.display_tools import *
    from core.cu.computer import *
    from core.teams import *
    from core.agent.agent_tools import get_tools
    from core.mcp.tool import mcp_tools
    from core.standard_tools import get_standard_tools
    from core.agent.Memory_System import add_tool,search_tool


from langgraph.prebuilt import chat_agent_executor


custom_tools_ = []


def custom_tools():
    global custom_tools_
    the_list = []
    the_list += custom_tools_
    return the_list


prompt_cache = {}


def get_prompt(name):
    global prompt_cache
    if name in prompt_cache:
        return prompt_cache[name]
    else:
        from langchain import hub

        prompt = hub.pull(name)
        prompt_cache[name] = prompt
        return prompt


def get_agent_executor(the_anthropic_model=False, no_tools=False):
    tools = get_tools()
    tools += custom_tools()

    model = load_model_settings()

    if is_predefined_agents_setting_active() and llm_settings[model]["tools"]:
        try:
            import crewai

            tools += [search_on_internet_and_report_team, generate_code_with_aim_team]
        except ImportError:
            pass


    if the_anthropic_model:
        tools += []
        if load_aws_access_key_id() == "default":
            model_catch = get_model(the_model="claude-3-5-sonnet-20241022")
        else:
            model_catch = get_model(the_model="us.anthropic.claude-3-5-sonnet-20241022-v2:0")

        return chat_agent_executor.create_tool_calling_executor(model_catch, tools)
    else:
        tools += [mouse_scroll, click_to_text, click_to_icon, click_to_area, screenshot] + mcp_tools() + get_standard_tools()



    if no_tools:
        tools = []
    tools+=[app_opener,app_closer,search_tool]
    if (
        llm_settings[model]["provider"] == "openai"
        or llm_settings[model]["provider"] == "groq"
        or llm_settings[model]["provider"] == "azureai"
        or llm_settings[model]["provider"] == "anthropic"
        or llm_settings[model]["provider"] == "aws"
    ):
        return chat_agent_executor.create_tool_calling_executor(get_model(), tools)

    if llm_settings[model]["provider"] == "ollama":
        return chat_agent_executor.create_tool_calling_executor(get_model(), tools)



