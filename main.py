import PyPDF2;
from buscas import Buscas

# ===================================OBTER PARAMETROS DE ENTRADA============================================

# Abre o arquivo PDF
pdf_file = open("C:\\Users\\vitor\\OneDrive\\Área de Trabalho\\TESTE HISTORICOS\\ID-1140084993-2201-GESTÃO ESTRAT MARKETING CASD.pdf", 'rb')
# Cria o objeto PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)
# Obtém o número de páginas
num_pages = len(pdf_reader.pages)

for i in range(num_pages):
    page = pdf_reader.pages[i]
    # ===================================ANALISAR NOME============================================
    nome = Buscas.BuscarCampoAZ("Nome:", "RA:", 6, page)
    #===================================ANALISAR RA===============================================
    ra = Buscas.BuscarCampoRanged(15,"RA:",4,page)
    #===================================ANALISAR DATA DE NASCIMENTO===============================
    data_nascimento = Buscas.BuscarCampoRanged(30, "Data de nascimento:", 20,page)
    #===================================NACIONALIDADE=============================================
    natural_do_estado = Buscas.BuscarCampoAZ("Natural do Estado:", "Nacionalidade:", 19, page)
    #===================================NACIONALIDADE=============================================
    nacionalidade = Buscas.BuscarCampoAZ("Nacionalidade:","RG nº",15,page)
    # ===================================BUSCAR RG================================================
    rg = Buscas.BuscarCampoRanged(21, "RG nº", 6, page)
    # ===================================VERIFICAR CARGA HORARIA DO CURSO=========================
    result_cargas_horarias = Buscas.VerificarCh(page)
    # ===================================VERIFICAR O PREENCHIMENTO================================
    result_preenchimento_componentes = Buscas.VerificarPreenchimentoDeComponentes(page)
    # ===================================VERIFICAR SE CONSTA APROVEITAMENTO DE ESTUDOS============

# Fecha o arquivo PDF
pdf_file.close()