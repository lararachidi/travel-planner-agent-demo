# Travel Planner Agent Demo

An interactive command-line Travel Planner Agent built with the OpenAI Agents SDK and simple local datasets.

## Features

Agentic tool selection: dynamically chooses the right function based on your query

## Project Structure

travel_planner_agent/        # Project root
├── data/                    # Local CSV datasets
│   ├── worldcities.csv
│   ├── unesco_world_heritage.csv
├── travel_planner_agent.py  # Main agent script
├── requirements.txt         # Python dependencies
└── README.md                # This file

## Prerequisites

* Python 3.10+ (use pyenv or venv)
* An OpenAI API key
* Git (for cloning this repo)

## Setup

* Clone the repo:

git clone [https://github.com/your-username/travel_planner_agent-demo.git](https://github.com/lararachidi/travel-planner-agent-demo.git)
cd travel_planner_agent

## Create & activate a virtual environment

Example using pyenv-virtualenv:

pyenv install 3.13.0         
pyenv virtualenv 3.13.0 travel_planner_agent
pyenv activate travel_planner_agent

## Install dependencies

pip install -r requirements.txt

## Set your OpenAI API key

export OPENAI_API_KEY="sk-...your_key..."   # macOS/Linux

## Running the Agent

python travel_planner_agent.py

You should see something like this:

Welcome to Travel Planner! Ask me about flights, hotels, attractions, or current travel info.
=>

Type queries like:

* Where is Aachen? 
* What can I visit in Italy?
* How do I fly from London to Italy?

exit to quit

🧩 How It Works

Tools:

* lookup_country()

* search_attractions()

* WebSearchTool() for hotels or flights

The Agent uses the OpenAI Agents SDK to choose which tool to call based on your natural language prompt.

## Dependencies

openai-agents — OpenAI Agents SDK

pandas — Data loading & manipulation

See requirements.txt 
