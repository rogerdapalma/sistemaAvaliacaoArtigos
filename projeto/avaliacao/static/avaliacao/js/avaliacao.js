function soma_notas_orientador() {
    //orientador
    $('#id_nota_final_orientador').val( (Number($('#id_nota_merito_acompanhamento_orientador').val()) +
                                        Number($('#id_nota_merito_desenvolvimento_orientador').val()) +
                                        Number($('#id_nota_merito_redacao_orientador').val()) +
                                        Number($('#id_nota_merito_apresentacao_orientador').val())).toFixed(1) );
    $('#id_nota_final_orientador_coordenador').val( $('#id_nota_final_orientador').val() );

    try {
        media_final();
    } catch(err) {
       
    }
}

function soma_notas_responsavel() {
    //responsavel
    $('#id_nota_final_responsavel').val( (Number($('#id_nota_merito_desenvolvimento_responsavel').val()) +
                                        Number($('#id_nota_merito_redacao_responsavel').val()) +
                                        Number($('#id_nota_merito_apresentacao_responsavel').val())).toFixed(1) );
    $('#id_nota_final_responsavel_coordenador').val( $('#id_nota_final_responsavel').val() );
    try {
        media_final();
    } catch(err) {
       
    }
}

function soma_notas_suplente() {
    //suplente
    $('#id_nota_final_suplente').val( (Number($('#id_nota_merito_desenvolvimento_suplente').val()) +
                                        Number($('#id_nota_merito_redacao_suplente').val()) +
                                        Number($('#id_nota_merito_apresentacao_suplente').val())).toFixed(1) );
    $('#id_nota_final_suplente_coordenador').val( $('#id_nota_final_suplente').val() );    
    try {
        media_final();
    } catch(err) {
       
    }                             
}

function soma_notas_convidado() {
    try {
        //convidado
        $('#id_nota_final_convidado').val( (Number($('#id_nota_merito_desenvolvimento_convidado').val()) +
                                            Number($('#id_nota_merito_redacao_convidado').val()) +
                                            Number($('#id_nota_merito_apresentacao_convidado').val())).toFixed(1) );
        $('#id_nota_final_convidado_coordenador').val( $('#id_nota_final_convidado').val() );    
        
        media_final_com_convidado();
    } catch(err) {
       
    }                             
}

function media_final() {
    //media final
    $('#id_media_final').val((( Number($('#id_nota_final_orientador_coordenador').val()) + 
                               Number($('#id_nota_final_responsavel_coordenador').val()) +
                               Number($('#id_nota_final_suplente_coordenador').val()) ) / 3).toFixed(1));

    //orientador
    try {
        let form = document.forms.avaliacao_visao_administrador;
        let nota_final_orientador = form.elements.nota_final_orientador;
        nota_final_orientador.value = $('#id_nota_final_orientador_coordenador').val();
    } catch(err) {

    }

    try {
        let form1 = document.forms.form_avaliacao_orientador;
        let nota_orientador = form1.elements.nota_final_orientador;
        nota_orientador.value = $('#id_nota_final_orientador').val();
    } catch(err) {

    }

    //responsavel
    try {
        let form = document.forms.avaliacao_visao_administrador;
        let nota_final_responsavel = form.elements.nota_final_responsavel;
        nota_final_responsavel.value = $('#id_nota_final_responsavel_coordenador').val();
    } catch(err) {
        
    }

    try {
        let form1 = document.forms.form_avaliacao_responsavel;
        let nota_responsavel = form1.elements.nota_final_responsavel;
        nota_responsavel.value = $('#id_nota_final_responsavel').val();
    } catch(err) {
        
    }
    
    //suplente
    try {
        let form = document.forms.avaliacao_visao_administrador;
        let nota_final_suplente = form.elements.nota_final_suplente;
        nota_final_suplente.value = $('#id_nota_final_suplente_coordenador').val();
    } catch(err) {
        
    }

    try {
        let form1 = document.forms.form_avaliacao_suplente;
        let nota_suplente = form1.elements.nota_final_suplente;
        nota_suplente.value = $('#id_nota_final_suplente').val();
    } catch(err) {
        
    }

    //media final
    try { 
        let form = document.forms.avaliacao_visao_administrador;
        let media_final_tfg = form.elements.media_final_avaliacao;
        media_final_tfg.value = $('#id_media_final').val();
    } catch(err) {

    }   
}

