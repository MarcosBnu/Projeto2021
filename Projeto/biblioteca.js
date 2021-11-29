$(function() { // quando o documento estiver pronto/carregado
    
    $.ajax({
        url: 'http://localhost:5000/listar_livros',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (livros) {
        // percorrer a lista de livros retornadas; 
        for (var i in livros) { //i vale a posição no vetor
          //lin='<div class="card cores10card col-3">'+
            lin='<div class="card cores10card col-3">'+
            '<a id="nomelivro" href="#"><img class="card-img-top" src="Imagens/Capas/MulheresRacaEClasse.jpg" alt="Mulheres Raça E Classe" id="capalivro" class="img-fluid">'+
              '<div class="card-body">'+
                '<h4 class="card-title">' + livros[i].Nome_do_livro +'</h4>'+
                '<p class="card-text">'+ livros[i].Autor + '</p>'+
              '</div>'+
            '</a>'+
          '</div>';
            // adiciona a linha no corpo da tabela
            if (livros[i].Status=="Lendo")
              $('#livros_lendo').append(lin);
            if (livros[i].Status=="Quero ler")
              $('#livros_ler').append(lin);
            if (livros[i].Status=="Lido")
              $('#livros_lido').append(lin);
            if (livros[i].Status=="Parei de Ler")
              $('#livros_parei_de_ler').append(lin);
        }
    }

});