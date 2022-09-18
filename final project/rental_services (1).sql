-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2022 at 09:28 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rental_services`
--

-- --------------------------------------------------------

--
-- Table structure for table `booked_hall_table`
--

CREATE TABLE `booked_hall_table` (
  `booked_id` int(11) NOT NULL,
  `hall_id` int(11) NOT NULL,
  `hall_name` varchar(100) NOT NULL,
  `hall_address` varchar(50) NOT NULL,
  `hall_district` varchar(50) NOT NULL,
  `hall_price` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `owner_fname` varchar(50) NOT NULL,
  `owner_lname` varchar(50) NOT NULL,
  `owner_contact` int(11) NOT NULL,
  `owner_email` varchar(50) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_fname` varchar(50) NOT NULL,
  `customer_lname` varchar(50) NOT NULL,
  `customer_contact` int(11) NOT NULL,
  `customer_email` varchar(80) NOT NULL,
  `booked_for` date NOT NULL,
  `date_booked_on` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booked_hall_table`
--

INSERT INTO `booked_hall_table` (`booked_id`, `hall_id`, `hall_name`, `hall_address`, `hall_district`, `hall_price`, `owner_id`, `owner_fname`, `owner_lname`, `owner_contact`, `owner_email`, `customer_id`, `customer_fname`, `customer_lname`, `customer_contact`, `customer_email`, `booked_for`, `date_booked_on`) VALUES
(7, 29, 'Crystal Banquet', 'Manbhawan', 'Lalitpur', 11000, 13, 'sagar', 'kc', 984123456, 'sagar@gmail.com', 16, 'khom', 'thapa', 2147483647, 'khom@gmail.com', '2022-09-03', '2022-09-12'),
(8, 22, 'WOW Hall & Bouqute', 'jamal', 'kathmandu', 10000, 6, 'rakesh', 'thapa', 984123456, 'rakesh@gmail.com', 16, 'khom', 'thapa', 2147483647, 'khom@gmail.com', '2022-09-03', '2022-09-12'),
(9, 30, 'Balaji banquet', 'Koteshwor', 'Kathmandu', 2000, 26, 'dhiraj', 'chaudary', 2147483647, 'dhiraj@gmail.com', 24, 'ujwal', 'rai', 2147483647, 'ujwal@gmail.com', '2022-09-23', '2022-09-13');

-- --------------------------------------------------------

--
-- Table structure for table `booked_vehicle_table`
--

CREATE TABLE `booked_vehicle_table` (
  `booked_id` int(11) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  `vehicle_category` varchar(20) NOT NULL,
  `vehicle_number` varchar(50) NOT NULL,
  `vehicle_address` varchar(50) NOT NULL,
  `vehicle_district` varchar(50) NOT NULL,
  `vehicle_company` varchar(50) NOT NULL,
  `vehicle_price` int(11) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `owner_firstName` varchar(50) NOT NULL,
  `owner_lastName` varchar(50) NOT NULL,
  `owner_contact` int(11) NOT NULL,
  `owner_email` varchar(80) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_fname` varchar(50) NOT NULL,
  `customer_lname` varchar(50) NOT NULL,
  `customer_contact` int(11) NOT NULL,
  `customer_email` varchar(80) NOT NULL,
  `booked_for` date NOT NULL,
  `booked_on_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booked_vehicle_table`
--

