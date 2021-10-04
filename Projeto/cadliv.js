$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirLivros", function () {
        //pegar dados da tela
        ISBM = $("#campoISBM").val();
        Capa_do_livro = $("#campoCapa do Livros").val();
        Nome_do_livro = $("#campoNome_do_livro").val();
        Autor = $("#campoAutor").val();
        Paginas = $("#campoPaginas").val();
        Editora = $("#campoEditora").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ ISBM: ISBM, Capa_do_livro: Capa_do_livro, Nome_do_livro: Nome_do_livro, Autor:Autor, Editora:Editora });
        alert(dados)
        alert("aleluia")
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_livro',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: incluir_livro, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function incluir_livro (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Pessoa incluída com sucesso!");
                // limpar os campos
                $("#campoISBM").val();
                $("#campoCapa do Livros").val();
                $("#campoNome_do_livro").val();
                $("#campoAutor").val();
                $("#campoPaginas").val();
                $("#campoEditora").val();
            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
});