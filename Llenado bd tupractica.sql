-- Inserción de regiones con ID
INSERT INTO tupractica_region (id, nombre) VALUES
(1, 'Región de Arica y Parinacota'),
(2, 'Región de Tarapacá'),
(3, 'Región de Antofagasta'),
(4, 'Región de Atacama'),
(5, 'Región de Coquimbo'),
(6, 'Región de Valparaíso'),
(7, 'Región Metropolitana de Santiago'),
(8, 'Región del Libertador General Bernardo O''Higgins'),
(9, 'Región del Maule'),
(10, 'Región de Ñuble'),
(11, 'Región del Biobío'),
(12, 'Región de La Araucanía'),
(13, 'Región de Los Ríos'),
(14, 'Región de Los Lagos'),
(15, 'Región de Aysén del General Carlos Ibáñez del Campo'),
(16, 'Región de Magallanes y de la Antártica Chilena');

-- Inserción de comunas con ID y referencia a región
INSERT INTO tupractica_comuna (id, nombre, region_id) VALUES
(1, 'Arica', 1), (2, 'Putre', 1), (3, 'Camarones', 1),
(4, 'Iquique', 2), (5, 'Alto Hospicio', 2), (6, 'Pozo Almonte', 2),
(7, 'Antofagasta', 3), (8, 'Mejillones', 3), (9, 'Taltal', 3),
(10, 'Copiapó', 4), (11, 'Caldera', 4), (12, 'Vallenar', 4),
(13, 'La Serena', 5), (14, 'Coquimbo', 5), (15, 'Ovalle', 5),
(16, 'Valparaíso', 6), (17, 'Viña del Mar', 6), (18, 'Quilpué', 6),
(19, 'Santiago', 7), (20, 'Providencia', 7), (21, 'Las Condes', 7),
(22, 'Rancagua', 8), (23, 'San Fernando', 8), (24, 'Pichilemu', 8),
(25, 'Talca', 9), (26, 'Curicó', 9), (27, 'Constitución', 9),
(28, 'Chillán', 10), (29, 'San Carlos', 10), (30, 'Quirihue', 10),
(31, 'Concepción', 11), (32, 'Los Ángeles', 11), (33, 'Talcahuano', 11),
(34, 'Temuco', 12), (35, 'Villarrica', 12), (36, 'Pucón', 12),
(37, 'Valdivia', 13), (38, 'La Unión', 13), (39, 'Panguipulli', 13),
(40, 'Puerto Montt', 14), (41, 'Castro', 14), (42, 'Ancud', 14),
(43, 'Coyhaique', 15), (44, 'Puerto Aysén', 15), (45, 'Chile Chico', 15),
(46, 'Punta Arenas', 16), (47, 'Puerto Natales', 16), (48, 'Porvenir', 16);

-- Inserción de carreras con ID
INSERT INTO tupractica_carrera (id, nombre) VALUES
(1, 'Ingeniería Informática'),
(2, 'Ingeniería Civil'),
(3, 'Medicina'),
(4, 'Derecho'),
(5, 'Psicología'),
(6, 'Ingeniería Comercial'),
(7, 'Diseño Gráfico'),
(8, 'Administración de Empresas'),
(9, 'Arquitectura'),
(10, 'Nutrición y Dietética');

-- Inserción de sectores empresa
INSERT INTO tupractica_sector (nombre)
VALUES 
    ('Tecnología'),
    ('Finanzas'),
    ('Salud'),
    ('Educación'),
    ('Comercio'),
    ('Construcción'),
    ('Turismo'),
    ('Marketing'),
    ('Manufactura'),
    ('Transporte');

-- Inserción de tags
INSERT INTO usuarios_tag (nombre) VALUES
    ('Python'),
    ('JavaScript'),
    ('C++'),
    ('Desarrollo Web'),
    ('SQL'),
    ('Machine Learning'),
    ('Data Analysis'),
    ('Gestión de Proyectos'),
    ('Marketing Digital'),
    ('Diseño Gráfico'),
    ('Cocina'),
    ('ReactJS'),
    ('Angular'),
    ('Node.js'),
    ('Scrum'),
    ('Git'),
    ('Django'),
    ('Flask'),
    ('Redacción Técnica'),
    ('Excel'),
    ('Power BI'),
    ('AutoCAD'),
    ('Photoshop'),
    ('Figma'),
    ('Illustrator'),
    ('Ventas'),
    ('Comunicación'),
    ('Resolución de Problemas'),
    ('Trabajo en Equipo'),
    ('Creatividad'),
    ('Atención al Cliente'),
    ('Planificación Estratégica'),
    ('R'),
    ('SPSS'),
    ('SAP'),
    ('PHP'),
    ('Laravel'),
    ('Microservicios'),
    ('Docker'),
    ('Kubernetes'),
    ('DevOps'),
    ('Seguridad Informática'),
    ('Redes'),
    ('Cloud Computing'),
    ('AWS'),
    ('Azure'),
    ('GCP'),
    ('Big Data'),
    ('NoSQL'),
    ('MongoDB'),
    ('MySQL'),
    ('PostgreSQL'),
    ('Hibernate'),
    ('Spring Boot'),
    ('JUnit'),
    ('Calidad de Software'),
    ('HTML'),
    ('CSS'),
    ('SASS'),
    ('TypeScript'),
    ('Redux'),
    ('Next.js'),
    ('GraphQL'),
    ('Rest APIs'),
    ('TDD'),
    ('Bash Scripting'),
    ('Unity'),
    ('Unreal Engine'),
    ('Videojuegos'),
    ('IA Conversacional'),
    ('Optimización de Procesos'),
    ('Logística'),
    ('Auditoría'),
    ('Coaching'),
    ('Mentoring');

