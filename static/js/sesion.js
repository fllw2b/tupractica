function confirmarCerrarSesion() {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "Estás a punto de cerrar sesión.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, cerrar sesión'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = "{% url 'logout' %}";
        }
    });
}