INSERT INTO `booked_vehicle_table` (`booked_id`, `vehicle_id`, `vehicle_category`, `vehicle_number`, `vehicle_address`, `vehicle_district`, `vehicle_company`, `vehicle_price`, `owner_id`, `owner_firstName`, `owner_lastName`, `owner_contact`, `owner_email`, `customer_id`, `customer_fname`, `customer_lname`, `customer_contact`, `customer_email`, `booked_for`, `booked_on_date`) VALUES
(24, 39, 'Suv', '2264', 'Kalimati', 'Kathmandu', 'Toyata', 3000, 26, 'dhiraj', 'chaudary', 2147483647, 'dhiraj@gmail.com', 44, 'salim', 'maharjan', 2147483647, 'salim.171329@ncit.edu.np', '2022-09-02', '2022-09-13'),
(25, 39, 'Suv', '2264', 'Kalimati', 'Kathmandu', 'Toyata', 3000, 26, 'dhiraj', 'chaudary', 2147483647, 'dhiraj@gmail.com', 44, 'salim', 'maharjan', 2147483647, 'salim.171329@ncit.edu.np', '2022-09-02', '2022-09-13'),
(26, 39, 'Suv', '2264', 'Kalimati', 'Kathmandu', 'Toyata', 3000, 26, 'dhiraj', 'chaudary', 2147483647, 'dhiraj@gmail.com', 24, 'ujwal', 'rai', 2147483647, 'ujwal@gmail.com', '2022-09-17', '2022-09-16');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `Id` int(11) NOT NULL,
  `sender` varchar(100) NOT NULL,
  `reciver` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`Id`, `sender`, `reciver`) VALUES
