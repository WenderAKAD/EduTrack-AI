// Update PRODUTO record
query "produto/{produto_id}" verb=PUT {
  api_group = "ProdutoKimpossible"

  input {
    int produto_id? filters=min:1
    dblink {
      table = ""
    }
  }

  stack {
    db.edit "" {
      field_name = "id"
      field_value = $input.produto_id
      enforce_hidden_fields = false
      data = {
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