-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 22, 2024 at 12:53 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

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
(36, 'Can view bid', 9, 'view_bid'),
(37, 'Can add listing', 10, 'add_listing'),
(38, 'Can change listing', 10, 'change_listing'),
(39, 'Can delete listing', 10, 'delete_listing'),
(40, 'Can view listing', 10, 'view_listing'),
(41, 'Can add watchlist item', 11, 'add_watchlistitem'),
(42, 'Can change watchlist item', 11, 'change_watchlistitem'),
(43, 'Can delete watchlist item', 11, 'delete_watchlistitem'),
(44, 'Can view watchlist item', 11, 'view_watchlistitem'),
(45, 'Can add user', 12, 'add_user'),
(46, 'Can change user', 12, 'change_user'),
(47, 'Can delete user', 12, 'delete_user'),
(48, 'Can view user', 12, 'view_user'),
(49, 'Can add user watchlist item', 13, 'add_userwatchlistitem'),
(50, 'Can change user watchlist item', 13, 'change_userwatchlistitem'),
(51, 'Can delete user watchlist item', 13, 'delete_userwatchlistitem'),
(52, 'Can view user watchlist item', 13, 'view_userwatchlistitem'),
(53, 'Can add watchlist', 14, 'add_watchlist'),
(54, 'Can change watchlist', 14, 'change_watchlist'),
(55, 'Can delete watchlist', 14, 'delete_watchlist'),
(56, 'Can view watchlist', 14, 'view_watchlist');

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
(1, 'pbkdf2_sha256$720000$4DhdO4RniUNLZjFVgslGID$xIQuXNTc7E34UKAH23uFd6vPPrNG+TO0K4d+sgYGBuI=', '2024-06-13 14:28:48.248176', 1, 'admin_1', '', '', '', 1, 1, '2024-06-09 13:11:31.224507');

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
  `amount` decimal(10,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `bid_status` varchar(10) NOT NULL,
  `expiry_date` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `vehicle_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bids_bid`
--

INSERT INTO `bids_bid` (`id`, `amount`, `timestamp`, `bid_status`, `expiry_date`, `user_id`, `vehicle_id`) VALUES
(12, '5100000.00', '2024-06-22 10:17:48.359477', 'PENDING', '2024-06-29 10:17:48.358480', 4, 21),
(13, '5950000.00', '2024-06-22 10:25:13.913335', 'PENDING', '2024-06-23 10:25:13.913335', 4, 22),
(14, '12050010.00', '2024-06-22 10:25:36.843926', 'PENDING', '2024-06-24 10:25:36.842538', 4, 23),
(15, '7555500.00', '2024-06-22 10:26:00.276742', 'PENDING', '2024-06-25 10:26:00.275657', 4, 27),
(16, '3700000.00', '2024-06-22 10:26:14.863017', 'PENDING', '2024-06-29 10:26:14.863017', 4, 28),
(17, '930000.00', '2024-06-22 10:26:23.681432', 'PENDING', '2024-06-27 10:26:23.681432', 4, 29),
(18, '8790000.00', '2024-06-22 10:26:48.930351', 'PENDING', '2024-06-23 10:26:48.930351', 4, 30),
(19, '18550000.00', '2024-06-22 10:28:20.117386', 'PENDING', '2024-06-26 10:28:20.117386', 4, 32),
(20, '4590010.00', '2024-06-22 10:28:42.197777', 'PENDING', '2024-06-27 10:28:42.197777', 4, 33),
(21, '5250000.00', '2024-06-22 10:50:36.826819', 'PENDING', '2024-06-29 10:17:48.361711', 1, 21),
(22, '1030000.00', '2024-06-22 10:50:53.262253', 'PENDING', '2024-06-27 10:26:23.689252', 1, 29),
(23, '4800000.00', '2024-06-22 10:51:05.863819', 'PENDING', '2024-06-29 10:51:05.863819', 1, 31),
(24, '4690010.00', '2024-06-22 10:51:21.887613', 'PENDING', '2024-06-27 10:28:42.200284', 1, 33);

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
(10, 'user', 'listing'),
(12, 'user', 'user'),
(8, 'user', 'userprofile'),
(13, 'user', 'userwatchlistitem'),
(14, 'user', 'watchlist'),
(11, 'user', 'watchlistitem'),
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
(25, 'vehicles', '0005_alter_vehicle_posted_date', '2024-06-11 09:38:54.012882'),
(26, 'user', '0002_remove_userprofile_email_address', '2024-06-13 14:14:13.793917'),
(27, 'user', '0003_userprofile_email_address', '2024-06-13 14:14:13.828894'),
(28, 'user', '0004_userprofile_trading_address', '2024-06-13 14:14:13.856543'),
(29, 'user', '0005_alter_userprofile_trading_address', '2024-06-13 14:14:13.935426'),
(30, 'user', '0006_listing', '2024-06-13 14:14:14.028841'),
(31, 'user', '0007_watchlistitem', '2024-06-13 14:14:14.140242'),
(32, 'user', '0008_rename_user_userprofile_user_name', '2024-06-13 14:14:15.240493'),
(33, 'user', '0009_rename_user_name_userprofile_user', '2024-06-13 14:14:15.453902'),
(34, 'user', '0010_user_alter_listing_user_alter_userprofile_user_and_more', '2024-06-13 14:14:40.010404'),
(35, 'user', '0011_alter_user_options_alter_user_managers_and_more', '2024-06-13 14:39:08.820799'),
(36, 'user', '0012_alter_user_password', '2024-06-16 06:17:31.003274'),
(37, 'vehicles', '0006_vehicle_color_vehicle_mileage', '2024-06-16 06:17:31.034731'),
(38, 'vehicles', '0007_vehicle_body_type_vehicle_engine_capacity_and_more', '2024-06-16 06:17:31.114407'),
(39, 'vehicles', '0008_vehicle_abs_breaks_vehicle_air_conditioning_and_more', '2024-06-16 06:17:31.286841'),
(40, 'vehicles', '0009_vehicle_picture2_vehicle_picture3', '2024-06-16 06:17:31.314416'),
(41, 'vehicles', '0010_vehicle_seller', '2024-06-16 06:17:31.382316'),
(42, 'bids', '0002_rename_bid_amount_bid_amount_and_more', '2024-06-16 10:38:43.178589'),
(43, 'bids', '0003_alter_bid_options', '2024-06-16 16:11:22.481745'),
(44, 'vehicles', '0011_alter_vehicle_engine_type_and_more', '2024-06-17 04:11:38.422475'),
(45, 'user', '0013_userwatchlistitem_watchlist_delete_watchlistitem', '2024-06-17 12:29:37.818076'),
(46, 'user', '0014_alter_watchlist_unique_together_and_more', '2024-06-17 12:29:38.482563'),
(47, 'user', '0015_alter_userwatchlistitem_unique_together_and_more', '2024-06-22 10:16:57.540577'),
(48, 'vehicles', '0012_vehicle_auction_duration_days', '2024-06-22 10:16:57.596775'),
(49, 'vehicles', '0013_vehicle_first_bid_date', '2024-06-22 10:16:57.616776');

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
('nwpw2w5c2felm7bcr7tf65za7x1g8r0r', '.eJxVjEEOgjAQRe_StWnodKAdl-49QzPtDIIaSCisjHdXEha6_e-9_zKJt3VIW9UljWLOpjWn3y1zeei0A7nzdJttmad1GbPdFXvQaq-z6PNyuH8HA9fhW3ODAKgOHIloACCIRYPzxKHx3nEsSEo9llzaHj06jVEDkgB56Trz_gDGSTcm:1sJaFm:T9UeTwk-0LN9hYXx0UphxOQ4FOskbAgEYq1clRmuV9Y', '2024-07-02 14:56:10.044636'),
('vhovfa0m1bjalyorx9c1jdzfn2jss767', '.eJxVjEEOgjAQRe_StWkGqLR16Z4zNDOdGYsaSCisjHdXEha6_e-9_zIJt7WkrcqSRjYX05jT70aYHzLtgO843Wab52ldRrK7Yg9a7TCzPK-H-3dQsJZvHaR1EN2ZCDySIIOXrteuVW1AEaNrpWeIWckrhSjMIYdGM0cFcmjeHwJbOVU:1sKy2u:CGBz9L-HBMokR5IoD6qHo3pY0Vl7po8O4C-fTBoJZ0s', '2024-07-06 10:32:36.466246'),
('w1bardw1dzj8vd7m82hyr8f54a616w62', '.eJxVjEEOgjAQRe_StWkGqLR16Z4zNDOdGYsaSCisjHdXEha6_e-9_zIJt7WkrcqSRjYX05jT70aYHzLtgO843Wab52ldRrK7Yg9a7TCzPK-H-3dQsJZvHaR1EN2ZCDySIIOXrteuVW1AEaNrpWeIWckrhSjMIYdGM0cFcmjeHwJbOVU:1sIjmn:Ytv61AaBN_iRe-XPR9a9ZpE_-YOhkKjz-hZe6C90Qnk', '2024-06-30 06:54:45.214359'),
('w8slgv5r5p0xtuqbm81n186npbgjll87', '.eJxVjDsOwyAQBe9CHSHM16RM7zOgXRaCkwgkY1dR7h5bcpG0b-bNmwXY1hK2npYwE7uygV1-N4T4TPUA9IB6bzy2ui4z8kPhJ-18apRet9P9CxToZX9bjUAGwDtDA2krsyNyfnRJSuUyoQNI1koVSWchktGo9rowcjSeLLLPF_mAOGQ:1sGJ7v:ZxPWXsUmVEuUYkCfNfRwM5JCrQlZ38XWYAnxFW2wk9g', '2024-06-23 14:02:31.942534');

-- --------------------------------------------------------

--
-- Table structure for table `user_listing`
--

CREATE TABLE `user_listing` (
  `id` bigint(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_user`
--

CREATE TABLE `user_user` (
  `id` bigint(20) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(128) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `postal_code` varchar(10) NOT NULL,
  `trading_address` longtext NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_user`
--

INSERT INTO `user_user` (`id`, `username`, `password`, `email`, `first_name`, `last_name`, `mobile_number`, `postal_code`, `trading_address`, `date_joined`, `is_active`, `is_staff`, `is_superuser`, `last_login`) VALUES
(1, 'Jane_Fernando', 'pbkdf2_sha256$720000$7vFls4MVg806f21pLdgy8l$rkB6bhQccGIDYGhtmLAoF7sEzkHjf02/yecC7acMumc=', 'islandexplorer@example.com', 'Jane', 'Fernando', '+94 76 987 6543', '20050', '12 Palm Grove, Negombo, Sri Lanka', '2024-06-13 14:48:07.098245', 1, 0, 0, '2024-06-22 10:32:36.460199'),
(2, 'Jason_Fonseka', 'pbkdf2_sha256$720000$ThTJoXgSrQ3uzD0mygoBhH$qbATyNhtqiDhfjWYgwurGF9LAgRLz1cVXLCYopV8iWI=', 'adventureseeker88@example.com', 'Jason', 'Fonseka', '+94 71 876 5432', '30025', '8 Sea View Road, Galle, Sri Lanka', '2024-06-18 11:43:38.828563', 1, 0, 0, '2024-06-18 13:40:17.908021'),
(3, 'Pete_Peiris', 'pbkdf2_sha256$720000$Q6Kxf70BN6PrzYByjSyZ6w$qVFA24IVteyHjeqcR+VkEDGFw/4QO9ta9rU/TZCYLyg=', 'pete.peiris@example.com', 'Pete', 'Peris', '+94 70 123 4567', '40090', '25 Lake Road, Kandy, Sri Lanka', '2024-06-18 12:22:35.054592', 1, 0, 0, '2024-06-18 14:00:40.647174'),
(4, 'Nimal_Fernando', 'pbkdf2_sha256$720000$KdXkj1ifY2d9fNxpmB8s9j$Qs4J4DMXXoAT1vUFmj/tJ+RnOC1+kaj6ld3S+XRqekc=', 'lankanuser123@example.com', 'Nimal', 'Fernando', '+94 77 123 4567', '10000', '45A, Lotus Lane, Colombo 07, Sri Lanka', '2024-06-18 14:19:26.814086', 1, 0, 0, '2024-06-22 10:17:37.637546'),
(5, 'Savindi', 'pbkdf2_sha256$720000$HomqCdtc9FYFpZ9G5Vr1eh$KW5JlkkeNBz7ALo8igEOmzN6IyoEA3SAVGNOelZiuVc=', 'savindi.dias@example.com', 'Savindi', 'Dias', '+94 76 234 5678', '50070', '15 Jasmine Avenue, Nuwara Eliya, Sri Lanka', '2024-06-18 14:56:09.124282', 1, 0, 0, '2024-06-18 14:56:10.028921');

-- --------------------------------------------------------

--
-- Table structure for table `user_user_groups`
--

CREATE TABLE `user_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_user_user_permissions`
--

CREATE TABLE `user_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_watchlist`
--

CREATE TABLE `user_watchlist` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `vehicle_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_watchlist`
--

INSERT INTO `user_watchlist` (`id`, `user_id`, `vehicle_id`) VALUES
(5, 3, 21),
(6, 3, 23),
(7, 5, 27),
(8, 4, 21),
(9, 4, 22),
(10, 4, 33);

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
  `posted_date` datetime(6) DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `mileage` int(10) UNSIGNED NOT NULL CHECK (`mileage` >= 0),
  `body_type` varchar(100) DEFAULT NULL,
  `engine_capacity` decimal(4,1) DEFAULT NULL,
  `engine_type` varchar(32) DEFAULT NULL,
  `fuel_type` varchar(20) DEFAULT NULL,
  `make` varchar(100) DEFAULT NULL,
  `no_of_seats` int(10) UNSIGNED NOT NULL CHECK (`no_of_seats` >= 0),
  `transmission_type` varchar(10) DEFAULT NULL,
  `abs_breaks` tinyint(1) NOT NULL,
  `air_conditioning` tinyint(1) NOT NULL,
  `airbags` tinyint(1) NOT NULL,
  `alloy_wheels` tinyint(1) NOT NULL,
  `central_locking` tinyint(1) NOT NULL,
  `leather_seats` tinyint(1) NOT NULL,
  `power_steering` tinyint(1) NOT NULL,
  `power_windows` tinyint(1) NOT NULL,
  `reverse_camera` tinyint(1) NOT NULL,
  `sunroof` tinyint(1) NOT NULL,
  `picture2` varchar(100) DEFAULT NULL,
  `picture3` varchar(100) DEFAULT NULL,
  `seller_id` bigint(20) DEFAULT NULL,
  `auction_duration_days` int(10) UNSIGNED NOT NULL CHECK (`auction_duration_days` >= 0),
  `first_bid_date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicles_vehicle`
--

INSERT INTO `vehicles_vehicle` (`id`, `model`, `year`, `price`, `picture`, `description`, `posted_date`, `color`, `mileage`, `body_type`, `engine_capacity`, `engine_type`, `fuel_type`, `make`, `no_of_seats`, `transmission_type`, `abs_breaks`, `air_conditioning`, `airbags`, `alloy_wheels`, `central_locking`, `leather_seats`, `power_steering`, `power_windows`, `reverse_camera`, `sunroof`, `picture2`, `picture3`, `seller_id`, `auction_duration_days`, `first_bid_date`) VALUES
(21, 'Corolla', 2023, '5000000.00', 'vehicle_pictures/Coralla1.jpg', 'Discover elegance and reliability with our pristine Toyota Corolla, a timeless sedan designed for comfort and efficiency. This 2023 model in sleek silver boasts modern features and safety enhancements, ensuring a smooth ride for every journey. Ideal for discerning drivers seeking quality and value.', '2024-06-18 13:35:04.412298', 'Silver', 1000, 'sedan', '18.0', 'Hybrid', 'petrol', 'Toyota', 5, 'Automatic', 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 'vehicle_pictures/Corolla_2.jpg', 'vehicle_pictures/corolla3.jpg', 2, 7, '2024-06-22 10:17:48.361711'),
(22, 'Civic', 2023, '5800000.00', 'vehicle_pictures/Honda1.jpg', 'Introducing the dynamic Honda Civic, a standout sedan delivering performance and style. This 2023 model in striking red combines sporty design with premium amenities, including a turbocharged engine for exhilarating drives. Perfect for those who crave sophistication and innovation.', '2024-06-18 13:39:22.325011', 'Red', 0, 'sedan', '1.5', 'Hybrid', 'petrol', 'Honda', 5, 'Automatic', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'vehicle_pictures/Honda2.jpg', 'vehicle_pictures/Honda3.jpg', 2, 1, '2024-06-22 10:25:13.921570'),
(23, 'Sprinter', 2024, '12000000.00', 'vehicle_pictures/Benze1.jpg', 'The Mercedes-Benz Sprinter Minibus is designed for transporting passengers with comfort and efficiency in mind. Built on a solid platform with a 2.1-liter inline-4 diesel engine and automatic transmission, it combines reliability with fuel efficiency. This minibus can seat up to 12 passengers comfortably, equipped with essential features like ABS brakes, airbags, air conditioning, power steering, central locking, and a reverse camera for added safety and convenience. It\'s an ideal choice for businesses or organizations needing a reliable people-mover that offers a blend of practicality and comfort.', '2024-06-18 13:47:44.945029', 'White', 0, 'bus', '2.1', 'Internal Combustion Engine', 'diesel', 'Mercedes-Benz', 12, 'Automatic', 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 'vehicle_pictures/Benze2.jpg', 'vehicle_pictures/Benze3.jpg', 2, 2, '2024-06-22 10:25:36.846360'),
(24, 'F-150', 2022, '9000000.00', 'vehicle_pictures/Ford1.jpg', 'The Ford F-150 is a robust and versatile pickup truck known for its durability and capability. Featuring a powerful 3.5-liter V6 engine paired with an automatic transmission, it offers excellent performance both on and off the road. With a spacious cabin accommodating up to 5 passengers, it includes modern amenities such as ABS brakes, alloy wheels, airbags, air conditioning, power steering, power windows, central locking, and a reverse camera. Ideal for those seeking a reliable vehicle for heavy-duty tasks without compromising on comfort and safety.', '2024-06-18 13:51:51.844288', 'Blue', 5000, 'truck', '3.5', 'Internal Combustion Engine', 'diesel', 'Ford', 5, 'Automatic', 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 'vehicle_pictures/Ford2.jpg', 'vehicle_pictures/Ford3.jpg', 1, 4, NULL),
(25, 'RE Auto Rickshaw', 2023, '800000.00', 'vehicle_pictures/tuk1.jpg', 'Discover the reliable Bajaj RE Auto Rickshaw, a trusted companion for urban commuting and short-distance travel. Known for its sturdy build and economical performance, this auto rickshaw is ideal for navigating bustling city streets with ease. Perfect for drivers looking for affordability and durability in their daily transportation solution.', '2024-06-18 13:56:33.355841', 'Yellow', 7000, 'three_wheeler', '0.2', 'Internal Combustion Engine', 'petrol', 'other', 3, 'Manual', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'vehicle_pictures/tuk2.jpg', '', 1, 3, NULL),
(26, 'YZF-R6', 2022, '2500000.00', 'vehicle_pictures/bike1.jpg', 'Experience exhilaration with the Yamaha YZF-R6, a high-performance sportbike designed for thrill-seeking riders. Renowned for its agility and power, the YZF-R6 delivers precision handling and impressive acceleration, making it a favorite on both the track and the road. Embrace the excitement of riding with Yamaha\'s legendary engineering and sleek design.', '2024-06-18 14:00:15.364594', 'Blue', 5000, 'motorbike', '0.6', 'Internal Combustion Engine', 'petrol', 'other', 2, 'Manual', 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 'vehicle_pictures/bike2.jpg', 'vehicle_pictures/bike3.jpg', 1, 6, NULL),
(27, 'Camry', 2023, '7500000.00', 'vehicle_pictures/Camry1.jpg', 'Embrace sophistication and reliability with the Toyota Camry, a flagship sedan renowned for its comfort, performance, and lasting appeal. Ideal for discerning drivers seeking a blend of style and practicality, the Camry excels with its spacious interior, advanced technology features, and smooth driving experience. Whether navigating city streets or embarking on long journeys, the Camry delivers a harmonious balance of luxury and efficiency, making it a timeless choice in the sedan segment.', '2024-06-18 14:05:24.838227', 'Silver', 1000, 'sedan', '2.5', 'Hybrid', 'hybrid', 'Toyota', 5, 'Automatic', 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 'vehicle_pictures/Camry2.jpg', 'vehicle_pictures/Camry3.jpg', 3, 3, '2024-06-22 10:26:00.279805'),
(28, '45DI', 2018, '3600000.00', 'vehicle_pictures/tracktor.jpg', 'The TAFE 45DI is a robust and reliable tractor designed for agricultural purposes. Known for its durability and simplicity, it offers essential features for farm work and rural applications, ensuring dependable performance in demanding conditions.', '2024-06-18 14:14:29.402653', 'Red', 1000, 'tractor', '1.0', 'Internal Combustion Engine', 'diesel', 'other', 1, 'Manual', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'vehicle_pictures/tracktor2.jpg', 'vehicle_pictures/tracktor3.jpg', 3, 7, '2024-06-22 10:26:14.869855'),
(29, 'Ntorq', 2023, '780000.00', 'vehicle_pictures/Bikke1.jpg', 'The TVS Ntorq is a sporty and feature-packed scooter that appeals to urban riders seeking style and performance. It combines modern design elements with practical features such as a digital instrument cluster, smartphone connectivity, and a peppy engine, making it an ideal choice for daily commuting with a touch of excitement.', '2024-06-18 14:17:33.722131', 'Red', 500, 'motorbike', '0.2', 'Internal Combustion Engine', 'petrol', 'other', 2, 'Automatic', 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 'vehicle_pictures/Bikke2.jpg', 'vehicle_pictures/Bikke3.jpg', 3, 5, '2024-06-22 10:26:23.689252'),
(30, 'Swift RS Turbo', 2023, '8690000.00', 'vehicle_pictures/susuki1.jpg', 'The Suzuki Swift RS Turbo blends sporty design with practicality, offering agile handling and turbocharged performance. It features advanced safety technologies, modern interior amenities, and a stylish exterior, making it a popular choice among enthusiasts and everyday drivers alike.', '2024-06-18 14:24:28.090812', 'White', 750, 'car', '1.0', 'Hybrid', 'petrol', 'Suzuki', 5, 'Automatic', 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 'vehicle_pictures/susuki2.jpg', '', 4, 1, '2024-06-22 10:26:48.933380'),
(31, 'Ashok Leyland JanBu', 2024, '4700000.00', 'vehicle_pictures/bus1.jpg', 'Ashok Leyland buses are renowned for their robust build quality, reliability, and versatility. They are widely used for public transportation, school buses, intercity travel, and special applications such as tourist coaches. Featuring spacious interiors, comfortable seating arrangements, and advanced engineering, Ashok Leyland buses cater to both passenger comfort and safety. Equipped with modern technology and designed for efficient performance, these buses are a preferred choice for fleet operators and transportation companies looking for durability and operational excellence.', '2024-06-18 14:35:03.290650', 'White', 0, 'bus', '1.5', 'Internal Combustion Engine', 'diesel', 'other', 60, 'Manual', 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 'vehicle_pictures/Bus2.jpg', '', 4, 7, '2024-06-22 10:51:05.863819'),
(32, 'CX-5', 2017, '18500000.00', 'vehicle_pictures/mazda1.jpg', 'The Mazda CX-5 combines stylish design with sporty performance and practicality. It offers a comfortable and upscale interior, advanced safety features, and a smooth driving experience suitable for both city and highway driving. With its responsive handling and versatile cargo space, the CX-5 is a popular choice among SUV enthusiasts seeking a blend of luxury and utility.', '2024-06-18 15:02:50.188755', 'Blue', 120000, 'suv', '2.0', 'Internal Combustion Engine', 'petrol', 'Mazda', 5, 'Automatic', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'vehicle_pictures/maxda2.jpg', '', 5, 4, '2024-06-22 10:28:20.122773'),
(33, 'Vitz', 2023, '4590000.00', 'vehicle_pictures/vitz1.jpg', 'The Toyota Vitz (Yaris) is a reliable and fuel-efficient hatchback known for its compact size and practicality. It offers agile handling, a comfortable interior, and a range of modern features suitable for urban commuting. With Toyota\'s reputation for reliability and affordability, the Vitz appeals to drivers looking for a dependable and economical everyday car.', '2024-06-18 15:06:39.386820', 'Red', 1000, 'car', '13.0', 'Hybrid', 'hybrid', 'Toyota', 5, 'Automatic', 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 'vehicle_pictures/vitz2.jpg', 'vehicle_pictures/vitz3.jpg', 5, 5, '2024-06-22 10:28:42.200284');

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
  ADD KEY `bids_bid_user_id_5ba34cc3_fk_user_user_id` (`user_id`),
  ADD KEY `bids_bid_vehicle_id_7d750961_fk_vehicles_vehicle_id` (`vehicle_id`);

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
-- Indexes for table `user_listing`
--
ALTER TABLE `user_listing`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_listing_user_id_2d0025b5_fk_user_user_id` (`user_id`);

--
-- Indexes for table `user_user`
--
ALTER TABLE `user_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_user_email_1c6f3d1a_uniq` (`email`),
  ADD UNIQUE KEY `user_user_mobile_number_86347fff_uniq` (`mobile_number`),
  ADD UNIQUE KEY `user_user_username_e2bdfe0c_uniq` (`username`);

--
-- Indexes for table `user_user_groups`
--
ALTER TABLE `user_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_user_groups_user_id_group_id_bb60391f_uniq` (`user_id`,`group_id`),
  ADD KEY `user_user_groups_group_id_c57f13c0_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq` (`user_id`,`permission_id`),
  ADD KEY `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `user_watchlist`
--
ALTER TABLE `user_watchlist`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_watchlist_vehicle_id_fbac1da1_fk_vehicles_vehicle_id` (`vehicle_id`),
  ADD KEY `user_watchlist_user_id_cf69f936` (`user_id`);

--
-- Indexes for table `vehicles_vehicle`
--
ALTER TABLE `vehicles_vehicle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vehicles_vehicle_seller_id_8b3ef8e4_fk_user_user_id` (`seller_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `user_listing`
--
ALTER TABLE `user_listing`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_user`
--
ALTER TABLE `user_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user_user_groups`
--
ALTER TABLE `user_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_watchlist`
--
ALTER TABLE `user_watchlist`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `vehicles_vehicle`
--
ALTER TABLE `vehicles_vehicle`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

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
  ADD CONSTRAINT `bids_bid_user_id_5ba34cc3_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`),
  ADD CONSTRAINT `bids_bid_vehicle_id_7d750961_fk_vehicles_vehicle_id` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles_vehicle` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `user_listing`
--
ALTER TABLE `user_listing`
  ADD CONSTRAINT `user_listing_user_id_2d0025b5_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Constraints for table `user_user_groups`
--
ALTER TABLE `user_user_groups`
  ADD CONSTRAINT `user_user_groups_group_id_c57f13c0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_user_groups_user_id_13f9a20d_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Constraints for table `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  ADD CONSTRAINT `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_user_user_permissions_user_id_31782f58_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Constraints for table `user_watchlist`
--
ALTER TABLE `user_watchlist`
  ADD CONSTRAINT `user_watchlist_user_id_cf69f936_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`),
  ADD CONSTRAINT `user_watchlist_vehicle_id_fbac1da1_fk_vehicles_vehicle_id` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles_vehicle` (`id`);

--
-- Constraints for table `vehicles_vehicle`
--
ALTER TABLE `vehicles_vehicle`
  ADD CONSTRAINT `vehicles_vehicle_seller_id_8b3ef8e4_fk_user_user_id` FOREIGN KEY (`seller_id`) REFERENCES `user_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
