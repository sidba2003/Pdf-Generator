from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class FontSetter:

    def __init__(self):
        self.styles = getSampleStyleSheet()

        self.style = "normal"
        self.commands = {".large": self.setTextFormat("bold", 15),
                         ".normal": self.setTextFormat(self.style, 12),
                         ".italics": self.setTextFormat(self.style, 12),
                         ".regular": self.setTextFormat(self.style, 12),
                         ".indent": self.setTextFormat(self.style, 12),
                         ".fill": self.setTextFormat(self.style, 12),
                         ".nofill": self.setTextFormat(self.style, 12),
                         ".bold": self.setTextFormat(self.style, 12)}

    def setStyle(self, command: str, style: str, font: int):
        if command in self.commands:
            return self.commands[command](style, font)
        raise ValueError("Please check the command. The provided command is", command)

    def setTextFormat(self, style, font):
        custom_style = ParagraphStyle(
            'Custom_Style',
            parent=self.styles[style],
            fontName='Helvetica',
            fontSize=font,
            leading=15
        )
        return custom_style
