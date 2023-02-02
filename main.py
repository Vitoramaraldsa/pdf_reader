import PyPDF2;
import sys
from aluno import Aluno

# ===================================OBTER PARAMETROS DE ENTRADA============================================

# Abre o arquivo PDF
pdf_file = open("C:\\Users\\vitor\\OneDrive\\Área de Trabalho\\TESTE HISTORICOS\\ID-1140084993-2201-GESTÃO ESTRAT MARKETING CASD.pdf", 'rb')
# Cria o objeto PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)
# Obtém o número de páginas
num_pages = len(pdf_reader.pages)

# Percorre as páginas
nome = ""
ra = ""
data_nascimento = ""
nacionalidade = ""
natural_do_estado = ""
rg = ""
perio_de_realizacao = ""

#Realiza a busca de um campo usando os parametros (quantidade de caracteres, nome do campo, pular caracteres e a página)
def BuscarCampoRanged(qtd_carateres,buscar_por,pular_caracteres,pagina):
    resultado = ""
    # -------------------------------------------------------------
    result_busca = pagina.extract_text().find(buscar_por)
    for i in range(qtd_carateres):
        if (i >= pular_caracteres):
            resultado = resultado + pagina.extract_text()[result_busca + i]
    return resultado.strip()

#Realiza a busca de um campo a outro campo
def BuscarCampoAZ(buscar_porA,buscar_porZ,pular_caracteres,pagina):
    resultado = ""
    #-------------------------------------------------------------
    result_busca = pagina.extract_text().find(buscar_porA)
    result_busca2 = pagina.extract_text().find(buscar_porZ)
    result_arquivo_qtd_total = len (pagina.extract_text())

    for i in range(result_arquivo_qtd_total):
        if(i >= result_busca + pular_caracteres and i <= result_busca2 - 1):
          resultado = resultado + pagina.extract_text()[i]

    return resultado.strip()


def VerificarPreenchimentoDeComponentes(pagina):
    resultado = ""
    #-------------------------------------------------------------
    result_busca = pagina.extract_text().find("Docente Qualificação")
    result_busca2 = pagina.extract_text().find("Total da carga horária do curso:")
    result_arquivo_qtd_total = len (pagina.extract_text())

    for i in range(result_arquivo_qtd_total):
        if(i >= result_busca + 20 and i <= result_busca2 - 1):
          resultado = resultado + pagina.extract_text()[i]

    resultado = resultado.strip()



    vpossivelAno = ""
    for i in range(len(resultado)):
        try:
            #capturar caracteres
            valor = int(resultado[i])
            #verificar se é um número
            if(valor >= 0):
                #verificar se é um número
               vpossivelAno = vpossivelAno + resultado[i]
        #ao encontrar uma string entrar na exception
        except:
            #tentar converter o possível ano em ano
            try:
              ano = int(vpossivelAno)
              if(ano >= 1999 and ano <= 2050):
                  print(ano)
            except:
              print("não era um ano")
        vpossivelAno = ""


        #prompt_assingment = prompt_assingment + resultado[i]

    #--------------------- Capturar o ano ---------------
    #prompt_assingment = ""
    #ano = 0
    #for i in range(4):
    #    prompt_assingment = prompt_assingment + resultado[i]

    #--------------------- Verificar se isso é um ano ---------------
    #ano = int(prompt_assingment)
    #if(ano > 1500):








    return resultado


for i in range(num_pages):
    page = pdf_reader.pages[i]
    # ===================================ANALISAR NOME============================================
    nome = BuscarCampoAZ("Nome:", "RA:", 6, page)
    #===================================ANALISAR RA===============================================
    ra = BuscarCampoRanged(15,"RA:",4,page)
    #===================================ANALISAR DATA DE NASCIMENTO===============================
    data_nascimento = BuscarCampoRanged(30, "Data de nascimento:", 20,page)
    #===================================NACIONALIDADE=============================================
    natural_do_estado = BuscarCampoAZ("Natural do Estado:", "Nacionalidade:", 19, page)
    #===================================NACIONALIDADE=============================================
    nacionalidade = BuscarCampoAZ("Nacionalidade:","RG nº",15,page)
    # ===================================BUSCAR RG================================================
    rg = BuscarCampoRanged(21, "RG nº", 6, page)

    VerificarPreenchimentoDeComponentes(page)

    ##print(VerificarPreenchimentoDeComponentes(page))
    #------------------------------------------TESTE----------------------------------------------
    #aluno = Aluno(nome,ra,data_nascimento,natural_do_estado,nacionalidade,rg)
    #------------------------------------------TESTE----------------------------------------------


# Fecha o arquivo PDF
pdf_file.close()