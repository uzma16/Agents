from crewai import Task
from textwrap import dedent


class ContentTasks():
    def create_content_task(self, agent, platform, description, min_word_length, max_word_length):
        return Task(
            description=dedent(f"""
                Generate engaging and platform-optimized content for {platform}. The content should be tailored to the platform's audience and adhere to its specific formatting and content guidelines.

                The content must be compelling, providing valuable insights and narratives that resonate with the audience. It should also be optimized for SEO if applicable, incorporating relevant keywords to enhance visibility and engagement.

                Platform: {platform}
                Content Description/Title/Topic: {description}
                Minimum Word Length: {min_word_length}
                Maximum Word Length: {max_word_length}
                Ensure the content strictly adheres to the specified word count range to maintain the effectiveness and appropriateness for the platform. No need to give any extra thing other than content.
            """),
            agent=agent,
            expected_output=f"A fully tailored, engaging, and platform-optimized post ready for publication on {platform}. The content should strictly meet the word count range, with a minimum of {min_word_length} words and a maximum of {max_word_length} words, incorporating the provided descriptions and adhering to the platform's content guidelines."
        )

    # def create_content_task(self, agent, platform, description, min_word_length, max_word_length):
    #     return Task(
    #         description=dedent(f"""
    #             Generate engaging and platform-optimized content for {platform}. The content should be tailored to the platform's audience and adhere to its specific formatting and content guidelines.

    #             The content must be compelling, providing valuable insights and narratives that resonate with the audience. It should also be optimized for SEO if applicable, incorporating relevant keywords to enhance visibility and engagement.

    #             Platform: {platform}
    #             Content Description/Title/Topic: {description}
    #             Minimum Word Length: {min_word_length}
    #             Maximum Word Length: {max_word_length}
    #             No need to give any extra thing other then content.
    #                         """),
    #         agent=agent,
    #         expected_output=f'A fully tailored, engaging, and platform-optimized post ready for publication on {platform}, incorporating the provided descriptions and adhering to the specified word length criteria.'
    #     )

# Note: Utilize tools for NLP generation and, if applicable, SEO optimization and platform-specific formatting, to ensure the content meets all quality and engagement metrics.


    def quality_assurance_task(self, agent, content):
        return Task(
            description=dedent(f"""
                Perform a detailed review of the provided content to ensure it meets the highest editorial standards. The review should cover grammar, coherence, clarity, and adherence to the specified editorial guidelines.

                The task involves using advanced NLP tools to identify and correct grammatical errors, enhance readability, and ensure stylistic consistency across the text. The content should be polished to remove any ambiguities or inconsistencies, making it suitable for its intended audience and platform.

                Content to be reviewed: The content provided is '{content}'.

                            """),
            agent=agent,
            expected_output='The content revised to be grammatically correct, coherent, clear, and beautifully formatted, adhering to all specified editorial guidelines and ready for publication.'
        )
    
#Note: Utilize the GrammarCheckTool to systematically check and correct grammar issues. Ensure that all edits preserve the original meaning of the content while enhancing its presentation and readability.

    def plagiarism_check_task(self, agent, content):
        return Task(
            description=dedent(f"""
                Conduct a thorough plagiarism check on the provided content to ensure that it is original and properly cites all sources. The process should detect any potential plagiarism and flag parts of the text that may need citation or rewriting to comply with copyright laws.

                Content to be reviewed: The provided content for review is: '{content}'.

                The task requires identifying instances of copied or improperly cited text using advanced AI-driven tools. This includes comparing the content against a database of existing materials to ensure no unintentional duplication or infringement has occurred.

                Note: Utilize the PlagiarismDetectionTool to scan the content for plagiarism. Ensure that any findings are reported with suggestions for correction or modification to maintain the integrity and originality of the content.
            """),
            agent=agent,
            expected_output='A thoroughly revised version of the content that is free from any plagiarism. This revision should address all identified instances of potential copyright infringement by either rephrasing, paraphrasing, or properly citing the sources. The output must ensure that the text not only avoids direct plagiarism but also maintains the original intent and style of the content while adhering to all relevant copyright laws. .'
        )

    def content_formatting_task(self, agent,content, platform):
        return Task(
            description=dedent(f"""
                Apply precise formatting to the provided content to ensure it matches the stylistic and structural standards required for the specified publication platform. The formatting task should focus on enhancing the content’s readability and visual appeal according to the guidelines of {platform}.

                Content to be formatted: The provided content for formatting is: '{content}'.
                Platform: {platform}

                This task includes adjusting fonts, spacing, layout, and other stylistic elements to make the content visually appealing and compliant with the platform's requirements. The goal is to create a professionally formatted piece that engages readers and adheres to all specified formatting guidelines.

                Note: Utilize the StyleApplicationTool to apply the necessary style transformations. Ensure that all adjustments preserve the content’s integrity while enhancing its presentation.
            """),
            agent=agent,
            expected_output=f'Content professionally formatted for {platform}, meeting all specified guidelines for style and layout, and ready for publication.'
        )
    

    def content_approval_task(self, agent, content):
        return Task(
            description=dedent(f"""
                Conduct a comprehensive review of the provided content to ensure that it complies with all legal, regulatory, and company standards before publication. The review process should thoroughly assess the content's adherence to the specified guidelines, identifying any areas where adjustments may be needed to meet these standards.

                Content to be approved: The provided content for approval is: '{content}'.

                The task involves a detailed examination of the text for compliance with the guidelines, maintaining the integrity and professionalism of the content. By ensuring that all content is up to standards, this role helps safeguard the organization's reputation and legal standing.

                Note: Utilize the ComplianceCheckTool to systematically check and ensure compliance issues are addressed. Report any findings with specific recommendations for necessary adjustments to ensure the content meets all regulatory requirements.
            """),
            agent=agent,
            expected_output='A comprehensive compliance report detailing any issues found and confirming that the content meets all specified guidelines for legal and regulatory compliance, ready for publication.'
        )



