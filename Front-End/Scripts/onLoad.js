import ('./Buttons.js')

document.getElementById('form1').addEventListener('submit', function(event) {
    event.preventDefault();

    const nombres = document.getElementById('name').value;
    const apellidos = document.getElementById('apellidos').value;
    const puesto = document.getElementById('puesto').value;
    const correo = document.getElementById('correo').value;
    const telefono = document.getElementById('telefono').value;
    const direccion = document.getElementById('direccion').value;

    if (nombres && apellidos && puesto && correo && telefono && direccion) {
        fetch('http://localhost:5000/empleado/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nombres, apellidos, puesto, correo, telefono, direccion })
        })
        .then(response => {
            if (response.ok) {
                closeW();
                location.reload();
            } else {
                alert('Error al registrar Empleado');
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('No es una info valida');
    }

});

document.addEventListener('DOMContentLoaded', function() {
    select();
})

function select(){
    fetch(`http://localhost:5000/empleado/select`)
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error fetching data:', data.error);
            return;
        } else {
            let tbody = document.querySelector('#table tbody');
            data.forEach(employee => {
                let row = document.createElement('tr');
                row.classList.add('columna');
                let keys = ['id_empleado', 'nombres', 'apellidos', 'puesto', 'correo', 'telefono', 'direccion'];
                keys.forEach(key => {
                    let item = document.createElement('td');
                    item.textContent = employee[key];
                    item.classList.add('dato');
                    row.appendChild(item);
                });

                let actionsCell = document.createElement('td');
                actionsCell.classList.add('dato');
                
                let updateButton = document.createElement('button');
                updateButton.textContent = 'Actualizar';
                updateButton.setAttribute('id','upd');
                updateButton.classList.add(employee['id_empleado'])
                updateButton.onclick = () => update();
                
                let removeButton = document.createElement('button');
                removeButton.textContent = 'Eliminar';
                removeButton.setAttribute('id','del');
                removeButton.classList.add(employee['id_empleado'])
                removeButton.onclick = () => remove();

                actionsCell.appendChild(updateButton);
                actionsCell.appendChild(removeButton);
                row.appendChild(actionsCell);

                tbody.appendChild(row);
            });
        }
    })
    .catch(error => console.error('Error fetching data:', error));
}
