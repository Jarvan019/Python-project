-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 10, 2023 at 06:57 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pos_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Ref` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Mother` varchar(255) NOT NULL,
  `Gender` varchar(255) NOT NULL,
  `PostCode` varchar(255) NOT NULL,
  `Mobile` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Nationality` varchar(255) NOT NULL,
  `Idproof` varchar(255) NOT NULL,
  `Idnumber` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Ref`, `Name`, `Mother`, `Gender`, `PostCode`, `Mobile`, `Email`, `Nationality`, `Idproof`, `Idnumber`, `address`) VALUES
(2569, '1', '1', 'Male', '1', '1', '1', 'American', 'Driver\'s License', '1', '1'),
(3880, 'raj', '123', 'Male', '123', '123', '123', 'Filipino', 'Student Id', '123', '123'),
(7788, '0', '1', 'Male', '2', '3', '4', 'American', 'Driver\'s License', '5', '6'),
(9038, 'Jarvan', 'marilou', 'Male', '1101', '26', 'Rajbrusola@gmail.com', 'Filipino', 'Student Id', '123', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`Ref`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
