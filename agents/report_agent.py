from crewai import Agent

report_agent = Agent(
    role="Report Generator",
    goal="Combine SEC + Insider trading data into a summarized report",
    backstory="Specialist in financial reporting and market insights.",
    llm=None, 
    verbose=True
)
