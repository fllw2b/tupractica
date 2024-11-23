document.addEventListener('DOMContentLoaded', function() {
    // Mostrar mensajes de Django con SweetAlert2
    const messagesScript = document.getElementById('django-messages');
    if (messagesScript) {
        const messages = JSON.parse(messagesScript.textContent);

        messages.forEach(message => {
            const { level, message: text } = message;
            Swal.fire({
                icon: level,
                title: level.charAt(0).toUpperCase() + level.slice(1),
                text: text,
                confirmButtonText: 'Aceptar',
                customClass: {
                    confirmButton: 'btn-pro btn-border',
                },
                buttonsStyling: false
            });
        });
    }

    // Confirmación para eliminar postulaciones
    const eliminarButtons = document.querySelectorAll('.eliminar-postulacion');
    eliminarButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const postId = this.dataset.id;

            Swal.fire({
                title: '¿Estás seguro?',
                text: "No podrás deshacer esta acción.",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Sí, eliminar',
                cancelButtonText: 'Cancelar',
                customClass: {
                    confirmButton: 'btn-pro btn-border',
                    cancelButton: 'btn-pro btn-border'
                },
                buttonsStyling: false
            }).then((result) => {
                if (result.isConfirmed) {

                    const formData = new FormData();
                    formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);

                    fetch(`/anuncios/eliminar-postulacion/${postId}/`, {
                        method: 'POST',
                        body: formData,
                    })
                    .then(response => {
                        if (response.ok) {
                            Swal.fire({
                                icon: 'success',
                                title: 'Eliminado',
                                text: 'La postulación ha sido eliminada exitosamente.',
                                confirmButtonText: 'Aceptar',
                                customClass: {
                                    confirmButton: 'btn-pro btn-border',
                                },
                                buttonsStyling: false
                            }).then(() => {
                                button.closest('.col-md-6').remove();
                                
                                if (document.querySelectorAll('.col-md-6').length === 0) {
                                    const container = document.querySelector('.container');
                                    container.innerHTML += '<p class="text-center text-muted" style="font-size: 1.1em;">No has realizado ninguna postulación aún.</p>';
                                }
                            });
                        } else {
                            Swal.fire({
                                icon: 'error',
                                title: 'Error',
                                text: 'No se pudo eliminar la postulación. Inténtalo de nuevo más tarde.',
                                confirmButtonText: 'Aceptar',
                                customClass: {
                                    confirmButton: 'btn-pro btn-border',
                                },
                                buttonsStyling: false
                            });
                        }
                    })
                    .catch(error => {
                        Swal.fire({
                            icon: 'error',
                            title: 'Error',
                            text: 'Ocurrió un error al procesar la solicitud.',
                            confirmButtonText: 'Aceptar',
                            customClass: {
                                confirmButton: 'btn-pro btn-border',
                            },
                            buttonsStyling: false
                        });
                        console.error('Error al eliminar la postulación:', error);
                    });
                }
            });
        });
    });
});

