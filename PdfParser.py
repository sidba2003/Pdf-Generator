import PyPDF2
from TextGenerator import TextGenerator


class PdfParser:

    def __init__(self) -> None:
        self.generator = TextGenerator()

    def parsePdf(self) -> None:
        with open('instructions.pdf', 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()
                page_lines = page_text.split("\n")
                for line in page_lines:
                    self.generator.handleLine(line)
            self.generator.addContentsToDocument()


if __name__ == '__main__':
    parser = PdfParser()
    parser.parsePdf()
