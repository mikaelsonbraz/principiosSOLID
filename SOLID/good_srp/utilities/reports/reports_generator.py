from ..reports.html_generator import HTMLGenerator
from ..reports.markdown_generator import MarkdownGenerator

class ReportsGenerator:

    @classmethod
    def build(cls, type, repos):
        if str.upper(type).__eq__("HTML"):
            return HTMLGenerator.build(repos)
        elif str.upper(type).__eq__("MARKDOWN") or str.upper(type).__eq__("MD"):
            return MarkdownGenerator.build(repos)
        else:
            return "Invalid type report"