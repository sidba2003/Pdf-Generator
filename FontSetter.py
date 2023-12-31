from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY


class FontSetter:
    def __init__(self) -> None:
        self.styles = getSampleStyleSheet()

        # the default values for the text style and font
        self.style = "Normal"
        self.font = 12
        self.indent = 0
        self.alignment = TA_LEFT

        self.commands = {".large": lambda: self.__setTextFormat("Heading1", 15, self.indent, self.alignment),
                         ".normal": lambda: self.__setTextFormat(self.style, 12, self.indent, self.alignment),
                         ".italics": lambda: self.__setTextFormat("Italic", self.font, self.indent, self.alignment),
                         ".regular": lambda: self.__setTextFormat("Normal", self.font, self.indent, self.alignment),
                         ".indent": lambda: self.__setTextFormat(self.style, self.font, self.indent, self.alignment),
                         ".fill": lambda: self.__setTextFormat(self.style, self.font, self.indent, TA_JUSTIFY),
                         ".nofill": lambda: self.__setTextFormat(self.style, self.font, self.indent, TA_LEFT),
                         ".bold": lambda: self.__setTextFormat("Heading1", self.font, self.indent, self.alignment)}

    def setStyle(self, command: str, indent=0) -> ParagraphStyle:
        if command in self.commands:
            self.indent = self.indent + (indent * 10)
            return self.commands[command]()
        raise ValueError("Please check the command. The provided command is", command)

    def __setTextFormat(self, style, font, indent, alignment) -> ParagraphStyle:
        # updating the text style values
        self.style, self.font, self.alignment = style, font, alignment

        font_name = 'Helvetica-Bold' if style == "Heading1" else 'Helvetica-Oblique' if style == "Italic" else 'Helvetica'

        custom_style = ParagraphStyle(
            'Custom_Style',
            parent=self.styles[style],
            fontName=font_name,
            fontSize=font,
            leading=15,
            leftIndent=indent,
            alignment=alignment
        )
        return custom_style
