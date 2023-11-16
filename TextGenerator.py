from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from FontSetter import FontSetter


class TextGenerator:

    def __init__(self) -> None:
        self.text_setter = FontSetter()
        self.font_style = self.text_setter.setStyle(command=".normal")

        self.line = []

        self.page_content = []

        self.commands = {".large", ".normal", ".italics", ".regular", ".indent", ".fill", ".nofill", ".bold"}

        self.document = SimpleDocTemplate("output.pdf", pagesize=letter)

    def handleLine(self, line: str) -> None:
        if line[0] == ".":
            self.__addParagraph()
            command_values = line.split(" ")
            cmd = command_values[0]
            if cmd == ".paragraph":
                self.page_content.append(Paragraph("&nbsp;", self.font_style))
            elif cmd == ".indent":
                if len(command_values) < 2:
                    raise ValueError("Please enter the correct command along with its values")
                self.font_style = self.text_setter.setStyle(command=cmd, indent=int(command_values[1]))
            else:
                self.font_style = self.text_setter.setStyle(command=cmd)
        else:
            self.line.append(line)

    def __addParagraph(self):
        if self.line:
            print(self.line)
            paragraph = Paragraph(" ".join(self.line), self.font_style)
            self.page_content.append(paragraph)
            self.line.clear()

    def addContentsToDocument(self) -> None:
        self.__addParagraph()
        self.document.build(self.page_content)
