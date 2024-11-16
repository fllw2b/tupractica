document.addEventListener('DOMContentLoaded', function() {
    const anuncios = document.querySelectorAll('.anuncio-item');
    const detalleAnuncioDiv = document.getElementById('detalle-anuncio');

    anuncios.forEach(anuncio => {
        anuncio.addEventListener('click', function(e) {
            e.preventDefault();
            const anuncioId = this.dataset.id;

            // Remover clase activa de todos los elementos
            anuncios.forEach(a => a.classList.remove('active'));

            // Agregar clase activa al elemento seleccionado
            this.classList.add('active');

            // Realizar la petición AJAX
            fetch(`/anuncios/detalle_ajax/${anuncioId}/`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error al obtener los detalles del anuncio.');
                    }
                    return response.text();
                })
                .then(html => {
                    detalleAnuncioDiv.innerHTML = html;
                })
                .catch(error => {
                    detalleAnuncioDiv.innerHTML = `<div class="card-body text-center text-danger"><p>Error al cargar los detalles del anuncio.</p></div>`;
                    console.error('Error al cargar los detalles del anuncio:', error);
                });
        });
    });
});
