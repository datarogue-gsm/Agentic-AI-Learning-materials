# This file contains code snippets for creating and using a weather tool with an agent in LangChain

import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

# Erro-handling-1 - Check API key is spaces or not
print("DEBUG: API Key Loaded:", bool(API_KEY))


# ---------------- TOOL ----------------
@tool
def get_weather(city: str) -> str:
    """
    Fetch the current weather information for a given city using WeatherAPI.

    This tool should be used when the user asks about:
    - Current weather conditions (e.g., temperature, climate)
    - Weather status in a specific city (e.g., "weather in London")
    - Real-time weather queries

    Input:
        city (str): Name of the city for which weather data is required.
                    Example: "London", "Bangalore", "New York"

    Output:
        str: A human-readable summary of the current weather including:
             - Temperature in Celsius
             - Weather condition (e.g., Sunny, Cloudy, Rainy)

    Example:
        Input: "London"
        Output: "Weather in London: 18°C, Partly cloudy."

    Notes:
    - This tool fetches real-time data from an external API.
    - If the API key is missing or invalid, it will return an error message.
    - If the city is not found, the API may return an error response.
    """
    # Erro-handling-2 - Check API key is available or not
    if not API_KEY:
        return "Error: API key missing. Check your .env file."

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)

    # Erro-handling-3 - Check whether the weather api request is successful or not
    if response.status_code != 200:
        return f"API error: {response.text}"

    data = response.json()
    temp = data["current"]["temp_c"]
    cond = data["current"]["condition"]["text"]
    return f"Weather in {city}: {temp}°C, {cond}."

@tool
def weather_advisor(condition: str, temperature: float) -> str:
    """
    Provide recommendations on what to do and what to avoid based on weather conditions.

    Use this tool when the user asks:
    - What should I do in this weather?
    - Is it safe to go outside?
    - Suggestions based on weather conditions

    Inputs:
        condition (str): Weather condition (e.g., Sunny, Rainy, Cloudy)
        temperature (float): Temperature in Celsius

    Output:
        str: Actionable advice including:
             - What to do
             - What to avoid
    """

    condition = condition.lower()

    advice = []

    # 🌧️ Rainy
    if "rain" in condition:
        advice.append("🌧️ Carry an umbrella or raincoat")
        advice.append("⚠️ Avoid outdoor activities")
        advice.append("🚗 Drive carefully due to slippery roads")

    # ☀️ Sunny / Hot
    elif "sun" in condition or temperature > 30:
        advice.append("☀️ Stay hydrated and drink water")
        advice.append("🧴 Use sunscreen")
        advice.append("⚠️ Avoid going out during peak afternoon heat")

    # ❄️ Cold
    elif temperature < 10:
        advice.append("🧥 Wear warm clothes")
        advice.append("🔥 Stay indoors if possible")
        advice.append("⚠️ Avoid prolonged exposure to cold")

    # 🌥️ Normal / Cloudy
    else:
        advice.append("👍 Weather is pleasant")
        advice.append("🚶 Good time for outdoor activities")
        advice.append("😊 Enjoy your day!")

    return "\n".join(advice)

# ---------------- LLM + AGENT ----------------
model = ChatOpenAI(model="gpt-4o-mini")

prompt_template = ChatPromptTemplate.from_template("""
You are a smart weather assistant.

You have two tools:
1. get_weather → fetch weather data
2. weather_advisor → give recommendations

Instructions:
- First call get_weather to fetch data
- Then use weather_advisor to provide suggestions
- Always combine both outputs into final answer

User Question:
{input}

Previous Steps:
{agent_scratchpad}

Final Answer:
""")

tools = [get_weather, weather_advisor]

agent = create_tool_calling_agent(
    llm=model,
    tools=tools,
    prompt=prompt_template
)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=5   
)


# ---------------- USER LOOP ----------------
print("\n🌦️ Weather Assistant Ready!")
print("👉 Type your question (e.g., 'weather in Bangalore')")
print("👉 Type 'quit' to exit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("👋 Exiting Weather Assistant. Goodbye!")
        break

    try:
        result = executor.invoke({"input": user_input})
        print("🤖:", result["output"])
    except Exception as e:
        # Erro-handling-4 - Check agent is failing in any step or not, if so, track/log in logger
        print("⚠️ Error:", str(e))