var clickDel;
var clickAlt;

document.getElementById('form2').addEventListener('submit', function(event) {
    event.preventDefault();

    const id_empleado = parseInt(clickAlt);
    const nombres = document.getElementById('name2').value;
    const apellidos = document.getElementById('apellidos2').value;
    const puesto = document.getElementById('puesto2').value;
    const correo = document.getElementById('correo2').value;
    const telefono = document.getElementById('telefono2').value;
    const direccion = document.getElementById('direccion2').value;
    

    if (nombres && apellidos && puesto && correo && telefono && direccion) {
        fetch('http://localhost:5000/empleado/update', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id_empleado, nombres, apellidos, puesto, correo, telefono, direccion })
        })
        .then(response => {
            if (response) {
                closeUpdt();
                location.reload();
            } else {
                alert('Error al Actualizar Empleado');
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('No es una info valida');
    }

});

window.onload = function () {
    setTimeout(function () {
        let buttons = document.querySelectorAll('button#del');
        buttons.forEach(button => {
            button.addEventListener('click', function () {
                clickDel = button.className;
            });
        });

        let buttons2 = document.querySelectorAll('button#upd');
        buttons2.forEach(button2 => {
            button2.addEventListener('click', function () {
                clickAlt = button2.className;
            });
        });
    }, 200);
};

function update() {
    setTimeout(function () {
        updt();
    }, 100);
}

function remove() {
    setTimeout(function () {
        fetch(`http://localhost:5000/empleado/delete/${parseInt(clickDel)}`, {
            method: 'DELETE',
        })
            .then(response => {
                if (response.ok) {
                    closeW();
                    location.reload();
                } else {
                    alert('Error al eliminar Empleado');
                }
            })
            .catch(error => console.error('Error:', error));
    }, 100);
}

function updt() {
    var form = document.getElementById('form2');
    var back = document.getElementById('cont');

    form.classList.replace('hide', 'show')
    back.classList.replace('hide', 'show')
}


function closeUpdt() {
    var form = document.getElementById('form2');
    var back = document.getElementById('cont');

    form.classList.replace('show', 'hide')
    back.classList.replace('show', 'hide')
}

function create() {
    var form = document.getElementById('form1');
    var back = document.getElementById('cont');

    form.classList.replace('hide', 'show')
    back.classList.replace('hide', 'show')
}


function closeW() {
    var form = document.getElementById('form1');
    var back = document.getElementById('cont');

    form.classList.replace('show', 'hide')
    back.classList.replace('show', 'hide')
}