function media_final_com_convidado() {
    //media final
    $('#id_media_final').val((( Number($('#id_nota_final_orientador_coordenador').val()) + 
                               Number($('#id_nota_final_responsavel_coordenador').val()) +
                               Number($('#id_nota_final_suplente_coordenador').val()) +
                               Number($('#id_nota_final_convidado_coordenador').val())) / 4).toFixed(1));

    //orientador
    try {
        let form = document.forms.avaliacao_visao_administrador;
        let nota_final_orientador = form.elements.nota_final_orientador;
        nota_final_orientador.value = $('#id_nota_final_orientador_coordenador').val();
    } catch(err) {

    }

    try {
        let form1 = document.forms.form_avaliacao_orientador;
        let nota_orientador = form1.elements.nota_final_orientador;
        nota_orientador.value = $('#id_nota_final_orientador').val();
    } catch(err) {

    }

    //responsavel
    try {
        let form = document.forms.avaliacao_visao_administrador;
        let nota_final_responsavel = form.elements.nota_final_responsavel;
        nota_final_responsavel.value = $('#id_nota_final_responsavel_coordenador').val();
    } catch(err) {
        
    }

    try {
        let form1 = document.forms.form_avaliacao_responsavel;
        let nota_responsavel = form1.elements.nota_final_responsavel;
        nota_responsavel.value = $('#id_nota_final_responsavel').val();
    } catch(err) {
        
    }
    
    //suplente
    try {
        let form = document.forms.avaliacao_visao_administrador;
        let nota_final_suplente = form.elements.nota_final_suplente;
        nota_final_suplente.value = $('#id_nota_final_suplente_coordenador').val();
    } catch(err) {
        
    }

    try {
        let form1 = document.forms.form_avaliacao_suplente;
        let nota_suplente = form1.elements.nota_final_suplente;
        nota_suplente.value = $('#id_nota_final_suplente').val();
    } catch(err) {
        
    }

    //convidado
    try {
        let form = document.forms.avaliacao_visao_administrador;
        let nota_final_convidado = form.elements.nota_final_convidado;
        nota_final_convidado.value = $('#id_nota_final_convidado_coordenador').val();
    } catch(err) {
        
    }

    try {
        let form1 = document.forms.form_avaliacao_convidado;
        let nota_convidado = form1.elements.nota_final_convidado;
        nota_convidado.value = $('#id_nota_final_convidado').val();
    } catch(err) {
        
    }

    //media final
    try { 
        let form = document.forms.avaliacao_visao_administrador;
        let media_final_tfg = form.elements.media_final_avaliacao;
        media_final_tfg.value = $('#id_media_final').val();
    } catch(err) {

    }   
}

