import os 
os.environ["OPENAI_API_KEY"] = "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"
from crewai import Task, Crew
from agents.sec_agent import sec_agent
from agents.insider_agent import insider_agent
from agents.report_agent import report_agent
from utils.fetch_sec import get_sec_data
from utils.fetch_insider import get_insider_data

def main():
    # Dummy data for testing (replace with real fetching later)
    sec_data = get_sec_data()
    insider_data = get_insider_data()

    print("SEC Data:", sec_data)
    print("Insider Data:", insider_data)

    # Define tasks with expected_output
    sec_task = Task(
        description="Fetch SEC filings from the last 48 hours",
        expected_output="List of SEC fillings with company name and filing count", 
        agent=sec_agent
    )

    insider_task = Task(
        description="Fetch insider trading activity from the SEC site (last 48 hours)",
        expected_output="List of insider trading transactions with company name and count",
        agent=insider_agent
    )

    report_task = Task(
        description="Generate a summarized report combining SEC and Insider data",
        expected_output="Final report summarizing company name, filings, insider trades, and trends",
        agent=report_agent
    )

    # Crew Flow
    crew = Crew(
        agents=[sec_agent, insider_agent, report_agent],
        tasks=[sec_task, insider_task, report_task],
        verbose=True
    )

    # Run workflow
    result = crew.kickoff()
    print("\n✅ Final Report:\n", result)

if __name__ == "__main__":
    main()
   

 


