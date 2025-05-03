document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("menu-toggle");
    const menu = document.getElementById("menuLateral");

    let isMenuOpen = false;

    toggle.addEventListener("click", () => {
        isMenuOpen = !isMenuOpen;
        menu.classList.toggle("active");
        
        // Cambia el ícono del botón según el estado
        toggle.textContent = isMenuOpen ? "✖" : "☰"; // Cambia entre '☰' y '✖'
    });
});




// Función para obtener la información del producto desde el archivo JSON y redirigir a WhatsApp
function comprar(productoId) {
    // Obtener el archivo JSON de productos localmente
    fetch('productos.json')
        .then(response => response.json())
        .then(data => {
        const producto = data.find(p => p.id == productoId);
        if (producto) {
            const mensaje = `
            ¡Hola! Me interesa el siguiente producto:
            Producto: ${producto.nombre}
            Descripción: ${producto.descripcion}
            Precio: ${producto.precio}
            Imagen: ${producto.imagen}
            `;
            const encodedMessage = encodeURIComponent(mensaje); // Codifica el mensaje para URL
            const whatsappUrl = `https://wa.me/5491151465747?text=${encodedMessage}`; // Cambia el número por el tuyo
            
            // Redirige a WhatsApp
            window.open(whatsappUrl, '_blank');
        } else {
            alert('Producto no encontrado');
        }
        })
        .catch(error => {
        console.error('Error al cargar el archivo JSON:', error);
        alert('Hubo un error al cargar los productos.');
        });
    }

// Función para cargar los productos desde el archivo JSON
function cargarProductos() {
    // Usamos fetch para cargar el archivo JSON
    fetch('productos.json')
        .then(response => response.json()) // Convertir la respuesta a JSON
        .then(productos => {
            const contenedor = document.getElementById('productos-container');  // Contenedor donde se mostrarán los productos
            
            // Detectar la página actual
            const esPaginaZapatillas = window.location.pathname.includes('zapatillas.html');

            // Filtrar los productos si estamos en zapatillas.html
            const productosFiltrados = esPaginaZapatillas
                ? productos.filter(producto => producto.id >= 85 && producto.id <101 )
                : productos;
            
            productosFiltrados.forEach(producto => {
                // Crear el HTML para cada producto
                const productoElemento = document.createElement('article');
                productoElemento.classList.add('producto');

                productoElemento.innerHTML = `
                    <img src="${producto.imagen}" alt="${producto.nombre}">
                    <h2>${producto.nombre}</h2>
                    <p>${producto.descripcion}</p>
                    <span>$${producto.precio.toFixed(2)}</span>
                    <button onclick="comprar(${producto.id})">Comprar</button>
                `;

                // Agregar el producto al contenedor
                contenedor.appendChild(productoElemento);
            });
        })
        .catch(error => {
            console.error('Error al cargar los productos:', error);
        });
}

// Llamar a la función para cargar los productos cuando cargue la página
window.onload = cargarProductos;