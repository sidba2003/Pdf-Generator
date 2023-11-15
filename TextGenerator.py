from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
import FontSetter


class TextGenerator:

    def __init__(self) -> None:
        self.text_setter = FontSetter()
        self.commands = {".large", ".normal", ".italics", ".regular", ".indent", ".fill", ".nofill", ".bold"}
        self.font_style = self.text_setter.setStyle(".normal")
        self.document = SimpleDocTemplate("output.pdf", pagesize=letter)

    def handleLine(self, line: str) -> None:

