-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 22-09-2026 a las 00:35:37
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_facturacion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `category`
--

CREATE TABLE `category` (
  `Id_Category` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `category`
--

INSERT INTO `category` (`Id_Category`, `name`) VALUES
(1, 'PESCADOS'),
(2, 'CARNES'),
(3, 'PASTAS'),
(4, 'AVES'),
(5, 'ARROZ'),
(6, 'BEBIDAS '),
(7, 'BEBIDAS PREPARADAS');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `company`
--

CREATE TABLE `company` (
  `id_company` int(11) NOT NULL,
  `Nit` varchar(45) NOT NULL,
  `company_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `company`
--

INSERT INTO `company` (`id_company`, `Nit`, `company_name`) VALUES
(1, '60301419', 'RESTAURANTE BRASAS DE ORO'),
(2, '103040123', 'DONATELLO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invoice`
--

CREATE TABLE `invoice` (
  `id_invoice` bigint(20) NOT NULL,
  `Id_person` int(11) NOT NULL,
  `Id_company` int(11) DEFAULT NULL,
  `Id_payment_method` tinyint(4) NOT NULL,
  `Date` date NOT NULL,
  `Hour` time NOT NULL,
  `Sub_total` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `invoice`
--

INSERT INTO `invoice` (`id_invoice`, `Id_person`, `Id_company`, `Id_payment_method`, `Date`, `Hour`, `Sub_total`, `total`) VALUES
(1, 1, NULL, 1, '2026-09-19', '03:03:00', 55000.00, 55000.00),
(6, 2, 2, 3, '2026-09-19', '16:27:38', 331000.00, 331000.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invoice_products`
--

CREATE TABLE `invoice_products` (
  `id_invoice` bigint(20) NOT NULL,
  `Id_product` int(11) NOT NULL,
  `Unit value` decimal(10,2) NOT NULL,
  `Amount` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `invoice_products`
--

INSERT INTO `invoice_products` (`id_invoice`, `Id_product`, `Unit value`, `Amount`) VALUES
(6, 1, 55000.00, 1),
(6, 2, 51000.00, 3),
(6, 3, 41000.00, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `payment_method`
--

CREATE TABLE `payment_method` (
  `id_Payment_method` tinyint(4) NOT NULL,
  `name` varchar(45) NOT NULL,
  `Description` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `payment_method`
--

INSERT INTO `payment_method` (`id_Payment_method`, `name`, `Description`) VALUES
(1, 'EFECTIVO', NULL),
(2, 'TARJETA DEBITO', NULL),
(3, 'TARJETA CREDITO', NULL),
(4, 'TRANSFERENCIA', NULL),
(5, 'OTROS MEDIOS DE PAGO', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `person`
--

CREATE TABLE `person` (
  `id_Person` int(11) NOT NULL,
  `company` varchar(45) DEFAULT NULL,
  `Identification` varchar(45) NOT NULL,
  `Name` varchar(450) NOT NULL,
  `address` varchar(250) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `potal_code` varchar(15) DEFAULT NULL,
  `phones_number` varchar(10) NOT NULL,
  `Email` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `person`
--

INSERT INTO `person` (`id_Person`, `company`, `Identification`, `Name`, `address`, `city`, `potal_code`, `phones_number`, `Email`) VALUES
(1, 'Brasas de oro', '1049654678', 'Javier Rodriguez', 'cra 9 · 150-1', 'Tunja', '150001', '3132719105', 'Javier@gmail.com'),
(2, 'DONATELLO', '1049123456', 'Alejandro Perez', 'avenida  norte # 89-32', 'Tunja', '15000', '3101234567', 'alejandro@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `Id_product` int(11) NOT NULL,
  `Id_Categoria` int(11) NOT NULL,
  `Product_code` varchar(50) NOT NULL,
  `name` varchar(45) NOT NULL DEFAULT '0',
  `Description` varchar(250) NOT NULL,
  `Purchase_price` decimal(10,2) NOT NULL,
  `Selling_price` decimal(10,2) NOT NULL,
  `Stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`Id_product`, `Id_Categoria`, `Product_code`, `name`, `Description`, `Purchase_price`, `Selling_price`, `Stock`) VALUES
(1, 2, '1000', 'CHURRASCO', 'Corte de rez a la parrilla', 45000.00, 55000.00, 20),
(2, 2, '1001', 'LOMO DE CERDO', 'Carne de cerdo a la parrilla ', 38000.00, 51000.00, 58),
(3, 1, '1002', 'TRUCHA PLANCHA', 'Deliciosa trucha arcoíris apanada a la plancha', 30000.00, 41000.00, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `supplier`
--

CREATE TABLE `supplier` (
  `id_supplier` int(11) NOT NULL,
  `Company_identification` varchar(45) NOT NULL,
  `Company_name` varchar(45) NOT NULL,
  `Directions` varchar(45) NOT NULL,
  `City` varchar(45) DEFAULT NULL,
  `Cell_phones` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `supplier`
--

INSERT INTO `supplier` (`id_supplier`, `Company_identification`, `Company_name`, `Directions`, `City`, `Cell_phones`, `Email`) VALUES
(1, '1049654678', 'CARNES CENTRAL', 'Cra 4 # 11-32', 'Tunja', '3124561728]', 'carnes.centra@gmail.com'),
(2, '603045641', 'PESQUERA', 'avenida colon # 10-40', 'Sogamoso', '7400040', 'PESQUERA@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `supplier_has_products`
--

CREATE TABLE `supplier_has_products` (
  `Supplier_id_supplier` int(11) NOT NULL,
  `Products_Id_producto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `supplier_has_products`
--

INSERT INTO `supplier_has_products` (`Supplier_id_supplier`, `Products_Id_producto`) VALUES
(1, 1),
(1, 2),
(2, 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`Id_Category`);

--
-- Indices de la tabla `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id_company`),
  ADD UNIQUE KEY `Nit_UNIQUE` (`Nit`),
  ADD UNIQUE KEY `company_name_UNIQUE` (`company_name`),
  ADD UNIQUE KEY `id_company_UNIQUE` (`id_company`);

--
-- Indices de la tabla `invoice`
--
ALTER TABLE `invoice`
  ADD PRIMARY KEY (`id_invoice`),
  ADD KEY `fk_Factura_Persona_idx` (`Id_person`),
  ADD KEY `fk_Factura_compañia1_idx` (`Id_company`),
  ADD KEY `fk_Factura_Termino1_idx` (`Id_payment_method`);

--
-- Indices de la tabla `invoice_products`
--
ALTER TABLE `invoice_products`
  ADD PRIMARY KEY (`id_invoice`,`Id_product`),
  ADD KEY `id_product_idx` (`Id_product`);

--
-- Indices de la tabla `payment_method`
--
ALTER TABLE `payment_method`
  ADD PRIMARY KEY (`id_Payment_method`);

--
-- Indices de la tabla `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id_Person`),
  ADD UNIQUE KEY `Identificacion_UNIQUE` (`Identification`),
  ADD UNIQUE KEY `Correo_UNIQUE` (`Email`),
  ADD UNIQUE KEY `Telefono_UNIQUE` (`phones_number`);

--
-- Indices de la tabla `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`Id_product`),
  ADD UNIQUE KEY `Product_code_UNIQUE` (`Product_code`),
  ADD KEY `fk_Producto_Categoria1_idx` (`Id_Categoria`);

--
-- Indices de la tabla `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id_supplier`);

--
-- Indices de la tabla `supplier_has_products`
--
ALTER TABLE `supplier_has_products`
  ADD PRIMARY KEY (`Supplier_id_supplier`,`Products_Id_producto`),
  ADD KEY `fk_Supplier_has_Products_Products1_idx` (`Products_Id_producto`),
  ADD KEY `fk_Supplier_has_Products_Supplier1_idx` (`Supplier_id_supplier`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `category`
--
ALTER TABLE `category`
  MODIFY `Id_Category` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `company`
--
ALTER TABLE `company`
  MODIFY `id_company` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `invoice`
--
ALTER TABLE `invoice`
  MODIFY `id_invoice` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `payment_method`
--
ALTER TABLE `payment_method`
  MODIFY `id_Payment_method` tinyint(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `person`
--
ALTER TABLE `person`
  MODIFY `id_Person` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `products`
--
ALTER TABLE `products`
  MODIFY `Id_product` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `supplier`
--
ALTER TABLE `supplier`
  MODIFY `id_supplier` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `invoice`
--
ALTER TABLE `invoice`
  ADD CONSTRAINT `fk_invoice_company` FOREIGN KEY (`Id_company`) REFERENCES `company` (`id_company`),
  ADD CONSTRAINT `fk_invoice_payment_method` FOREIGN KEY (`Id_payment_method`) REFERENCES `payment_method` (`id_Payment_method`),
  ADD CONSTRAINT `fk_invoice_person` FOREIGN KEY (`Id_person`) REFERENCES `person` (`id_Person`);

--
-- Filtros para la tabla `invoice_products`
--
ALTER TABLE `invoice_products`
  ADD CONSTRAINT `fk_invoice_products_invoice` FOREIGN KEY (`id_invoice`) REFERENCES `invoice` (`id_invoice`);

--
-- Filtros para la tabla `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `fk_products_category` FOREIGN KEY (`Id_Categoria`) REFERENCES `category` (`Id_Category`);

--
-- Filtros para la tabla `supplier_has_products`
--
ALTER TABLE `supplier_has_products`
  ADD CONSTRAINT `fk_Supplier_has_Products_Products1` FOREIGN KEY (`Products_Id_producto`) REFERENCES `products` (`Id_product`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Supplier_has_Products_Supplier1` FOREIGN KEY (`Supplier_id_supplier`) REFERENCES `supplier` (`id_supplier`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
