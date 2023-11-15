from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class FontSetter:

    def __init__(self):
        self.styles = getSampleStyleSheet()

        # the default values for the text style and font
        self.style = "normal"
        self.font = 12
        self.indent = 0

        self.commands = {".large": self.setTextFormat("bold", 15),
                         ".normal": self.setTextFormat(self.style, 12),
                         ".italics": self.setTextFormat("italics", self.font),
                         ".regular": self.setTextFormat(self.style, 12),
                         ".indent": self.setTextFormat(self.style, 12),
                         ".fill": self.setTextFormat(self.style, 12),
                         ".nofill": self.setTextFormat(self.style, 12),
                         ".bold": self.setTextFormat(self.style, 12)}

    def setStyle(self, command: str, style: str, font: int, indent: int):
        if command in self.commands:
            return self.commands[command](style, font, indent)
        raise ValueError("Please check the command. The provided command is", command)

    def setTextFormat(self, style, font, indent):

        # updating the text style values
        self.style, self.font, self.indent = style, font, indent

        custom_style = ParagraphStyle(
            'Custom_Style',
            parent=self.styles[style],
            fontName='Helvetica',
            fontSize=font,
            leading=15,
            leftIndent=indent
        )
        return custom_style