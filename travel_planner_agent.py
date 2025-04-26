import os
import pandas as pd
from agents import (
    Agent,
    Runner,
    function_tool,
    set_default_openai_key,
    WebSearchTool
)

# load api key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")
set_default_openai_key(api_key)

# load local datasets 
BASE = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE, "data")

df_cities = pd.read_csv(os.path.join(DATA_DIR, "worldcities.csv"))
unesco = pd.read_csv(os.path.join(DATA_DIR, "unesco_world_heritage.csv"))

# define tools 
@function_tool
def lookup_country(city: str) -> str:
    """Return the country (and subcountry) for a given city using the world cities dataset."""
    matches = df_cities[df_cities['name'].str.contains(city, case=False, na=False)]
    if matches.empty:
        return f"I couldn't find any country for the city '{city}'."
    # Drop duplicates by city, country, subcountry
    unique = matches.drop_duplicates(subset=['name', 'country', 'subcountry'])
    # Build output lines
    lines = [f"{row['name']} is in {row['country']} ({row['subcountry']})" for _, row in unique.iterrows()]
    return "\n".join(lines)

@function_tool
def search_attractions(location: str) -> str:
    """List up to 5 UNESCO World Heritage Sites matching the given location (country, region, or site name)."""
    df_filtered = unesco[
        unesco['states_name_en'].str.contains(location, case=False, na=False) |
        unesco['region_en'].str.contains(location, case=False, na=False) |
        unesco['name_en'].str.contains(location, case=False, na=False)
    ]
    if df_filtered.empty:
        return f"No UNESCO World Heritage Sites found for '{location}'."
    top = df_filtered[['name_en', 'states_name_en', 'category', 'date_inscribed']].head(5)
    lines = [
        f"{row['name_en']} ({row['category']}), {row['states_name_en']} - Inscribed: {row['date_inscribed']}"
        for _, row in top.iterrows()
    ]
    return "UNESCO World Heritage Sites:\n" + "\n".join(lines)

# agent setup
def main():
    agent = Agent(
        name="Lara's Travel Planner",
        instructions=(
            "You are a travel planning assistant. "
            "For flights or hotels, use the WebSearchTool hosted tool. "
            "For city-country lookups, use the lookup_country function tool. "
            "For UNESCO attractions, use the search_attractions function tool (do not use WebSearchTool for attractions)."
        ),
        tools=[
            WebSearchTool(),
            lookup_country,
            search_attractions,
        ],
    )

    print("Welcome to Travel Planner! Ask me about flights, hotels, or attractions.")
    while True:
        q = input(">> ").strip()
        if q.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        result = Runner.run_sync(agent, q)
        print(result.final_output)

if __name__ == "__main__":
    main()