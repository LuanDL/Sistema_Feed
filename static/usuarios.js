function dados_usuario(tipo){
    
    add_usuario = document.getElementById('adicionar-usuario')
    att_usuario = document.getElementById('att_usuario')

    if(tipo == "1"){
        att_usuario.style.display = "none"
        add_usuario.style.display = "block"

    }else if(tipo == "2"){
        add_usuario.style.display = "none"
        att_usuario.style.display = "block"
    }
}