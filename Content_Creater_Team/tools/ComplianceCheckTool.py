from crewai import Agent, Task
from langchain.tools import tool

class ComplianceCheckTool:
    @staticmethod
    @tool("Verify compliance with regulatory and company standards")
    def verify_compliance(text, standards):
        """Automatically checks if the text complies with the provided regulatory and company standards."""
        # Assume standards is a dictionary of {keyword: compliance requirement}
        compliance_issues = []

        for keyword, requirement in standards.items():
            if keyword in text:
                if not ComplianceCheckTool.check_requirement(text, keyword, requirement):
                    compliance_issues.append(f"Non-compliance found for {keyword}")
            else:
                compliance_issues.append(f"{keyword} not mentioned, which is required.")

        if compliance_issues:
            return "Issues detected: " + "; ".join(compliance_issues)
        else:
            return "No compliance issues detected."

    @staticmethod
    def check_requirement(text, keyword, requirement):
        """Placeholder function to simulate checking compliance requirements."""
        # Example logic: check if the requirement specifies a minimum mention count
        if 'min_count' in requirement:
            count = text.count(keyword)
            if count < requirement['min_count']:
                return False
        return True
