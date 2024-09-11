from crewai import Agent, Task
from langchain.tools import tool

class StyleApplicationTool:
    @staticmethod
    @tool("Apply specific style guidelines")
    def apply_style(text):
        """Applies specific style rules to the text to ensure consistency with predefined stylistic guidelines."""
        text = StyleApplicationTool.apply_oxford_comma(text)
        text = StyleApplicationTool.capitalize_sentences(text)
        return text

    @staticmethod
    def apply_oxford_comma(text):
        """Ensures the use of Oxford commas in lists within the text."""
        import re
        # Regex to find list items and add an Oxford comma if missing
        pattern = r"(\w+), (\w+) and (\w+)"
        replacement = r"\1, \2, and \3"
        text = re.sub(pattern, replacement, text)
        return text

    @staticmethod
    def capitalize_sentences(text):
        """Capitalizes the first letter of each sentence."""
        import re
        # Regex to capitalize the first character of each sentence
        return re.sub(r'(?<!\w)([a-zA-Z])', lambda x: x.group().upper(), text)
