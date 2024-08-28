import csv
import os

import docx


CSV_PATH = "data"
DOCX_PATH = "result"
DELIMITER = "|"


def allowed_file(filename: str, allowed_extensions: tuple[str, ...]) -> bool:
    """
    Check a file extension
    :param filename: a file name
    :param allowed_extensions: a list of valid file extensions
    :return: an allowed file extension flag
    """
    return "." in filename and filename.rsplit(".", 1)[1] in allowed_extensions


if __name__ == "__main__":
    if not os.path.exists(CSV_PATH):
        os.makedirs(CSV_PATH)

    if not os.path.exists(DOCX_PATH):
        os.makedirs(DOCX_PATH)

    for _, _, files in os.walk(CSV_PATH):
        for file in files:
            if not allowed_file(file, ("csv",)):
                continue

            with open(CSV_PATH + "/" + file, newline="", encoding="utf-8") as f:
                csv_reader = csv.reader(f, delimiter=DELIMITER)

                csv_headers = next(csv_reader)
                csv_cols = len(csv_headers)

                doc = docx.Document()
                table = doc.add_table(rows=1, cols=csv_cols)
                hdr_cells = table.rows[0].cells

                for i in range(csv_cols):
                    hdr_cells[i].text = csv_headers[i]

                for row in csv_reader:
                    row_cells = table.add_row().cells
                    for i in range(csv_cols):
                        row_cells[i].text = row[i]

            doc.add_page_break()
            result_path = DOCX_PATH + "/" + os.path.splitext(file)[0] + ".docx"
            doc.save(result_path)
            print("Save DOCX files:")
            print(result_path)