function atualiza() {
    //orientador
    let peso_merito_acompanhamento_orientador = $("#id_peso_merito_acompanhamento_orientador").val();
    let merito_acompanhamento_orientador = $("#id_merito_acompanhamento_orientador").val();
    $('#id_nota_merito_acompanhamento_orientador').val(peso_merito_acompanhamento_orientador * merito_acompanhamento_orientador / 10);

    let peso_merito_desenvolvimento_orientador = $("#id_peso_merito_desenvolvimento_orientador").val();
    let merito_desenvolvimento_orientador = $("#id_merito_desenvolvimento_orientador").val();
    $('#id_nota_merito_desenvolvimento_orientador').val(peso_merito_desenvolvimento_orientador * merito_desenvolvimento_orientador / 10);

    let peso_merito_redacao_orientador = $("#id_peso_merito_redacao_orientador").val();
    let merito_redacao_orientador = $("#id_merito_redacao_orientador").val();
    $('#id_nota_merito_redacao_orientador').val(peso_merito_redacao_orientador * merito_redacao_orientador / 10);
  
    let peso_merito_apresentacao_orientador = $("#id_peso_merito_apresentacao_orientador").val();
    let merito_apresentacao_orientador = $("#id_merito_apresentacao_orientador").val();
    $('#id_nota_merito_apresentacao_orientador').val(peso_merito_apresentacao_orientador * merito_apresentacao_orientador / 10);
    
    try {
        soma_notas_orientador();
    } catch(err) {
        
    }

    //avaliador responsável
    let peso_merito_desenvolvimento_responsavel = $("#id_peso_merito_desenvolvimento_responsavel").val();
    let merito_desenvolvimento_responsavel = $("#id_merito_desenvolvimento_responsavel").val();
    $('#id_nota_merito_desenvolvimento_responsavel').val(peso_merito_desenvolvimento_responsavel * merito_desenvolvimento_responsavel / 10);
    
    let peso_merito_redacao_responsavel = $("#id_peso_merito_redacao_responsavel").val();
    let merito_redacao_responsavel = $("#id_merito_redacao_responsavel").val();
    $('#id_nota_merito_redacao_responsavel').val(peso_merito_redacao_responsavel * merito_redacao_responsavel / 10);
    
    let peso_merito_apresentacao_responsavel = $("#id_peso_merito_apresentacao_responsavel").val();
    let merito_apresentacao_responsavel = $("#id_merito_apresentacao_responsavel").val();
    $('#id_nota_merito_apresentacao_responsavel').val(peso_merito_apresentacao_responsavel * merito_apresentacao_responsavel / 10);

    try {
        soma_notas_responsavel();
    } catch(err) {
       
    }
    
    //avaliador suplente
    let peso_merito_desenvolvimento_suplente = $("#id_peso_merito_desenvolvimento_suplente").val();
    let merito_desenvolvimento_suplente = $("#id_merito_desenvolvimento_suplente").val();
    $('#id_nota_merito_desenvolvimento_suplente').val(peso_merito_desenvolvimento_suplente * merito_desenvolvimento_suplente / 10);

    let peso_merito_redacao_suplente = $("#id_peso_merito_redacao_suplente").val();
    let merito_redacao_suplente = $("#id_merito_redacao_suplente").val();
    $('#id_nota_merito_redacao_suplente').val(peso_merito_redacao_suplente * merito_redacao_suplente / 10);

    let peso_merito_apresentacao_suplente = $("#id_peso_merito_apresentacao_suplente").val();
    let merito_apresentacao_suplente = $("#id_merito_apresentacao_suplente").val();
    $('#id_nota_merito_apresentacao_suplente').val(peso_merito_apresentacao_suplente * merito_apresentacao_suplente / 10);

    try {
        soma_notas_suplente();
    } catch(err) {
        
    }

    try {
        //avaliador convidado
        let peso_merito_desenvolvimento_convidado = $("#id_peso_merito_desenvolvimento_convidado").val();
        let merito_desenvolvimento_convidado = $("#id_merito_desenvolvimento_convidado").val();
        $('#id_nota_merito_desenvolvimento_convidado').val(peso_merito_desenvolvimento_convidado * merito_desenvolvimento_convidado / 10);

        let peso_merito_redacao_convidado = $("#id_peso_merito_redacao_convidado").val();
        let merito_redacao_convidado = $("#id_merito_redacao_convidado").val();
        $('#id_nota_merito_redacao_convidado').val(peso_merito_redacao_convidado * merito_redacao_convidado / 10);

        let peso_merito_apresentacao_convidado = $("#id_peso_merito_apresentacao_convidado").val();
        let merito_apresentacao_convidado = $("#id_merito_apresentacao_convidado").val();
        $('#id_nota_merito_apresentacao_convidado').val(peso_merito_apresentacao_convidado * merito_apresentacao_convidado / 10);

        soma_notas_convidado();
    } catch(err) {
        
    }
  }
  
  window.onload = (function () { atualiza() });


