$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirLivros", function () {
        //pegar dados da tela
        ISBM = $("#campoISBM").val();
        Capa_do_livro = $("#campoCapa_do_Livro").val();
        Nome_do_livro = $("#campoNome_do_livro").val();
        Autor = $("#campoAutor").val();
        Paginas = $("#campoPaginas").val();
        Editora = $("#campoEditora").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ ISBM: ISBM, Capa_do_livro: Capa_do_livro, Nome_do_livro: Nome_do_livro, Autor:Autor, Editora:Editora });
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
                alert("livro cadastrado com sucesso!");
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

$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btCadastrar", function () {
        //pegar dados da tela
        Nome = $("#campoNome").val();
        Idade= $("#campoIdade").val();
        Email = $("#campoEmail").val();
        Senha = $("#campoSenha").val();
        Repetir_senha = $("#campoRepetir_senha").val();
        // preparar dados no formato json
        var Cadados = JSON.stringify({ Nome: Nome, Idade: Idade, Email: Email, Senha:Senha, Repetir_senha:Repetir_senha });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/cadastrar_usuario',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: Cadados, // estes são os dados enviados
            success: cadastrar_usuario, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function cadastrar_usuario (retorno_cad) {
            if (retorno_cad.resultado_cad == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("livro cadastrado com sucesso!");
                // limpar os campos
                $("#campoNome").val();
                $("#campoIdade").val();
                $("#campoEmail").val();
                $("#campoSenha").val();
                $("#campoRepetir_senha").val();
            } else {
                // informar mensagem de erro
                alert(retorno_cad.resultado_cad + ":" + retorno_cad.detalhes);
            }            
        }
        function erroAoIncluir (retorno_cad) {
            // informar mensagem de erro
            alert("ERRO: "+retorno_cad.resultado_cad + ":" + retorno_cad.detalhes);
        }
    });
});