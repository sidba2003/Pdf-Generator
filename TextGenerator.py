from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus import Spacer
import FontSetter


class TextGenerator:

    def __init__(self) -> None:
        self.text_setter = FontSetter()
        self.font_style = self.text_setter.setStyle(command=".normal")

        self.page_content = []

        self.commands = {".large", ".normal", ".italics", ".regular", ".indent", ".fill", ".nofill", ".bold"}

        self.document = SimpleDocTemplate("output.pdf", pagesize=letter)

    def handleLine(self, line: str) -> None:


