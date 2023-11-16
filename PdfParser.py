import PyPDF2
from TextGenerator import TextGenerator
import sys


class PdfParser:

    def __init__(self, file) -> None:
        self.generator = TextGenerator()
        self.file = file

    def parsePdf(self) -> None:
        with open(self.file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()
                page_lines = page_text.split("\n")
                for line in page_lines:
                    self.generator.handleLine(line)
            self.generator.addContentsToDocument()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("Please enter the correct number of arguments. Required 1, passed", len(sys.argv))
    parser = PdfParser(sys.argv[1])
    parser.parsePdf()
