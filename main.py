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

    # Save output in a text file
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("=== CrewAI SEC Task Report ===\n")
        f.write("SEC Data: " + str(sec_data) + "\n")
        f.write("Insider Data: " + str(insider_data) + "\n")
        f.write("\n✅ Final Report:\n" + str(result) + "\n")

if __name__ == "__main__":
    main()
