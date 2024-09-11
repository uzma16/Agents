from textwrap import dedent

def analyze_content_task(self, agent, content):
    return Task(
        description=dedent(f"""
            Analyze the provided content to extract key themes, sentiments, and contextual cues. This analysis will identify areas that may require commenting, modification, or deletion to enhance dialogue quality and maintain relevance.

            Content to Analyze: {content}
            
            The goal is to ensure that all interactions with the content are appropriate and contribute positively to the discussion, adhering to the community guidelines and platform standards. This task will inform subsequent actions by other agents in the team, such as the Comment Generation Agent or the Comment Approver Agent.
            
            Note: Utilize the agent's tools for theme extraction and sentiment analysis to perform a thorough review of the content. The insights gained will guide the strategic placement of comments, suggest edits, or identify potential deletions.
        """),
        agent=agent,
        expected_output='A detailed report of the analysis, including recommendations for comments, edits, or deletions, ensuring that all content interactions are constructive and contextually appropriate.'
    )

from textwrap import dedent

def generate_comment_task(self, agent, content, context_analysis):
    return Task(
        description=dedent(f"""
            Generate thoughtful and relevant comments for the provided content based on the detailed context analysis. The comments should be engaging and designed to foster a positive and informative dialogue among users.

            Content to Comment On: {content}
            Context Analysis Report: {context_analysis}
            
            The goal is to use the insights from the context analysis to create comments that are not only pertinent to the discussion but also enhance user interaction and engagement. These comments should reflect a deep understanding of the content's themes and the sentiments expressed in it, aligning with the platform's tone and community standards.

            Note: Utilize the agent's text generation tool to craft comments that are appropriate for the audience and the context of the discussion. Ensure that each comment adds value and adheres to the ethical guidelines of the platform.
        """),
        agent=agent,
        expected_output='A set of well-crafted, engaging, and contextually relevant comments ready for review and publication.'
    )


from textwrap import dedent

def approve_comment_task(self, agent, comments):
    return Task(
        description=dedent(f"""
            Review the generated comments to ensure they meet the established quality and community standards before they are published. Each comment should be evaluated for its appropriateness, relevance, and contribution to constructive dialogue.

            Comments to Approve: {comments}
            
            The goal of this task is to scrutinize the comments carefully to confirm that they are positive, relevant, and adhere to the platform's rules and guidelines. This includes checking for any potential violations of content policies, ensuring that the comments are respectful of all community members, and aligning with the overall tone of the discussion.

            Note: Utilize the agent's text evaluation tool to assess each comment for quality, appropriateness, and engagement potential. This review process is crucial for maintaining the integrity of the platform and fostering a healthy, engaging community environment.
        """),
        agent=agent,
        expected_output='A report detailing each comment's approval status, including any necessary feedback or recommendations for revisions before publication.'
    )
