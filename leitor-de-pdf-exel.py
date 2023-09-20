import PyPDF2
import tabula
import pandas as pd

# Função para extrair tabelas do PDF e convertê-las para Excel
def pdf_to_excel(pdf_file, excel_file):
    # Abre o arquivo PDF
    with open(pdf_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        # Extrai as tabelas de cada página do PDF
        all_tables = []
        for page_number in range(num_pages):
            tables = tabula.read_pdf(pdf_file, pages=page_number + 1, multiple_tables=True)
            all_tables.extend(tables)

        # Concatena todas as tabelas em um único DataFrame
        if all_tables:
            df = pd.concat(all_tables, ignore_index=True)
            
            # Salva o DataFrame como um arquivo Excel
            df.to_excel(excel_file, index=False, engine='openpyxl')

# Nome do arquivo PDF de entrada e arquivo Excel de saída
pdf_file = 'seu_arquivo.pdf'
excel_file = 'saida.xlsx'

# Chama a função para converter o PDF para Excel
pdf_to_excel(pdf_file, excel_file)

print(f'Conversão concluída. Os dados do PDF foram salvos em {excel_file}.')
