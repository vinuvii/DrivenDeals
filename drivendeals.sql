-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2024 at 04:01 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drivendeals`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add vehicle', 7, 'add_vehicle'),
(26, 'Can change vehicle', 7, 'change_vehicle'),
(27, 'Can delete vehicle', 7, 'delete_vehicle'),
(28, 'Can view vehicle', 7, 'view_vehicle'),
(29, 'Can add user profile', 8, 'add_userprofile'),
(30, 'Can change user profile', 8, 'change_userprofile'),
(31, 'Can delete user profile', 8, 'delete_userprofile'),
(32, 'Can view user profile', 8, 'view_userprofile'),
(33, 'Can add bid', 9, 'add_bid'),
(34, 'Can change bid', 9, 'change_bid'),
(35, 'Can delete bid', 9, 'delete_bid'),
(36, 'Can view bid', 9, 'view_bid');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$4DhdO4RniUNLZjFVgslGID$xIQuXNTc7E34UKAH23uFd6vPPrNG+TO0K4d+sgYGBuI=', '2024-06-09 14:02:31.932474', 1, 'admin_1', '', '', '', 1, 1, '2024-06-09 13:11:31.224507');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bids_bid`
--

CREATE TABLE `bids_bid` (
  `id` bigint(20) NOT NULL,
  `bid_amount` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `bid_status` varchar(10) NOT NULL,
  `expiry_date` datetime(6) NOT NULL,
  `bidder_id` bigint(20) NOT NULL,
  `car_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-06-09 14:11:18.957433', '1', 'Q7 3.0 quattro TDI Premium Plus', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-06-09 15:04:14.210318', '2', 'Mercedes-Benz E-Class E 450 4MATIC WAGON AMG', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-06-10 07:23:30.699942', '3', 'Toyota Corolla S', 1, '[{\"added\": {}}]', 7, 1),
(4, '2024-06-11 06:28:22.581014', '4', 'Toyota Vitz KSP 130', 1, '[{\"added\": {}}]', 7, 1),
(5, '2024-06-11 06:40:35.777829', '5', 'BMW 318i M Sport', 1, '[{\"added\": {}}]', 7, 1),
(6, '2024-06-11 06:59:05.262902', '6', 'Mercedes Benz E200', 1, '[{\"added\": {}}]', 7, 1),
(7, '2024-06-11 08:03:35.706207', '7', 'Toyota Corolla 110 Crystal light', 1, '[{\"added\": {}}]', 7, 1),
(8, '2024-06-11 08:09:02.901150', '8', 'Land Rover Range Evoque', 1, '[{\"added\": {}}]', 7, 1),
(9, '2024-06-11 08:14:53.401275', '9', 'Suzuki Swift RS Turbo', 1, '[{\"added\": {}}]', 7, 1),
(10, '2024-06-11 08:20:54.503901', '10', 'Toyota Harrier Sport ( GS )', 1, '[{\"added\": {}}]', 7, 1),
(11, '2024-06-11 08:32:33.906739', '11', 'TAFE 45DI', 1, '[{\"added\": {}}]', 7, 1),
(12, '2024-06-11 09:14:02.218895', '12', 'TVS Ntorq', 1, '[{\"added\": {}}]', 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(9, 'bids', 'bid'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(8, 'user', 'userprofile'),
(7, 'vehicles', 'vehicle');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-09 12:52:08.736731'),
(2, 'auth', '0001_initial', '2024-06-09 12:52:09.775566'),
(3, 'admin', '0001_initial', '2024-06-09 12:52:10.027086'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-06-09 12:52:10.039104'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-09 12:52:10.059085'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-06-09 12:52:10.150402'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-06-09 12:52:10.601843'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-06-09 12:52:10.618840'),
(9, 'auth', '0004_alter_user_username_opts', '2024-06-09 12:52:10.626839'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-06-09 12:52:10.652846'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-06-09 12:52:10.656839'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-06-09 12:52:10.667841'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-06-09 12:52:10.682839'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-06-09 12:52:10.702893'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-06-09 12:52:10.735683'),
(16, 'auth', '0011_update_proxy_permissions', '2024-06-09 12:52:10.755546'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-06-09 12:52:10.782547'),
(18, 'sessions', '0001_initial', '2024-06-09 12:52:10.985747'),
(19, 'vehicles', '0001_initial', '2024-06-09 13:04:14.664306'),
(20, 'user', '0001_initial', '2024-06-09 13:04:54.932509'),
(21, 'vehicles', '0002_vehicle_posted_date', '2024-06-11 06:22:24.236817'),
(22, 'bids', '0001_initial', '2024-06-11 06:22:24.327013'),
(23, 'vehicles', '0003_alter_vehicle_posted_date', '2024-06-11 06:52:37.748756'),
(24, 'vehicles', '0004_alter_vehicle_posted_date', '2024-06-11 06:56:14.295580'),
(25, 'vehicles', '0005_alter_vehicle_posted_date', '2024-06-11 09:38:54.012882');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('w8slgv5r5p0xtuqbm81n186npbgjll87', '.eJxVjDsOwyAQBe9CHSHM16RM7zOgXRaCkwgkY1dR7h5bcpG0b-bNmwXY1hK2npYwE7uygV1-N4T4TPUA9IB6bzy2ui4z8kPhJ-18apRet9P9CxToZX9bjUAGwDtDA2krsyNyfnRJSuUyoQNI1koVSWchktGo9rowcjSeLLLPF_mAOGQ:1sGJ7v:ZxPWXsUmVEuUYkCfNfRwM5JCrQlZ38XWYAnxFW2wk9g', '2024-06-23 14:02:31.942534');

-- --------------------------------------------------------

--
-- Table structure for table `user_userprofile`
--

CREATE TABLE `user_userprofile` (
  `id` bigint(20) NOT NULL,
  `email_address` varchar(254) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `postal_code` varchar(10) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `vehicles_vehicle`
--

CREATE TABLE `vehicles_vehicle` (
  `id` bigint(20) NOT NULL,
  `model` varchar(100) NOT NULL,
  `year` int(10) UNSIGNED NOT NULL CHECK (`year` >= 0),
  `price` decimal(10,2) NOT NULL,
  `picture` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `posted_date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicles_vehicle`
--

INSERT INTO `vehicles_vehicle` (`id`, `model`, `year`, `price`, `picture`, `description`, `posted_date`) VALUES
(1, 'Q7 3.0 quattro TDI Premium Plus', 2012, '18500000.00', 'vehicle_pictures/2012_Q7_3.0_quattro_TDI_Premium_Plus.png', '2012 Audi Q7 3.0 Quattro TDI\r\n\r\n Super SHARP !\r\n - Desirable Diesel + \r\n3 Row Seats + \r\nALL Wheel Drive - \r\nSHARP\r\nDriven less than 9k Miles per year (112k miles total)\r\nGreat Fuel Economy almost 30 MPG HWY !!\r\n\r\nAmazing Car !!', '2024-06-11 06:22:24.211879'),
(2, 'Mercedes-Benz E-Class E 450 4MATIC WAGON AMG', 2019, '7689000.00', 'vehicle_pictures/2019_Mercedes-Benz_E-Class_E_450_4MATIC_WAGON_AMG.png', '2019 MERCEDES BENZ E450 4MATIC WAGON WITH REAR JUMP SEAT FOR 7 PASSENGER SEATING\r\n\r\nAMG APPEARENCE PKG.\r\n\r\nPREMIUM PKG.\r\n\r\nWHITE EXTERIOR WITH A BEAUTIFUL BEIGE MB TEX INTERIOR.\r\n\r\n3.0 LITER TWIN TURBOCHARGED ENGINE THAT DELIVERS OUTSTANDING PERFORMANCE AND SUPERIOR FUEL ECONOMY ALONG WITH THE LEGENDARY MERCEDES BENZ DRIVING EXPERIENCE.\r\n\r\nSMOOTH AND RESPONSIVE AUTOMATIC TRANSMISSION.\r\n\r\nALL WHEEL DRIVE FOR ENHANCED SAFTEY AND TRACTION IN ALL WEATHER CONDITIONS.\r\n\r\nICE COLD FRONT AND REAR AIR COND.\r\n\r\nHEATED FRONT SEATS.\r\n\r\nALL POWER.\r\n\r\nPOWER GLASS SLIDING SUNROOF.', '2024-06-11 06:22:24.211879'),
(3, 'Toyota Corolla S', 2015, '9800000.00', 'vehicle_pictures/2015_Toyota_Corolla_S.png', 'The 2015 Toyota Corolla S Edition boasts a sleek silver exterior free of any significant flaws and an interior that’s black with grey inserts, maintaining a like-new appearance. It’s powered by a 1.8 Litre engine that operates flawlessly without any mechanical concerns. This car has been meticulously serviced, which is evident from the CarFax report available for review. It comes equipped with all the standard features from this model year, all in perfect working condition. The vehicle presents well, offering a smooth driving experience, free of mechanical troubles, and is fitted with a good set of tires on factory alloy wheels. Emphasizing its aesthetic appeal, ease of driving, fuel efficiency, and excellent maintenance record, this Corolla S Edition is ready to deliver a reliable and enjoyable driving experience.', '2024-06-11 06:22:24.211879'),
(4, 'Toyota Vitz KSP 130', 2015, '7390000.00', 'vehicle_pictures/toyota_vitz_ksp_130_2015.png', 'Toyota Vitz Edition KSP130 2015 manufactured & registered 2018 car for quick sale. Sterling imported,  full history available.  88,000km done,  01st  owner. \r\n\r\n** Gun Metalic Grey exterior , original paint full body. Velvet interior with all 5  head rest seats. \r\n\r\n**  Smart entry,  Remote key,  retractable winker mirrors.\r\n\r\n**  Safety package, Auto brakes, Lane departure warning, traction control & Auto High Beam.\r\n\r\n**  Dual multifunctions, original Japaneese DVD player & reverse camera.\r\n\r\n**  Led Buffer light, Head light level adjusters, traction control.\r\n\r\n** Full options, power shutter, power mirrors, rear wiper.\r\n\r\n**  New tyres, Japan Alloys, New battery\r\n\r\nMint condition car for quick sale.', '2024-06-11 06:28:22.578008'),
(5, 'BMW 318i M Sport', 2016, '20900000.00', 'vehicle_pictures/BMW_318i_M_Sport_2016.jpg', '• BMW 318i M Sport \r\n\r\n• Manufactured 2016\r\n\r\n• Registered 2017\r\n\r\n• CAW-XXXX\r\n\r\n• 2nd Owner\r\n\r\n• 89,000Kms done\r\n\r\n• Genuine mileage\r\n\r\n• Alcantara Seats\r\n\r\n• Electric/Memory Seats\r\n\r\n• Wide Screen Display\r\n\r\n• Kick Boot\r\n\r\n• 18” Alloys\r\n\r\n• Key Less Entry\r\n\r\n• Lane Departure \r\n\r\n• Park Assist\r\n\r\n• Company maintained\r\n\r\n• Brand New Tyres', '2024-06-11 06:40:35.774784'),
(6, 'Mercedes Benz E200', 2014, '24600000.00', 'vehicle_pictures/Mercedes_Benz_E200_2014.jpg', 'MAKE: Mercedes Benz \r\n\r\nMODEL: E200\r\n\r\nYEAR OF MANUFACTURE: 2014\r\n\r\nYEAR OF REGISTRATION: 2014\r\n\r\nTRANSMISSION: Automatic\r\n\r\nSEATING CAPACITY: 5\r\n\r\nEXTERIOR COLOUR: Obsidian Black\r\n\r\nMILEAGE: 47,000 KM\r\n\r\nENGINE CAPACITY: 2000cc\r\n\r\nFUEL: Petrol\r\n\r\nOWNERS: 2nd Owner\r\n\r\nCOUNTRY OF ORIGIN: Germany\r\n\r\n• Leasing Can Be Arranged \r\n\r\n• Price Negotiable After Inspections Only.', '2024-06-11 06:59:05.251892'),
(7, 'Toyota Corolla 110 Crystal light', 1999, '2770000.00', 'vehicle_pictures/Toyota_Corolla_110_Crystal_light_1999.jpg', 'Toyota Corolla CE110 Crystal Light Car for quick sale. 1998 manufactured & 1999 brand new regd. \r\n\r\nRegd 4th owner, 327,000km genuine mileage. \r\n\r\n➡️  2000cc 2C molli engine, with manual 5 fwd gears. \r\n\r\n➡️  Retractable power mirrors\r\n\r\n➡️  Power shutters\r\n\r\n➡️  Center locking\r\n\r\n➡️  Rear arm rest, head rest\r\n\r\n➡️  CD player\r\n\r\n➡️  Crystal head lights\r\n\r\n➡️  Alloys and new tyres @ front.\r\n\r\nMechanically up to date.\r\n\r\n●  Engine is in perfect condition. \r\n\r\n●  Time belt changed recently.\r\n\r\n●  Engine & gear box mounts replaced\r\n\r\n●  water pump replaced. \r\n\r\n●  Superb running condition for it\'s age\r\n\r\nPrice Rs 2,775,000/= Sightly negotiable , upon inspection.', '2024-06-11 08:03:35.689793'),
(8, 'Land Rover Range Evoque', 2019, '56500000.00', 'vehicle_pictures/Land_Rover_Range_Evoque_2019.jpg', 'MAKE: Land Rover\r\n\r\nMODEL: Range Rover Evoque\r\n\r\nYEAR OF MANUFACTURE: 2019\r\n\r\nYEAR OF REGISTRATION: 2019\r\n\r\nTRANSMISSION: Automatic\r\n\r\nSEATING CAPACITY: 5\r\n\r\nEXTERIOR COLOUR: Nolita Grey\r\n\r\nMILEAGE: 36,000 KM\r\n\r\nENGINE CAPACITY: 2000cc\r\n\r\nFUEL: Petrol\r\n\r\nOWNERS: 1st Owner\r\n\r\nCOUNTRY OF ORIGIN: UK\r\n\r\nSpecs: Moonroof, Meridian Sound System, Electric and Memory Seats, Head Up Display, Power Boot, Ambient Light and many more…\r\n\r\n• Leasing Can Be Arranged \r\n\r\n• Price Negotiable After Inspections Only.', '2024-06-11 08:09:02.895788'),
(9, 'Suzuki Swift RS Turbo', 2017, '8690000.00', 'vehicle_pictures/2017-Suzuki-Swift-RS-Turbo-PakWheels-4.jpg', 'Suzuki Swift Rs Turbo\r\n\r\nYear 2017\r\n\r\nRegistered 2018\r\n\r\n1st owner\r\n\r\nFull option\r\n\r\nAuto Gear\r\n\r\nMultifunction steering \r\n\r\nPaddle shift\r\n\r\nRevers camera\r\n\r\nAccident free mint car\r\n\r\nQuick sale lease can be arranged on your request', '2024-06-11 08:14:53.137857'),
(10, 'Toyota Harrier Sport ( GS )', 2017, '26500000.00', 'vehicle_pictures/TOYOTA_HARRIER_SPORT__GS__.jpg', 'TOYOTA HARRIER SPORT ( GS ) \r\n\r\n	SPORT POWER MOOD \r\n\r\n	100 % Maintained By Toyota Lanka \r\n\r\n	Registered 2018 \r\n\r\n	88800 KM Original Millage \r\n\r\n	Black Color \r\n\r\n	Push Start \r\n\r\n	8 Air Bags \r\n\r\n	Central Locking \r\n\r\n	Multifunction Steering \r\n\r\n	Electric Seats \r\n\r\n	Rear Wiper \r\n\r\n	Rear Spoiler \r\n\r\n	Bluetooth / DVD /USB\r\n\r\n	Rear Camera \r\n\r\n	Dual AC / Touch AC \r\n\r\n	Alloy wheels\r\n\r\n	Over head Mirror TV \r\n\r\n	Retract Mirrors\r\n\r\n	ABS \r\n\r\n	Power Shutter\r\n\r\n•	Immediate Sale \r\n\r\n•	Can Negotiate \r\n\r\n•	Executive personal used \r\n\r\n•	Can be seen after the appointment \r\n\r\n*Location :  Colombo 06', '2024-06-11 08:20:54.497886'),
(11, 'TAFE 45DI', 2022, '3600000.00', 'vehicle_pictures/TAFE_45DI_2022.jpg', 'In Jaffna town\r\n\r\nReg number - RH-XXXX\r\n\r\nFirst owner\r\n\r\nUsed only 950 hours\r\n\r\nBrand new condition \r\n\r\nPersonal used only. No mud use. \r\n\r\nNo damages\r\n\r\nServiced regularly and maintained well', '2024-06-11 08:32:33.891099'),
(12, 'TVS Ntorq', 2023, '780000.00', 'vehicle_pictures/TVS_Ntorq_2023.jpg', 'TVS Ntorq 2023 For Sale\r\n\r\n????Brand New Condition\r\n\r\n????125cc\r\n\r\n????First Owner\r\n\r\n????350km\r\n\r\n????Price - 780,000', '2024-06-11 09:14:02.210388');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `bids_bid`
--
ALTER TABLE `bids_bid`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bids_bid_bidder_id_8ba622b0_fk_user_userprofile_id` (`bidder_id`),
  ADD KEY `bids_bid_car_id_e2067132_fk_vehicles_vehicle_id` (`car_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `user_userprofile`
--
ALTER TABLE `user_userprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `vehicles_vehicle`
--
ALTER TABLE `vehicles_vehicle`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bids_bid`
--
ALTER TABLE `bids_bid`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `user_userprofile`
--
ALTER TABLE `user_userprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vehicles_vehicle`
--
ALTER TABLE `vehicles_vehicle`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `bids_bid`
--
ALTER TABLE `bids_bid`
  ADD CONSTRAINT `bids_bid_bidder_id_8ba622b0_fk_user_userprofile_id` FOREIGN KEY (`bidder_id`) REFERENCES `user_userprofile` (`id`),
  ADD CONSTRAINT `bids_bid_car_id_e2067132_fk_vehicles_vehicle_id` FOREIGN KEY (`car_id`) REFERENCES `vehicles_vehicle` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `user_userprofile`
--
ALTER TABLE `user_userprofile`
  ADD CONSTRAINT `user_userprofile_user_id_2474538d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
