from crewai import Agent

insider_agent = Agent(
    role="Insider Trading Analyst",
    goal="Scrape insider trading activity in last 48 hours",
    backstory="Monitors insider activity to detect unusual trading patterns.",
    llm=None, 
    verbose=True
)
