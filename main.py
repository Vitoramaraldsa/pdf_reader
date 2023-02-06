import PyPDF2;
from buscas import Buscas
from aluno import Aluno

# ===================================OBTER PARAMETROS DE ENTRADA============================================

#caminho do pdf
with open('C:\\Users\\vitor\\OneDrive\\Área de Trabalho\\TESTE HISTORICOS\\ENTRADAS\\pdfPath.txt', 'r', encoding='UTF-8') as arquivo:
    conteudo = arquivo.read()
    pathPdf = str(conteudo)



# Abre o arquivo PDF
pdf_file = open(pathPdf, 'rb')
# Cria o objeto PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)
# Obtém o número de páginas
num_pages = len(pdf_reader.pages)

for i in range(num_pages):
    page = pdf_reader.pages[i]
    # ===================================ANALISAR NOME============================================
    Aluno.nome = Buscas.BuscarCampoAZ("Nome:", "RA:", 6, page)
    #===================================ANALISAR RA===============================================
    Aluno.ra = Buscas.BuscarCampoRanged(15,"RA:",4,page)
    #===================================ANALISAR DATA DE NASCIMENTO===============================
    Aluno.data_nascimento = Buscas.BuscarCampoRanged(30, "Data de nascimento:", 20,page)
    #===================================NACIONALIDADE=============================================
    Aluno.natural_do_estado = Buscas.BuscarCampoAZ("Natural do Estado:", "Nacionalidade:", 19, page)
    #===================================NACIONALIDADE=============================================
    Aluno.nacionalidade = Buscas.BuscarCampoAZ("Nacionalidade:","RG nº",15,page)
    # ===================================BUSCAR RG================================================
    Aluno.rg = Buscas.BuscarCampoRanged(21, "RG nº", 6, page)
    #===================================VERIFICAR CARGA HORARIA DO CURSO==========================
    Aluno.result_cargas_horarias = Buscas.VerificarCh(page)
    #===================================VERIFICAR O PREENCHIMENTO=================================
    Aluno.result_preenchimento_componentes = Buscas.VerificarPreenchimentoDeComponentes(page)
    #===================================VERIFICAR SE CONSTA APROVEITAMENTO DE ESTUDOS=============
    Aluno.aproveitamento_estudos = Buscas.VerificarAproveitamentoEstudos(page)
    #===================================VERIFICAR PERIODO E REALIZACAO============================
    Aluno.periodo_realizacao = Buscas.BuscarCampoRanged(46, "Período de realização:", 22, page)
    #===================================CAPTURAR TITULO DO TCC====================================
    Aluno.titulo_tcc = Buscas.BuscarCampoAZ("Título do TCC:", "Nota:", 14, page)
    #===================================CAPTURAR NOTA=============================================
    Aluno.nota = Buscas.BuscarCampoAZ("Nota:", "Declaramos que", 5, page)
    #===================================EXIBIR ALUNO COMPLETO=====================================
    print("Nome: " + Aluno.nome)
    print("Ra: " + Aluno.ra)
    print("Nascimento: " + Aluno.data_nascimento)
    print("Natural do estado: " + Aluno.natural_do_estado)
    print("Rg: " + Aluno.rg)
    print("Resultado das cargas horárias: " + Aluno.result_cargas_horarias)
    print("Preenchimento de componentes: " + Aluno.result_preenchimento_componentes)
    print("Aproveitamento de estudos: " + Aluno.aproveitamento_estudos)
    print("Periodo de realização: " + Aluno.periodo_realizacao)
    print("Título do tcc: " + Aluno.titulo_tcc)
    print("Notal final: " + Aluno.nota)
#=======================================Fecha o arquivo PDF
pdf_file.close()