$(document).ready(function () {
    //orientador
    $('#id_merito_acompanhamento_orientador').on('change', function(){
        let peso_merito_acompanhamento_orientador = $("#id_peso_merito_acompanhamento_orientador").val();
        let merito_acompanhamento_orientador = $("#id_merito_acompanhamento_orientador").val();
        $('#id_nota_merito_acompanhamento_orientador').val(peso_merito_acompanhamento_orientador * merito_acompanhamento_orientador / 10);
        try {
            soma_notas_orientador();
        } catch(err) {
           
        }
    });
    $('#id_merito_desenvolvimento_orientador').on('change', function(){
        let peso_merito_desenvolvimento_orientador = $("#id_peso_merito_desenvolvimento_orientador").val();
        let merito_desenvolvimento_orientador = $("#id_merito_desenvolvimento_orientador").val();
        $('#id_nota_merito_desenvolvimento_orientador').val(peso_merito_desenvolvimento_orientador * merito_desenvolvimento_orientador / 10);
        try {
            soma_notas_orientador();
        } catch(err) {
            
        }
    });
    $('#id_merito_redacao_orientador').on('change', function(){
        let peso_merito_redacao_orientador = $("#id_peso_merito_redacao_orientador").val();
        let merito_redacao_orientador = $("#id_merito_redacao_orientador").val();
        $('#id_nota_merito_redacao_orientador').val(peso_merito_redacao_orientador * merito_redacao_orientador / 10);
        try {
            soma_notas_orientador();
        } catch(err) {
            
        }
    });
    $('#id_merito_apresentacao_orientador').on('change', function(){
        let peso_merito_apresentacao_orientador = $("#id_peso_merito_apresentacao_orientador").val();
        let merito_apresentacao_orientador = $("#id_merito_apresentacao_orientador").val();
        $('#id_nota_merito_apresentacao_orientador').val(peso_merito_apresentacao_orientador * merito_apresentacao_orientador / 10);
        try {
            soma_notas_orientador();
        } catch(err) {
            
        }
    });

    //avaliador responsável
    $('#id_merito_desenvolvimento_responsavel').on('change', function(){
        let peso_merito_desenvolvimento_responsavel = $("#id_peso_merito_desenvolvimento_responsavel").val();
        let merito_desenvolvimento_responsavel = $("#id_merito_desenvolvimento_responsavel").val();
        $('#id_nota_merito_desenvolvimento_responsavel').val(peso_merito_desenvolvimento_responsavel * merito_desenvolvimento_responsavel / 10);
        try {
            soma_notas_responsavel();
        } catch(err) {
           
        }
    });
    $('#id_merito_redacao_responsavel').on('change', function(){
        let peso_merito_redacao_responsavel = $("#id_peso_merito_redacao_responsavel").val();
        let merito_redacao_responsavel = $("#id_merito_redacao_responsavel").val();
        $('#id_nota_merito_redacao_responsavel').val(peso_merito_redacao_responsavel * merito_redacao_responsavel / 10);
        try {
            soma_notas_responsavel();
        } catch(err) {
            
        }
    });
    $('#id_merito_apresentacao_responsavel').on('change', function(){
        let peso_merito_apresentacao_responsavel = $("#id_peso_merito_apresentacao_responsavel").val();
        let merito_apresentacao_responsavel = $("#id_merito_apresentacao_responsavel").val();
        $('#id_nota_merito_apresentacao_responsavel').val(peso_merito_apresentacao_responsavel * merito_apresentacao_responsavel / 10);
        try {
            soma_notas_responsavel();
        } catch(err) {
           
        }
    });

    //avaliador suplente
    $('#id_merito_desenvolvimento_suplente').on('change', function(){
        let peso_merito_desenvolvimento_suplente = $("#id_peso_merito_desenvolvimento_suplente").val();
        let merito_desenvolvimento_suplente = $("#id_merito_desenvolvimento_suplente").val();
        $('#id_nota_merito_desenvolvimento_suplente').val(peso_merito_desenvolvimento_suplente * merito_desenvolvimento_suplente / 10);
        try {
            soma_notas_suplente();
        } catch(err) {
            
        }
    });
    $('#id_merito_redacao_suplente').on('change', function(){
        let peso_merito_redacao_suplente = $("#id_peso_merito_redacao_suplente").val();
        let merito_redacao_suplente = $("#id_merito_redacao_suplente").val();
        $('#id_nota_merito_redacao_suplente').val(peso_merito_redacao_suplente * merito_redacao_suplente / 10);
        try {
            soma_notas_suplente();
        } catch(err) {
            
        }
    });
    $('#id_merito_apresentacao_suplente').on('change', function(){
        let peso_merito_apresentacao_suplente = $("#id_peso_merito_apresentacao_suplente").val();
        let merito_apresentacao_suplente = $("#id_merito_apresentacao_suplente").val();
        $('#id_nota_merito_apresentacao_suplente').val(peso_merito_apresentacao_suplente * merito_apresentacao_suplente / 10);
        try {
            soma_notas_suplente();
        } catch(err) {
            
        }
    });

    //avaliador convidado
    $('#id_merito_desenvolvimento_convidado').on('change', function(){
        let peso_merito_desenvolvimento_convidado = $("#id_peso_merito_desenvolvimento_convidado").val();
        let merito_desenvolvimento_convidado = $("#id_merito_desenvolvimento_convidado").val();
        $('#id_nota_merito_desenvolvimento_convidado').val(peso_merito_desenvolvimento_convidado * merito_desenvolvimento_convidado / 10);
        try {
            soma_notas_convidado();
        } catch(err) {
            
        }
    });
    $('#id_merito_redacao_convidado').on('change', function(){
        let peso_merito_redacao_convidado = $("#id_peso_merito_redacao_convidado").val();
        let merito_redacao_convidado = $("#id_merito_redacao_convidado").val();
        $('#id_nota_merito_redacao_convidado').val(peso_merito_redacao_convidado * merito_redacao_convidado / 10);
        try {
            soma_notas_convidado();
        } catch(err) {
            
        }
    });
    $('#id_merito_apresentacao_convidado').on('change', function(){
        let peso_merito_apresentacao_convidado = $("#id_peso_merito_apresentacao_convidado").val();
        let merito_apresentacao_convidado = $("#id_merito_apresentacao_convidado").val();
        $('#id_nota_merito_apresentacao_convidado').val(peso_merito_apresentacao_convidado * merito_apresentacao_convidado / 10);
        try {
            soma_notas_convidado();
        } catch(err) {
            
        }
    });
});