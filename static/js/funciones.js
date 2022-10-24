// function alerta_error(obj) {
//   var html = '<ul style="text-align: left;">';
//   $.each(obj, function (key, value) {
//     html += "<li>" + key + ":" + value + "</li>";
//   });
//   html += "</ul>";
//   Swal.fire({
//     icon: "error",
//     title: "Error!",
//     html: html,
//   });
// }
function alerta_error(obj) {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}

function alert_jqueryconfirm(url, parameters, callback) {
  $.confirm({
    theme: "material",
    title: "Confirmación",
    icon: "fa fa-info",
    content: "¿Estas seguro de realizar la siguiente acción?",
    columnClass: "small",
    typeAnimated: true,
    cancelButtonClass: "btn-primary",
    draggable: true,
    dragWindowBorder: false,
    buttons: {
      info: {
        text: "Si",
        btnClass: "btn-primary",
        action: function () {
          $.ajax({
            url: url,
            type: "POST",
            data: parameters,
            dataType: "json",
            processData: false,
            contentType: false,
          })
            .done(function (data) {
              console.log(data);
              if (!data.hasOwnProperty("error")) {
                callback();
                //location.href = "{{ listado_url }}";
                return false;
              }
              alerta_error(data.error);
            })
            .fail(function (jqXHR, textStatus, errorThrow) {
              alert(textStatus + " : " + errorThrow);
            })
            .always(function (data) {});
        },
      },
      danger: {
        text: "No",
        btnClass: "btn-red",
        action: function () {},
      },
    },
  });
}
