// Add PRODUTO record
query produto verb=POST {
  api_group = "ProdutoKimpossible"

  input {
    dblink {
      table = ""
    }
  }

  stack {
    db.add "" {
      enforce_hidden_fields = false
      data = {
        created_at      : "now"
        nome            : $input.nome
        descricao       : $input.descricao
        qtd_disp        : $input.qtd_disp
        url_imagem      : $input.url_imagem
        preco           : $input.preco
        precisa_produzir: $input.precisa_produzir
      }
    } as $model
  }

  response = $model
}