from gtts import gTTs
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', lanquage='en'):
   if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
       return 'File exists!'
   else:
       return 'File not exists, check the file path!'

   def main():
       print(pdf_to_mp3(file_path='\Users\Andry\PycharmProjects\myProjectsgit\PDF_to-MP3\pdf_files\geely-atlas.pdf'))


if __name__ == '__main__':
    main()
