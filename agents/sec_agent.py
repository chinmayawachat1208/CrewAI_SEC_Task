from crewai import Agent

sec_agent = Agent(
    role="SEC Data Analyst",
    goal="Collect SEC filings from last 48 hours",
    backstory="Expert in analyzing SEC financial filings.",
    llm=None,
    verbose=True
)
