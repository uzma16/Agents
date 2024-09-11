from crewai import Crew
from textwrap import dedent
from .agents import ContentAgents
from .tasks import ContentTasks

from dotenv import load_dotenv
load_dotenv()

class ContentCrew:
    def __init__(self, description, min_word_length, max_word_length, platform):
        self.description = description
        self.min_word_length = min_word_length
        self.max_word_length = max_word_length
        self.platform = platform

    def run(self):
        agents = ContentAgents()
        tasks = ContentTasks()

        # Initialize agents
        content_creation_agent = agents.content_creation_agent()
        quality_assurance_agent = agents.quality_assurance_agent()
        # plagiarism_check_agent = agents.plagiarism_check_agent()
        # content_formatting_agent = agents.content_formatting_agent()
        # content_approver_agent = agents.content_approver_agent()

        # Define tasks
        create_content_task = tasks.create_content_task(
            content_creation_agent,
            self.platform,
            self.description,
            self.min_word_length,
            self.max_word_length
        )
        quality_assurance_task = tasks.quality_assurance_task(
            quality_assurance_agent,
            create_content_task.expected_output
        )
        # plagiarism_check_task = tasks.plagiarism_check_task(
        #     plagiarism_check_agent,
        #     quality_assurance_task.expected_output
        # )
        # formatting_task = tasks.content_formatting_task(
        #     content_formatting_agent,
        #     plagiarism_check_task.expected_output,
        #     self.platform
        # )
        # approval_task = tasks.content_approval_task(
        #     content_approver_agent,
        #     formatting_task.expected_output
        # )

        crew = Crew(
            agents=[
                content_creation_agent,
                quality_assurance_agent,
                # plagiarism_check_agent,
                # content_formatting_agent,
                # content_approver_agent
            ],
            tasks=[
                create_content_task,
                quality_assurance_task,
                # plagiarism_check_task,
                # formatting_task,
                # approval_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result
    
def main(platform, description, min_word_length, max_word_length):
    print("## Welcome to the Content Creation and Management System")
    print('-----------------------------------------------')

    content_crew = ContentCrew(description, min_word_length, max_word_length, platform)
    result = content_crew.run()
    print("\n\n########################")
    print("## Here is your Content Management Execution Result")
    print("########################\n")
    print(result)
    return result
