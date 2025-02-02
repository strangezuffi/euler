import csv

def split_csv_by_key(input_file, output_prefix):
    """
    Trennt eine CSV-Datei anhand eines Schlüssels in Feld 1 (Position 20-letzte Pos vor erstem Space).

    Args:
        input_file (str): Pfad zur Eingabedatei.
        output_prefix (str): Präfix für die Ausgabedateien.
    """

    output_files = {}

    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader)  # Überspringe erste Zeile
        next(reader)  # Überspringe zweite Zeile


        for row in reader:
            if len(row) > 0:
                feld1 = row[0]
                start = 20 # Startposition des Schlüssels)
                ende = feld1.find(' ', start)
                if ende == -1:
                    ende = len(feld1)
                key = row[0][start:ende]  # Extrahiere den Schlüssel aus Feld 1 (Position 20-24)

                row[0] = row[0][20:-1]

                if key not in output_files:
                    output_files[key] = open(f"{output_prefix}_{key}.csv", 'w', newline='', encoding='utf-8')
                writer = csv.writer(output_files[key], delimiter='\t')
                writer.writerow(row)  # Schreibe die Zeile in die entsprechende Ausgabedatei

    for file in output_files.values():
        file.close()

# Beispielaufruf
split_csv_by_key("/home/zuffi/workbench/inforec.csv", "output")
