import re;
class Buscas:
    #verifica a falta de componentes
    def VerificarPreenchimentoDeComponentes(pagina):
        resultado = ""
        # -------------------------------------------------------------
        result_busca = pagina.extract_text().find("Docente Qualificação")
        result_busca2 = pagina.extract_text().find("Total da carga horária do curso:")
        result_arquivo_qtd_total = len(pagina.extract_text())

        #pegar somente os componentes academicos
        for i in range(result_arquivo_qtd_total):
            if (i >= result_busca + 20 and i <= result_busca2 - 1):
                resultado = resultado + pagina.extract_text()[i]

        #-----------------------------------regex para capturar campos
        #anos-------------------------------
        patternAnos = r'\b\d{4}'
        pattern = re.compile(patternAnos)
        anos = pattern.findall(resultado)
        #qalificacoes----------------------- -
        patternQualificacoes = r'\b(Mestre|Mestra|Doutora|Doutor|Especialista)\b'
        pattern = re.compile(patternQualificacoes)
        qualificacoes = pattern.findall(resultado)
        #ch---------------------------------
        patternCh = r'\d{2}:\d{2}'
        pattern = re.compile(patternCh)
        ch = pattern.findall(resultado)
        #nota final-------------------------
        patternNotaFinal = r'(10|\d{1},\d{1})'
        pattern = re.compile(patternNotaFinal)
        notal_final = pattern.findall(resultado)
        #resultado formacao----------------
        patternResultadoFormacao = r'Aprovado'
        pattern = re.compile(patternResultadoFormacao)
        resultado_formacao = pattern.findall(resultado)
        #docentes-------------------------
        patternDocentes = r'Aprovado\s+(.*?)\s+(Mestra|Mestre|Doutora|Doutor|Especialista)'
        pattern = re.compile(patternDocentes)
        docentes = pattern.findall(resultado)
        #--------------------------------- Remover todos para encontrar os componentes curriculares
        resultado = re.sub(patternAnos, '', resultado)
        resultado = re.sub(patternCh, '|', resultado)
        resultado = re.sub(patternNotaFinal, '', resultado)
        resultado = re.sub(patternDocentes, '', resultado)
        # --------------------------------- Realizar split para a captura dos componentes curriculares
        resultado = resultado.replace("\n","")
        resultado = resultado.strip()
        resultado = resultado[:-1]
        componentes_curriculares = resultado.split('|')

        #verificar a quantidade dos campos
        if (len(anos) == len(qualificacoes)
            and len(qualificacoes) == len(ch)
            and len(ch) == len(notal_final)
            and len(notal_final) == len(resultado_formacao)
            and len(resultado_formacao) == len(docentes)
            and len(docentes) == len(componentes_curriculares)
            and len(componentes_curriculares) == len(anos)
        ):  #retornar os anos para que seja comparado com o periodo letivos de admissao no robô
            # salvar todos os campos analisados no log
            print("-----------------------------------------------------------------------------")
            print(anos)
            print(qualificacoes)
            print(ch)
            print(notal_final)
            print(resultado_formacao)
            print(docentes)
            print(componentes_curriculares)
            print("-----------------------------------------------------------------------------")
            return str(anos).strip("[]")
        else:
            # salvar todos os campos analisados no log
            print("-----------------------------------------------------------------------------")
            print(anos)
            print(qualificacoes)
            print(ch)
            print(notal_final)
            print(resultado_formacao)
            print(docentes)
            print(componentes_curriculares)
            print("-----------------------------------------------------------------------------")
            return "VERIFIQUE A LISTA DE COMPONENTES CURRICULARES"
    #-----------------------------------------------------------------------------------------------------------------------
    # Realiza a busca de um com uma quantidade limitada de caracteres
    def BuscarCampoRanged(qtd_carateres, buscar_por, pular_caracteres, pagina):
        resultado = ""
        result_busca = pagina.extract_text().find(buscar_por)
        for i in range(qtd_carateres):
            if (i >= pular_caracteres):
                resultado = resultado + pagina.extract_text()[result_busca + i]
        return resultado.strip()
#-----------------------------------------------------------------------------------------------------------------------
    # Realiza a busca de um campo a outro campo
    def BuscarCampoAZ(buscar_porA, buscar_porZ, pular_caracteres, pagina):
        resultado = ""
        result_busca = pagina.extract_text().find(buscar_porA)
        result_busca2 = pagina.extract_text().find(buscar_porZ)
        result_arquivo_qtd_total = len(pagina.extract_text())

        for i in range(result_arquivo_qtd_total):
            if (i >= result_busca + pular_caracteres and i <= result_busca2 - 1):
                resultado = resultado + pagina.extract_text()[i]
        return resultado.strip()
#-----------------------------------------------------------------------------------------------------------------------
    def VerificarCh(pagina):
        text_pagina = pagina.extract_text()
        patternCh = r'\d{3}:\d{2}'
        pattern = re.compile(patternCh)
        cargasHorarias = pattern.findall(text_pagina)
        if(len(cargasHorarias) == 2 and cargasHorarias[0] == cargasHorarias[1]):
            return "CARGAS HORARIAS OK"
        else:
            return "VERIFICAR CARGAS HORARIAS"
#-----------------------------------------------------------------------------------------------------------------------
    def VerificarAproveitamentoEstudos(pagina):
        text_pagina = pagina.extract_text()
        patternAproveitamento = r'Aproveitamento de Estudos'
        pattern = re.compile(patternAproveitamento)
        aproveitamento = pattern.findall(text_pagina)
        return str(aproveitamento)