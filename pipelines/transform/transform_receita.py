def transform_receita(raw):

    registros = raw["data"]["registros"]

    result = []

    for item in registros:
        receita = item["registro"]

        base = {
            "receita_codigo": receita["receita"]["codigo"],
            "tipo_receita": receita["receita"]["tipoReceita"],

            "unidade_codigo": receita["unidadeGestora"]["codigo"],
            "unidade_nome": receita["unidadeGestora"]["denominacao"],

            "exercicio": receita["exercicio"]["exercicio"],


            "categoria_codigo": (
                receita["naturezaReceita"]
                ["categoriaEconomica"]
                ["codigo"]
            ),

            "categoria_nome": (
                receita["naturezaReceita"]
                ["categoriaEconomica"]
                ["denominacao"]
            )
        }


        for movimento in receita["listMovimentos"]:

            row = base.copy()

            row.update(
                {
                    "data_movimento": movimento["dataMovimento"],
                    "tipo_movimento": movimento["tipoMovimento"],
                    "valor_movimento": movimento["valorMovimento"]
                }
            )

            result.append(row)


    return result