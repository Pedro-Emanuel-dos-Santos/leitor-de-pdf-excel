# Leitor de PDF com Conversão para Excel

Este é um leitor de PDF em Python que extrai tabelas de um arquivo PDF e converte essas tabelas em um arquivo Excel. Ele utiliza as bibliotecas PyPDF2, tabula-py e pandas para realizar essa tarefa.

## Tabela de Conteúdo

- [Visão Geral](#visão-geral)
- [Instalação](#instalação)
- [Uso](#uso)

## Visão Geral

Este projeto permite a extração de dados tabulares de arquivos PDF e a conversão desses dados em um arquivo Excel (.xlsx). É útil quando você precisa trabalhar com tabelas de PDFs em planilhas Excel para análise de dados, relatórios, etc.

## Instalação

Certifique-se de ter as bibliotecas necessárias instaladas em seu ambiente Python. Você pode instalá-las usando o seguinte comando:

```shell
pip install PyPDF2 tabula-py pandas openpyxl

## Uso

Para usar o leitor de PDF com conversão para Excel, siga estas etapas:

1. Coloque seu arquivo PDF (seu_arquivo.pdf) na pasta do projeto.

2. Execute o script pdf_to_excel.py: python pdf_to_excel.py


O script lerá o PDF, extrairá tabelas e as salvará em um arquivo Excel chamado saida.xlsx na mesma pasta do projeto.
Nota: Certifique-se de que o arquivo PDF contenha tabelas tabulares que possam ser extraídas.
