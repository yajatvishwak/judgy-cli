from pypdf import PdfReader


class PDFParser:
    def __init__(self) -> None:
        pass

    def get_pdf_content(self, pdf_link):
        try:
            reader = PdfReader(pdf_link)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extract_text()
            pdf_text = bytes(pdf_text, "utf-8").decode("utf-8", "ignore")
            return {"text": pdf_text}
        except Exception as e:
            print("failed for {}".format(pdf_link))
            raise e
            return {"text": ""}
