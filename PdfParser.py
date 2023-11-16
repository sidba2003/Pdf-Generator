import os.path

import PyPDF2
from TextGenerator import TextGenerator
import sys
from os import path


class PdfParser:

    def __init__(self, file) -> None:
        self.generator = TextGenerator()
        self.file = file

    def computePdf(self) -> None:
        with open(self.file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()
                page_lines = page_text.split("\n")
                for line in page_lines:
                    self.generator.handleLine(line)
            self.generator.addContentsToDocument()

        self.__printOutputLocation()


    def __printOutputLocation(self) -> None:
        output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output.pdf")

        print("PDF file generated successfully!")
        print("The generated PDF file is located at", output_file_path)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("Please enter the correct number of arguments. Required 1, passed", len(sys.argv) - 1)
    parser = PdfParser(sys.argv[1])
    parser.computePdf()