-- Inserción de usuarios (empresas y estudiantes) se hace en la shell de django con comando python manage.py shell
   /*
    * 
    from apps.usuarios.models import Usuario

usuarios = [
    {"email": "empresa1@ejemplo.com", "password": "123123123", "es_estudiante": False},
    {"email": "empresa2@ejemplo.com", "password": "123123123", "es_estudiante": False},
    {"email": "empresa3@ejemplo.com", "password": "123123123", "es_estudiante": False},
    {"email": "estudiante1@ejemplo.com", "password": "123123123", "es_estudiante": True},
    {"email": "estudiante2@ejemplo.com", "password": "123123123", "es_estudiante": True},
    {"email": "estudiante3@ejemplo.com", "password": "123123123", "es_estudiante": True},
]

for user_data in usuarios:
    usuario = Usuario.objects.create_user(
        email=user_data["email"],
        password=user_data["password"],
        es_estudiante=user_data["es_estudiante"],
    )
    print(f"Usuario creado: {usuario.email}")
 
    */

-- Inserción de empresas de ejemplo
INSERT INTO usuarios_empresa (id, usuario_id, nombre_empresa, rut, direccion, sector_id, pagina_web, descripcion) VALUES
(1, 1, 'TechCorp', '12.345.678-9', 'Av. Siempre Viva 123, Santiago', 1, 'https://www.techcorp.com', 'Empresa dedicada al desarrollo de soluciones tecnológicas.'),
(2, 2, 'EduPlus', '98.765.432-1', 'Calle Falsa 456, Valparaíso', 4, 'https://www.eduplus.com', 'Institución enfocada en la educación y capacitación.'),
(3, 3, 'HealthServices', '11.223.344-5', 'Pasaje Salud 789, Antofagasta', 3, 'https://www.healthservices.com', 'Servicios médicos y de atención en salud para la comunidad.');

-- Inserción de estudiantes de ejemplo
INSERT INTO usuarios_estudiante (id, usuario_id, nombres, apellidos, rut, region_id, comuna_id, carrera_id, fecha_nacimiento, genero, direccion, telefono)
VALUES
(1, 4, 'Juan', 'Pérez', '12.345.678-9', 7, 19, 1, '2000-01-01', 'M', 'Calle Falsa 123', '+56912345678'),
(2, 5, 'María', 'González', '98.765.432-1', 6, 16, 5, '2001-03-15', 'F', 'Av. Principal 456', '+56987654321'),
(3, 6, 'Pedro', 'Ramírez', '11.223.344-5', 3, 7, 3, '1999-07-21', 'M', 'Pasaje Lateral 789', '+56911223344');

-- Inserción de anuncios de práctica
INSERT INTO anuncios_anunciopractica (id, empresa_id, titulo, region_id, comuna_id, ubicacion, modalidad, descripcion, fecha_publicacion) VALUES
(1, 1, 'Práctica Desarrollo Web', 7, 19, 'Av. Providencia 100', 'remoto', 'Práctica para el desarrollo de aplicaciones web usando tecnologías modernas como React y Django.', NOW()),
(2, 1, 'Práctica Data Science', 7, 21, 'Av. Las Condes 123', 'hibrido', 'Práctica para análisis de datos y machine learning en proyectos innovadores.', NOW()),
(3, 2, 'Práctica Diseño Gráfico', 6, 17, 'Calle Arlegui 456', 'presencial', 'Práctica para estudiantes de diseño gráfico con enfoque en material educativo.', NOW()),
(4, 2, 'Práctica Marketing Digital', 6, 16, 'Calle Bellavista 789', 'remoto', 'Práctica para campañas de marketing digital orientadas a la educación.', NOW()),
(5, 3, 'Práctica Atención al Cliente', 3, 7, 'Calle Salud 101', 'presencial', 'Práctica para estudiantes interesados en aprender sobre la atención de pacientes en el sector salud.', NOW()),
(6, 3, 'Práctica Nutrición y Dietética', 3, 8, 'Calle Mejillones 303', 'hibrido', 'Práctica para apoyar programas de nutrición en centros de salud comunitarios.', NOW());

-- Asignación de tags a anuncios
INSERT INTO anuncios_anunciopractica_requisitos (anunciopractica_id, tag_id) VALUES
(1, 1), (1, 4), (1, 17), (1, 27), (1, 14),
(2, 6), (2, 7), (2, 41), (2, 42), (2, 43),
(3, 10), (3, 24), (3, 25), (3, 9),
(4, 8), (4, 21), (4, 11), (4, 28),
(5, 27), (5, 41), (5, 26),
(6, 9), (6, 3), (6, 5), (6, 43);
