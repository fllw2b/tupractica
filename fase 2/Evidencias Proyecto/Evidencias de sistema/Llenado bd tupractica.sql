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
(5, 'Psicología');

INSERT INTO tupractica_sector (nombre)
VALUES 
    ('Tecnología'),
    ('Finanzas'),
    ('Salud'),
    ('Educación'),
    ('Comercio');