(1, 'sagar@gmail.com', 'don@gmail.com'),
(3, 'khom@gamil.com', 'don@gmail.com'),
(5, 'khom@gmail.com', 'sagar@gmail.com'),
(6, 'sagar@gmail.com', 'khom@gmail.com'),
(7, 'rakesh@gmail.com', 'sagar@gmail.com'),
(8, 'sagar@gmail.com', 'rakesh@gmail.com'),
(9, 'rakesh@gmail.com', 'khom@gmail.com'),
(10, 'khom@gmail.com', 'rakesh@gmail.com'),
(11, 'dhiraj@gmail.com', 'salim.171329@ncit.edu.np'),
(12, 'salim.171329@ncit.edu.np', 'dhiraj@gmail.com'),
(13, 'ujwal@gmail.com', 'khom@gmail.com'),
(14, 'khom@gmail.com', 'ujwal@gmail.com'),
(15, 'ujwal@gmail.com', 'dhiraj@gmail.com'),
(16, 'dhiraj@gmail.com', 'ujwal@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `email_confirm_table`
--

CREATE TABLE `email_confirm_table` (
  `id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `email_confirm_table`
--

INSERT INTO `email_confirm_table` (`id`, `email`, `value`) VALUES
(12, 'khom@gmail.com', 1),
(14, 'sagar@gmail.com', 1),
(15, 'rakesh@gmail.com', 1),
(16, 'rita@gmail.com', 1),
(17, 'ujwal@gmail.com', 1),
(18, 'dhiraj@gmail.com', 1),
(22, 'salim.171329@ncit.edu.np', 1);

-- --------------------------------------------------------

--
-- Table structure for table `flat`
--

CREATE TABLE `flat` (
  `flat_id` int(11) NOT NULL,
  `flat_title` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `flat_district` varchar(30) NOT NULL,
  `upload_date` date NOT NULL,
  `upload_time` time NOT NULL,
  `price` int(11) NOT NULL,
  `area` text NOT NULL,
  `no_room` int(11) NOT NULL,
  `floor` varchar(20) NOT NULL,
  `parking_car` int(11) NOT NULL,
  `parking_bike` int(11) NOT NULL,
  `description` text NOT NULL,
  `img1_path` text NOT NULL,
  `img2_path` text DEFAULT NULL,
  `img3_path` text DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flat`
--

INSERT INTO `flat` (`flat_id`, `flat_title`, `address`, `flat_district`, `upload_date`, `upload_time`, `price`, `area`, `no_room`, `floor`, `parking_car`, `parking_bike`, `description`, `img1_path`, `img2_path`, `img3_path`, `user_id`) VALUES
(38, 'Flat for office', 'Tripureshwor', 'Kathmandu', '2022-09-12', '19:16:57', 10000, 'Behind kd tower', 3, '2', 1, 5, '-Internet available\r\n-generator available\r\n-security gaurd not availabe\r\n\r\ntwo washroom for 3 rooms.\r\n-washroom need to be made clean\r\n\r\n-loud noise noise is not tollerable\r\n-money should be paid within 15 days of month complete.\r\n\r\nfor additional details please contact us without any hesitation. ', 'static/img/flat/office.png', 'static/img/flat/office2.png', 'static/img/flat/office3.png', 26),
(40, 'Room for student', 'Kumaripai', 'Lalitpur', '2022-09-13', '18:45:39', 22, 'sfsdf', 22, '22', 22, 22, 'xc,mvlkd', 'static/img/flat/logo-search-grid-1x.png', NULL, NULL, 9),
(41, 'Room for Student', 'Sankhamul', 'Lalitpur', '2022-09-13', '18:53:07', 1200, 'Near to sankhamul futsal', 2, '3', 0, 1, '- water and electricity facility.\r\n-internet and tv connection not available. (incase of dishhome tenant should bring thier own setup box)\r\n-1 bathroom \r\n-rent amount should be deposited within 1 week.\r\n\r\n-noise not allowed.\r\n-cleaning is necessary.\r\n-party with loud music and alcohol is not allowed. (in such case tenant will have to leave flat).', 'static/img/flat/flat-a.png', 'static/img/flat/flat-a2.png', 'static/img/flat/flat-a3.png', 9),
(42, 'Flat for Rent', 'Lagankhel', 'Lalitpur', '2022-09-13', '19:03:58', 15000, 'Near lagankhel mini super market', 3, '2', 1, 3, '-dishhome anteena available.\r\n-sharing of internet available.\r\n-water supply twice a week.\r\n-family will be priotize.\r\n\r\n-garbage collection once a 5 days.\r\n-1 bathroom (should make clean)\r\n\r\nfor additional details please message in the chat option of the system.\r\nor contact to my number given.', 'static/img/flat/flat-b.png', 'static/img/flat/flat-b2.png', 'static/img/flat/flat-b3.png', 9),
(43, 'Flat with 3 room', 'Nakhu', 'Lalitpur', '2022-09-13', '19:11:38', 16000, 'Near Asmita cafe', 3, '3', 0, 2, '\r\n- 1 kitchen\r\n-2 bathroom\r\n-drinking water once a week.\r\n-well water 24 hrs available.\r\n\r\n-no internet.\r\n-no tv connection.\r\n\r\n-please send message in chat box for additional queries or call in the provided number.', 'static/img/flat/flat-a3.png', 'static/img/flat/flat-c.png', 'static/img/flat/flat-c2.png', 9),
(46, 'sf', 'sdf', 'fdsf', '2022-09-17', '11:20:18', 324, 'sdf', 234, '23', 324, 324, 'wafsadfsdf', 'static/img/flat/flat-b3.png', NULL, NULL, 24);

-- --------------------------------------------------------

--
-- Table structure for table `flat_map`
--

CREATE TABLE `flat_map` (
  `id` int(11) NOT NULL,
  `lattitude` double NOT NULL,
  `longitude` double NOT NULL,
  `flat_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flat_map`
--

INSERT INTO `flat_map` (`id`, `lattitude`, `longitude`, `flat_id`) VALUES
(5, 23.333, 23.333, 23),
(6, 37.22, 38.33, 28),
(7, 37.22, 38.33, 28),
(8, 27.672355, 85.341559, 29),
(10, 85.31, 27.05, 30),
(11, 27.674278, 85.425571, 31),
(12, 85.31631298523331, 27.705983058564954, 32),
(17, 27.717437935681886, 85.28339690963105, 34),
(18, 27.715842286692705, 85.289619641115, 35),
(19, 27.71113124453896, 85.29579945068622, 35),
(20, 27.71236654125545, 85.31780255376026, 28),
(21, 27.711359202875812, 85.31112022857849, 25),
(22, 27.694898583367177, 85.31368498309917, 38),
(23, 27.682112499664257, 85.33217053432622, 41),
(24, 27.666734732029667, 85.32368457683162, 42),
(25, 27.664441419654707, 85.30654681055461, 43);

-- --------------------------------------------------------

--
-- Table structure for table `hall`
--

CREATE TABLE `hall` (
  `hall_id` int(11) NOT NULL,
  `hall_name` text NOT NULL,
  `hall_address` varchar(50) NOT NULL,
  `hall_district` varchar(30) NOT NULL,
  `hall_price` int(11) NOT NULL,
  `contact_number` bigint(20) NOT NULL,
  `person_capacity` int(11) NOT NULL,
  `parking_2wheel` int(11) NOT NULL,
  `parking_4wheel` int(11) NOT NULL,
  `hall_description` text NOT NULL,
  `meeting_hall` varchar(20) NOT NULL,
  `conference_hall` varchar(20) NOT NULL,
  `party_palace` varchar(50) NOT NULL,
  `upload_date` date DEFAULT NULL,
  `upload_time` time DEFAULT NULL,
  `img1` text NOT NULL,
  `img2` text DEFAULT NULL,
  `img3` text DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `property_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hall`
--

INSERT INTO `hall` (`hall_id`, `hall_name`, `hall_address`, `hall_district`, `hall_price`, `contact_number`, `person_capacity`, `parking_2wheel`, `parking_4wheel`, `hall_description`, `meeting_hall`, `conference_hall`, `party_palace`, `upload_date`, `upload_time`, `img1`, `img2`, `img3`, `user_id`, `property_type`) VALUES
(29, 'Crystal Banquet', 'Manbhawan', 'Lalitpur', 11000, 9851029382, 1200, 750, 50, 'Per Plate System\r\nStarting price Rs.1650 each for 300 people\r\nStarting price Rs.1600 each for 500 people\r\nStarting price Rs.1800 each for 200 people\r\n', 'No', 'No', 'Party Palace', '2022-09-11', '11:54:55', 'static/img/hall/crystal_banquet.png', 'static/img/hall/crystal_banquet2.png', 'static/img/hall/crystal_banquet3.png', 13, 'hall'),
(30, 'Balaji banquet', 'Koteshwor', 'Kathmandu', 2000, 9845562312, 800, 200, 15, '\r\nBalaji Banquet has provided the venue and fine catering services for all types of events including weddings, anniversaries, holiday parties, conferences, seminars and meetings. Our staff, with their many years of experience, will create an event your guests will long remember. \r\n\r\nfood:\r\n-customer can make adjustment in choices of food and price will be according to that.\r\n-dj service\r\n-DJ charge RS. 15,000. DJ will be closed at sharp 9 PM.\r\n-decoration service\r\n-Full payment is required before the day of function.\r\n', 'No', 'No', 'Party Palace', '2022-09-12', '18:50:39', 'static/img/hall/balaji_banquet.png', 'static/img/hall/balaji_banquet2.png', 'static/img/hall/balaji_banquet3.png', 26, 'hall'),
(31, 'Lotus Party Palace', 'Mahadevsthan', 'Koteshwor', 3000, 9841799634, 800, 70, 10, 'If you are looking for the best venue to celebrate an auspicious day, party or any kind of functions and ceremony in this town then we are the best ultimate solution for you. We provide the hygienic and delicious food in a welcoming environment.\r\n\r\n We provide the spacious hall to the guest. There is huge space for parking your vehicles. Moreover, we are dedicated to fulfill our customers’ satisfaction which leads to great hospitality and management.\r\n\r\nLotus Party Place is a well known party place in Kathmandu which is located in Mahadevsthan, Koteshwor. We offer solutions for functions, such as weddings, receptions, events, celebrations, conventions, exhibitions and conferences, etc.\r\n\r\n\r\nfor additional details please send message or call or email us.', 'No', 'Conference Hall', 'Party Palace', '2022-09-13', '19:22:19', 'static/img/hall/lotus_party_palace.png', 'static/img/hall/lotus_party_palace2.png', 'static/img/hall/lotus_party_palace3.png', 9, 'hall'),
(33, 'sff', 'sdfsdfsd', 'fsdfs', 3, 5345634, 324, 324, 234, 'sdfsdfsd', 'No', 'Conference Hall', 'No', '2022-09-17', '11:08:53', 'static/img/hall/flat-c.png', NULL, NULL, 24, 'hall'),
(34, 'sff', 'sdfsdfsd', 'fsdfs', 3, 5345634, 324, 324, 234, 'sdfsdfsd', 'No', 'Conference Hall', 'No', '2022-09-17', '11:09:54', 'static/img/hall/flat-c.png', NULL, NULL, 24, 'hall'),
(35, 'sff', 'sdfsdfsd', 'fsdfs', 3, 5345634, 324, 324, 234, 'sdfsdfsd', 'No', 'Conference Hall', 'No', '2022-09-17', '11:10:54', 'static/img/hall/flat-c.png', NULL, NULL, 24, 'hall'),
(36, 'sff', 'sdfsdfsd', 'fsdfs', 3, 5345634, 324, 324, 234, 'sdfsdfsd', 'No', 'Conference Hall', 'No', '2022-09-17', '11:11:33', 'static/img/hall/flat-c.png', NULL, NULL, 24, 'hall');

-- --------------------------------------------------------

--
-- Table structure for table `hall_image_db`
--

CREATE TABLE `hall_image_db` (
  `hall_img_id` int(11) NOT NULL,
  `image_path` text NOT NULL,
  `hall_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `hall_map`
--

CREATE TABLE `hall_map` (
  `id` int(11) NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `hall_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hall_map`
--

INSERT INTO `hall_map` (`id`, `latitude`, `longitude`, `hall_id`) VALUES
(1, 27.712460994790703, 85.30815906982644, 28),
(2, 27.679185600449003, 85.34701766032828, 30),
(3, 27.679891428605075, 85.34775615467424, 30),
(4, 27.679630447612098, 85.34716908491822, 30),
(5, 27.680904223607925, 85.34201108810709, 31);

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `Id` int(11) NOT NULL,
  `sender` varchar(100) NOT NULL,
  `msg` varchar(100) NOT NULL,
  `reciver` varchar(100) NOT NULL,
  `dateTime` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`Id`, `sender`, `msg`, `reciver`, `dateTime`) VALUES
(1, 'salim.171329@ncit.edu.np', 'helo dhiraj can i rent it one day before', 'dhiraj@gmail.com', '13.09.22 11:40'),
(2, 'dhiraj@gmail.com', 'huncha', 'salim.171329@ncit.edu.np', '13.09.22 11:49'),
(3, 'salim.171329@ncit.edu.np', 'la teso bhaye ma book gardinchu hae', 'dhiraj@gmail.com', '13.09.22 11:49'),
(4, 'dhiraj@gmail.com', 'ok', 'salim.171329@ncit.edu.np', '13.09.22 11:50'),
(5, 'salim.171329@ncit.edu.np', 'book gareko paisa chai', 'dhiraj@gmail.com', '13.09.22 11:50'),
(6, 'salim.171329@ncit.edu.np', 'firta', 'dhiraj@gmail.com', '13.09.22 11:50'),
(7, 'salim.171329@ncit.edu.np', 'aucha', 'dhiraj@gmail.com', '13.09.22 11:50'),
(8, 'dhiraj@gmail.com', 'certain % cut huncha', 'salim.171329@ncit.edu.np', '13.09.22 11:50'),
(9, 'salim.171329@ncit.edu.np', 'ksljflsk', 'dhiraj@gmail.com', '13.09.22 14:14'),
(10, 'ujwal@gmail.com', 'heloo', 'dhiraj@gmail.com', '16.09.22 12:48');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `email` text NOT NULL,
  `address` varchar(50) NOT NULL,
  `district` varchar(20) NOT NULL,
  `phone_number` bigint(20) NOT NULL,
  `password` text NOT NULL,
  `image_path` text DEFAULT NULL,
  `created_on` date NOT NULL,
  `created_on_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `address`, `district`, `phone_number`, `password`, `image_path`, `created_on`, `created_on_time`) VALUES
(1, 'admin', 'user', 'admin@gmail.com', 'balkumari', 'ktm', 9878787654, 'admin', '', '0000-00-00', '00:00:00'),
(6, 'rakesh', 'thapa', 'rakesh@gmail.com', 'kumaripati', 'lalitpur', 984123456, 'pbkdf2:sha256:260000$Cp80QjzXg6Ck8mZZ$aabced4c3453493d5cb27b8260a2613ecac549321a57af3036c0ee8bf24d7e10', 'static/img/profile/eric-michael-KA9W4k0pOn4-unsplash_1.jpg', '2022-08-10', '18:04:00'),
(8, 'Hari', 'Khadka', 'hari123@gmail.com', 'Koteshower', 'kathmandu', 984123456, 'pbkdf2:sha256:260000$dwZ9irWzApgSyQYg$fa0613673431aa264c8f1dbf6fe189af62d5a3c14627450a16a900eef51fc9d8', NULL, '2022-08-07', '21:00:00'),
(9, 'rita', 'thapa', 'rita@gmail.com', 'kalanki', 'kathmandu', 984123456, 'pbkdf2:sha256:260000$b4twzFCFHc29pEW9$f541d83405ba61b50502e2b993ec0d069454f62b014387441a61174175c3d1f5', NULL, '2022-08-29', '12:09:00'),
(12, 'kiran', 'magar', 'kiran@gmail.com', 'jamal', 'kathmandu', 984123456, 'pbkdf2:sha256:260000$N84VuWGCZSNZLMwX$48d6bcbcca35138c627a28893d134db67269f039d0b661511d0f49bce3bf5f88', NULL, '2022-09-08', '17:00:00'),
(13, 'sagar', 'kc', 'sagar@gmail.com', 'gwarko', 'gwarko', 984123456, 'pbkdf2:sha256:260000$PGInavfArZFXJrDh$d0df0e92b5b35a89d53b47e5ead2b005bb8b9ddfec38f0237e3f64912464f6a1', NULL, '2022-09-02', '14:15:00'),
(16, 'khom', 'thapa', 'khom@gmail.com', 'balkumari', 'lalitpur', 9822123456, 'pbkdf2:sha256:260000$Rh6YSD3aZHN427Nc$7451580ce6a2cc162073556d777209f08d7cf84ae518b16dd3f037d97fc157e7', 'static/img/profile/user4.jpg', '2022-07-08', '10:15:00'),
(17, 'narendra', 'chand', 'narendra@gmail.com', 'koteshwor', 'kathmandu', 9841253614, 'pbkdf2:sha256:260000$xmI2uXTWOudEUC2b$0628f1c7b5854e20dea7d5e8ca36070e1ae371623d01620e8f38725b5a869234', NULL, '2022-08-10', '10:29:00'),
(24, 'ujwal', 'rai', 'ujwal@gmail.com', 'balkumari', 'balkumari', 9841789456, 'pbkdf2:sha256:260000$WWukUsLpIymXITAz$d6d3bd87e89a556fc70e82726b9550ba83310f7ab26b2751104d402fa9dd418d', NULL, '2022-08-25', '07:44:00'),
(25, 'sushant', 'luitel', 'sushant@gmail.com', 'thimi', 'bhaktapur', 9865231458, 'pbkdf2:sha256:260000$svF7JPN5ISQf7SIr$a905ad66f8a9d9f088576bac8b903f9fcdefdafd7f5a57df249144f2029d6a20', NULL, '2022-09-01', '09:04:00'),
(26, 'dhiraj', 'chaudary', 'dhiraj@gmail.com', 'yatayat', 'yatayat', 9845123654, 'pbkdf2:sha256:260000$s2hxukOHsZP8WJw6$d28c246eb5d9342f189587b57c3015c82fb74a2429e8522ecf7a26ed351be2fd', NULL, '2022-09-06', '11:55:22'),
(27, 'bijay', 'chand', 'bijay@gmail.com', 'kritipur', 'kathmandu', 9841123789, 'pbkdf2:sha256:260000$86PGNKGPBgz92i5w$042920b82e24f9042f87eb7e946d1793ef13a1cc97b5a671c3eea6b2b0fc7f11', NULL, '2022-09-06', '11:57:13'),
(45, 'salim', 'Maharjan', 'salim.171329@ncit.edu.np', 'dhobighat', 'lalitpur', 9860996421, 'pbkdf2:sha256:260000$UXNlkX4fHkWjNPDg$381066abaa9734326c56a56a491d45378701c393db2f50d19ab1293bce5d735c', NULL, '2022-09-13', '15:07:13');

-- --------------------------------------------------------

--
-- Table structure for table `v`
--

CREATE TABLE `v` (
  `id` int(11) NOT NULL,
  `value` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `v`
--

INSERT INTO `v` (`id`, `value`) VALUES
(0, 'vehicle');

-- --------------------------------------------------------

--
-- Table structure for table `vechile`
--

CREATE TABLE `vechile` (
  `id` int(11) NOT NULL,
  `vehicle_number` text NOT NULL,
  `Location` text NOT NULL,
  `district` varchar(20) NOT NULL,
  `vehicle_company` text NOT NULL,
  `vehicle_model` text NOT NULL,
  `vehicle_color` text NOT NULL,
  `vehicle_engine` varchar(10) NOT NULL,
  `vehicle_mileage` varchar(10) NOT NULL,
  `vehicle_personCapacity` int(11) NOT NULL,
  `vehicle_price` int(11) NOT NULL,
  `vehicle_category` varchar(50) NOT NULL,
  `fuel_type` varchar(10) NOT NULL,
  `description` text NOT NULL,
  `upload_date` date NOT NULL,
  `upload_time` time NOT NULL,
  `img1` text NOT NULL,
  `img2` text DEFAULT NULL,
  `img3` text DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `property_type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vechile`
--

INSERT INTO `vechile` (`id`, `vehicle_number`, `Location`, `district`, `vehicle_company`, `vehicle_model`, `vehicle_color`, `vehicle_engine`, `vehicle_mileage`, `vehicle_personCapacity`, `vehicle_price`, `vehicle_category`, `fuel_type`, `description`, `upload_date`, `upload_time`, `img1`, `img2`, `img3`, `user_id`, `property_type`) VALUES
(37, '2242', 'Balkumari', 'Lalitpur', 'Honda', '2008', 'gray', '3000', '35', 5, 2000, 'Car', 'Disel', 'features \r\n-air conditioner\r\n-air bags\r\n-anti braking system\r\n-power window\r\n-tubeless Tyre\r\n-fog light\r\n', '2022-09-12', '18:10:34', 'static/img/vehicle/honda.png', 'static/img/vehicle/honda2.png', 'static/img/vehicle/honda3.png', 26, 'vehicle'),
(39, '2264', 'Kalimati', 'Kathmandu', 'Toyata', 'Toyata fortuner', 'brown', '3000', '35', 5, 2500, 'Suv', 'Disel', '\r\nfeatures \r\n-air conditioner\r\n-air bags\r\n-anit breaking system\r\n-power window\r\n-tubeless tyre\r\n-fog light\r\n-power steering\r\n-leather seat\r\n-alloy wheel\r\n-back camera\r\ncustomer themselves need to pick vehicle in the given address.\r\nfor additional queries please contact or message through the system.', '2022-09-12', '18:18:51', 'static/img/vehicle/toyata.png', 'static/img/vehicle/toyata1.png', 'static/img/vehicle/toyata2.png', 26, 'vehicle'),
(40, '23fdgdf', 'dfgd', 'kjhk', 'kjhkj', 'jkhk', '5', '4', '54', 22, 400, 'Car', 'Disel', 'lkjdlfkjslkdfjls', '2022-09-16', '13:30:44', 'static/img/vehicle/flat-b3.png', 'static/img/vehicle/flat-c.png', 'static/img/vehicle/flat-c2.png', 24, 'vehicle'),
(41, '32r', 'fsf', 'ewf', 'sdf', 'sdf', '23dssd', '24', '324', 324, 324, 'Car', 'Disel', 'sdfsad', '2022-09-17', '11:11:55', 'static/img/vehicle/flat-c.png', NULL, NULL, 24, 'vehicle');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_map`
--

CREATE TABLE `vehicle_map` (
  `id` int(11) NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `vehicle_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_map`
--

INSERT INTO `vehicle_map` (`id`, `latitude`, `longitude`, `vehicle_id`) VALUES
(5, 27.715158438360504, 85.33987350921848, 36),
(6, 27.70547012636011, 85.3372556732204, 35),
(7, 27.671579044584675, 85.33948075958818, 37),
(8, 27.699547579350252, 85.30089752330912, 39),
(9, 27.700834629660136, 85.32000370483576, 40);

-- --------------------------------------------------------

--
-- Table structure for table `whishlist_flat`
--

CREATE TABLE `whishlist_flat` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `whishlist_hall`
--

CREATE TABLE `whishlist_hall` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `whishlist_vehicle`
--

CREATE TABLE `whishlist_vehicle` (
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `wishlist_flat`
--

CREATE TABLE `wishlist_flat` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `flat_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `wishlist_hall`
--

CREATE TABLE `wishlist_hall` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `hall_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `wishlist_vehicle`
--

CREATE TABLE `wishlist_vehicle` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `vehicle_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wishlist_vehicle`
--

INSERT INTO `wishlist_vehicle` (`id`, `user_id`, `vehicle_id`) VALUES
(10, 24, 39);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booked_hall_table`
--
ALTER TABLE `booked_hall_table`
  ADD PRIMARY KEY (`booked_id`);

--
-- Indexes for table `booked_vehicle_table`
--
ALTER TABLE `booked_vehicle_table`
  ADD PRIMARY KEY (`booked_id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `email_confirm_table`
--
ALTER TABLE `email_confirm_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `flat`
--
ALTER TABLE `flat`
  ADD PRIMARY KEY (`flat_id`);

--
-- Indexes for table `flat_map`
--
ALTER TABLE `flat_map`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hall`
--
ALTER TABLE `hall`
  ADD PRIMARY KEY (`hall_id`);

--
-- Indexes for table `hall_image_db`
--
ALTER TABLE `hall_image_db`
  ADD PRIMARY KEY (`hall_img_id`);

--
-- Indexes for table `hall_map`
--
ALTER TABLE `hall_map`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `vechile`
--
ALTER TABLE `vechile`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicle_map`
--
ALTER TABLE `vehicle_map`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `whishlist_flat`
--
ALTER TABLE `whishlist_flat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `whishlist_hall`
--
ALTER TABLE `whishlist_hall`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `whishlist_vehicle`
--
ALTER TABLE `whishlist_vehicle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wishlist_flat`
--
ALTER TABLE `wishlist_flat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wishlist_hall`
--
ALTER TABLE `wishlist_hall`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wishlist_vehicle`
--
ALTER TABLE `wishlist_vehicle`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booked_hall_table`
--
ALTER TABLE `booked_hall_table`
  MODIFY `booked_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `booked_vehicle_table`
--
ALTER TABLE `booked_vehicle_table`
  MODIFY `booked_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `email_confirm_table`
--
ALTER TABLE `email_confirm_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `flat`
--
ALTER TABLE `flat`
  MODIFY `flat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `flat_map`
--
ALTER TABLE `flat_map`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `hall`
--
ALTER TABLE `hall`
  MODIFY `hall_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `hall_image_db`
--
ALTER TABLE `hall_image_db`
  MODIFY `hall_img_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hall_map`
--
ALTER TABLE `hall_map`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `vechile`
--
ALTER TABLE `vechile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `vehicle_map`
--
ALTER TABLE `vehicle_map`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `whishlist_flat`
--
ALTER TABLE `whishlist_flat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `whishlist_hall`
--
ALTER TABLE `whishlist_hall`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `whishlist_vehicle`
--
ALTER TABLE `whishlist_vehicle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `wishlist_flat`
--
ALTER TABLE `wishlist_flat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `wishlist_hall`
--
ALTER TABLE `wishlist_hall`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `wishlist_vehicle`
--
ALTER TABLE `wishlist_vehicle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
