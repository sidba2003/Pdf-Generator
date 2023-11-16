from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY


class FontSetter:

    def __init__(self):
        self.styles = getSampleStyleSheet()

        # the default values for the text style and font
        self.style = "Normal"
        self.font = 12
        self.indent = 0
        self.alignment = TA_LEFT

        self.commands = {".large": lambda: self.setTextFormat("Heading1", 15, self.indent, self.alignment),
                         ".normal": lambda: self.setTextFormat(self.style, 12, self.indent, self.alignment),
                         ".italics": lambda: self.setTextFormat("Italic", self.font, self.indent, self.alignment),
                         ".regular": lambda: self.setTextFormat("Normal", self.font, self.indent, self.alignment),
                         ".indent": lambda: self.setTextFormat(self.style, self.font, self.indent, self.alignment),
                         ".fill": lambda: self.setTextFormat(self.style, self.font, self.indent, TA_JUSTIFY),
                         ".nofill": lambda: self.setTextFormat(self.style, self.font, self.indent, TA_LEFT),
                         ".bold": lambda: self.setTextFormat("Heading1", self.font, self.indent, self.alignment)}

    def setStyle(self, command: str, indent=0):
        if command in self.commands:
            self.indent = self.indent + (indent * 10)
            return self.commands[command]()
        raise ValueError("Please check the command. The provided command is", command)

    def setTextFormat(self, style, font, indent, alignment):
        # updating the text style values
        self.style, self.font, self.alignment = style, font, alignment

        custom_style = ParagraphStyle(
            'Custom_Style',
            parent=self.styles[style],
            fontName='Helvetica',
            fontSize=font,
            leading=15,
            leftIndent=indent,
            alignment=alignment
        )
        return custom_style
