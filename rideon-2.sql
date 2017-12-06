-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 12, 2017 at 04:25 AM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rideon`
--

-- --------------------------------------------------------

--
-- Table structure for table `contactus`
--

CREATE TABLE `contactus` (
  `id` int(11) NOT NULL,
  `fb_id` varchar(100) DEFAULT NULL,
  `type` varchar(11) DEFAULT NULL,
  `message` text,
  `attachment_url` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contactus`
--

INSERT INTO `contactus` (`id`, `fb_id`, `type`, `message`, `attachment_url`) VALUES
(1, '1474590815942063', 'Complaint', 'fb pic is zoomed in references', 'images/cropped-2091503309.jpg'),
(2, '1890801504270129', 'Query', 'i am unable to see any rides', NULL),
(3, '1709082829164167', 'Feedback', 'please add available rides list (List of rides offered) , so that people can select required ride ', NULL),
(4, '10214006313334842', 'Feedback', 'Hello', NULL),
(5, '10214006313334842', 'Query', 'Hello', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `ratings`
--

CREATE TABLE `ratings` (
  `id` int(11) NOT NULL,
  `rate` varchar(100) DEFAULT NULL,
  `fb_id` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ratings`
--

INSERT INTO `ratings` (`id`, `rate`, `fb_id`) VALUES
(40, '3.5', '10154789249431712'),
(41, '5.0', '10213593713652734'),
(42, '5.0', '10213593713652734'),
(43, '1.0', '1089140217883713'),
(44, '5.0', '10155629413203080'),
(45, '5.0', '1890801504270129'),
(46, '5.0', '1890801504270129'),
(47, '5.0', '1161403207294108'),
(48, '5.0', '1161403207294108'),
(49, '5.0', '1264452186999740'),
(50, '5.0', '1880524541975066'),
(51, '5.0', '1880524541975066'),
(52, '5.0', '1089140217883713'),
(53, '5.0', '1709082829164167');

-- --------------------------------------------------------

--
-- Table structure for table `rides`
--

CREATE TABLE `rides` (
  `id` int(11) NOT NULL,
  `fb_id` varchar(100) DEFAULT NULL,
  `car_model` varchar(100) DEFAULT NULL,
  `seats` varchar(100) DEFAULT NULL,
  `seats_available` int(11) NOT NULL DEFAULT '0',
  `cost` varchar(10) DEFAULT NULL,
  `source` varchar(100) DEFAULT NULL,
  `source_latitude` varchar(100) DEFAULT NULL,
  `source_longitude` varchar(100) DEFAULT NULL,
  `destination` varchar(100) DEFAULT NULL,
  `destination_latitude` varchar(100) DEFAULT NULL,
  `destination_longitude` varchar(100) DEFAULT NULL,
  `dateofride` varchar(20) DEFAULT NULL,
  `start_time` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `message` text,
  `rideCancelStatus` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rides`
--

INSERT INTO `rides` (`id`, `fb_id`, `car_model`, `seats`, `seats_available`, `cost`, `source`, `source_latitude`, `source_longitude`, `destination`, `destination_latitude`, `destination_longitude`, `dateofride`, `start_time`, `created_at`, `message`, `rideCancelStatus`) VALUES
(243, '1089140217883713', 'honda', '2', 0, '150', 'Anantapur', '14.6818877', '77.6005911', 'Kadiri', '14.1130272', '78.1605586', '2017-09-29', '2017-09-29 23:48:00', '2017-09-30 03:15:21', 'join my ride!!!!!!!', 0),
(244, '1089140217883713', 'beat', '1', 1, '9000', 'Anantapur', '14.6818877', '77.6005911', 'Wayanad', '11.6287048', '76.0812507', '2017-09-29', '2017-09-29 21:18:00', '2017-09-30 03:20:05', 'coool breezy waynad ......any one join with me', 0),
(245, '10214006313334842', 'bull', '2', 0, '300', 'Jayanagar', '12.925007', '77.593803', 'BTM Layout', '12.916576', '77.610116', '2017-11-05', '2017-11-05 22:45:36', '2017-10-30 15:16:29', 'Hello', 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(11) NOT NULL,
  `fb_id` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `ref_number` varchar(100) DEFAULT NULL,
  `ref_status` varchar(100) NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `api_key` varchar(32) DEFAULT NULL,
  `fcm_id` varchar(1000) DEFAULT NULL,
  `company` varchar(100) NOT NULL DEFAULT 'NULL',
  `aadhar` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `fb_id`, `name`, `email`, `mobile`, `gender`, `dob`, `ref_number`, `ref_status`, `created_at`, `api_key`, `fcm_id`, `company`, `aadhar`) VALUES
(128, '1887614827922173', 'Ram Daruru', 'Ram Daruru', '9663800688', 'male', '29', '', '0', '2017-09-30 05:15:27', 'e4fcba76401befbfe5ee205d5be36e1d', 'eShlVde79rI:APA91bG5tCNLWx8-thkPwaxuI6egnW-yOeJq6_avEMVUmco0qnWXEmFpiCDCtK9xBUOX9oPR_c9RQn661msGJ9NNct0MN9c7zyLipaaEbO-qPGONRK96YJ25Ti5s4QTvZbZMdhGXSbFN', 'Ciber', NULL),
(131, '1593746680695301', 'Smitha Rammurthy', 'smitharammurthy@gmail.com', '98', 'female', '25', NULL, '0', '2017-11-05 03:10:17', '90a7e21bde84bd55ed0c0a5631069109', NULL, 'Kelli', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user_rides`
--

CREATE TABLE `user_rides` (
  `id` int(11) NOT NULL,
  `fb_id` varchar(100) DEFAULT NULL,
  `task_id` varchar(100) DEFAULT NULL,
  `status` enum('0','1','2') DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `message` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_rides`
--

INSERT INTO `user_rides` (`id`, `fb_id`, `task_id`, `status`, `created_at`, `message`) VALUES
(235, '1089140217883713', '244', '1', '2017-09-30 03:21:47', ''),
(236, '1474590815942063', '248', '1', '2017-09-30 15:17:22', 'i would like to join'),
(237, '10214006313334842', '294', '0', '2017-11-04 18:25:51', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contactus`
--
ALTER TABLE `contactus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ratings`
--
ALTER TABLE `ratings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rides`
--
ALTER TABLE `rides`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `user_rides`
--
ALTER TABLE `user_rides`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contactus`
--
ALTER TABLE `contactus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `ratings`
--
ALTER TABLE `ratings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
--
-- AUTO_INCREMENT for table `rides`
--
ALTER TABLE `rides`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=297;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=276;
--
-- AUTO_INCREMENT for table `user_rides`
--
ALTER TABLE `user_rides`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=252;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
