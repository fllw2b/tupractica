function validarFormulario() {
    let errores = [];

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const nombres = document.getElementById('nombres').value;
    const apellidos = document.getElementById('apellidos').value;
    const rut = document.getElementById('rut').value;
    const direccion = document.getElementById('direccion').value;
    const telefono = document.getElementById('telefono').value;

    if (!email.includes('@') || !email.includes('.')) {
        errores.push('Por favor, ingresa un correo electrónico válido.');
    }

    if (password.length < 8) {
        errores.push('La contraseña debe tener al menos 8 caracteres.');
    }

    if (nombres.length === 0 || nombres.length > 20) {
        errores.push('Los nombres no pueden estar vacíos y deben tener un máximo de 20 caracteres.');
    }

    if (apellidos.length === 0 || apellidos.length > 20) {
        errores.push('Los apellidos no pueden estar vacíos y deben tener un máximo de 20 caracteres.');
    }

    const rutLimpio = rut.replace(/[^0-9kK]/g, '');
    if (rutLimpio.length < 8 || rutLimpio.length > 9) {
        errores.push('Por favor, ingresa un RUT válido.');
    }

    if (direccion.length === 0 || direccion.length > 50) {
        errores.push('La dirección no puede estar vacía y debe tener un máximo de 50 caracteres.');
    }

    const telefonoRegex = /^[0-9]{9}$/;
    if (!telefonoRegex.test(telefono)) {
        errores.push('Por favor, ingresa un número de teléfono válido (solo 9 dígitos).');
    }

    if (errores.length > 0) {
        Swal.fire({
            title: 'Error en el formulario',
            html: errores.join('<br>'),
            icon: 'error',
            confirmButtonText: 'OK'
        });
        return false; // Evitar envío del formulario
    }

    return true; // Permitir envío del formulario si todo está bien
}

document.getElementById('region-selector').addEventListener('change', function () {
    var regionId = this.value;
    if (regionId) {
        fetch(`/get-comunas/${regionId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error al obtener comunas');
                }
                return response.json();
            })
            .then(data => {
                var comunaSelector = document.getElementById('comuna-selector');
                comunaSelector.innerHTML = '';
                data.forEach(function (comuna) {
                    var option = document.createElement('option');
                    option.value = comuna.id;
                    option.text = comuna.nombre;
                    comunaSelector.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Error al obtener comunas:', error);
            });
    }
});
