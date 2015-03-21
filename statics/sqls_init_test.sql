
INSERT INTO `catBrands_catbrand` (`id`, `brand`, `web`) VALUES
(1, 'Nike', 'http://www.nike.com/'),
(2, 'Armani', '');



INSERT INTO `catProductCategories_catproductcategory` (`id`, `category`, `primary`, `parent_id`) VALUES
(1, 'Ropa', 1, NULL),
(2, 'Caballero', 0, 1),
(3, 'Dama', 0, 1),
(4, 'Niño', 0, 1),
(5, 'Niña', 0, 1),
(6, 'Electrónica', 1, NULL),
(7, 'Ferretería', 1, NULL),
(8, 'Herramienta', 0, 7),
(9, 'Pintura', 0, 7),
(10, 'Audio', 0, 6),
(11, 'Videojuegos', 0, 6);



INSERT INTO `catProducts_product` (`id`, `product`, `description`, `price`, `brand_id`, `category_level_1_id`, `category_level_2_id`, `category_level_3_id`, `category_level_4_id`, `category_level_5_id`) VALUES
(1, 'Playera tipo Polo', 'Playera tipo Polo Marca Nike, original, varios colores y varias tallas', 450.000000, 1, 2, NULL, NULL, NULL, NULL);



INSERT INTO `productFeatures_productfeatures` (`id`, `feature`) VALUES
(1, 'Color Rojo'),
(2, 'Cuello "V"'),
(3, 'Logotipo grande de Nike'),
(4, 'Talla Mediana');



INSERT INTO `catProducts_product_features` (`id`, `product_id`, `productfeatures_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4);
