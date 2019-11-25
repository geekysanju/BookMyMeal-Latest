-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 31, 2019 at 12:11 PM
-- Server version: 5.7.27-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mypython23`
--

-- --------------------------------------------------------

--
-- Table structure for table `addcat`
--

CREATE TABLE `addcat` (
  `catid` int(11) NOT NULL,
  `catnm` varchar(20) NOT NULL,
  `caticonnm` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addcat`
--

INSERT INTO `addcat` (`catid`, `catnm`, `caticonnm`) VALUES
(1, 'Indian', 'indianfood.png'),
(2, 'Chinese', 'chinese.jpeg'),
(3, 'Italian', 'italianfood.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `addsubcat`
--

CREATE TABLE `addsubcat` (
  `subcatid` int(11) NOT NULL,
  `subcatnm` varchar(50) NOT NULL,
  `catnm` varchar(50) NOT NULL,
  `subcaticonnm` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addsubcat`
--

INSERT INTO `addsubcat` (`subcatid`, `subcatnm`, `catnm`, `subcaticonnm`) VALUES
(1, 'Rajasthani', 'Indian', 'logo1.jpeg'),
(2, 'SouthIndian', 'Indian', 'img13.jpeg'),
(3, 'Dish1', 'Chinese', 'img12.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `foodproduct`
--

CREATE TABLE `foodproduct` (
  `pid` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `subcatnm` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `picon` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `foodproduct`
--

INSERT INTO `foodproduct` (`pid`, `title`, `subcatnm`, `description`, `price`, `picon`) VALUES
(1, 'Rajasthani dish 1', 'Rajasthani', 'good quality food', 100, 'logo1_tJjtnMq.jpeg'),
(2, 'Rajasthani dish 2', 'Rajasthani', 'good quality food at affordable price', 120, 'img14.jpeg'),
(3, 'south Indian dish', 'SouthIndian', 'good quality food and large quantity', 100, 'demo.png');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `txnid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `uid` varchar(100) NOT NULL,
  `dt` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`txnid`, `pid`, `price`, `uid`, `dt`) VALUES
(1, 1, 100, 'adawadkarvilekh@gmail.com', 'Tue Jul 30 11:20:59 2019'),
(2, 3, 100, 'adawadkarvilekh@gmail.com', 'Tue Jul 30 11:25:27 2019'),
(3, 2, 120, 'phpbatch34@gmail.com', 'Tue Jul 30 11:45:27 2019');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `regid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(10) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `city` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `role` varchar(10) NOT NULL,
  `status` int(11) NOT NULL,
  `dt` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`regid`, `name`, `email`, `password`, `address`, `mobile`, `city`, `gender`, `role`, `status`, `dt`) VALUES
(1, 'vilekh', 'adawadkarvilekh@gmail.com', '123', 'indore mp', '11111111111', 'Indore', 'male', 'user', 1, 'Mon Jul 22 10:38:15 2019'),
(2, 'Admin', 'admin@gmail.com', '123', 'check', '11111111111', 'Bhopal', 'female', 'admin', 1, 'Mon Jul 22 10:38:46 2019'),
(3, 'phpbatch', 'phpbatch34@gmail.com', '12345', 'indore mp', '11111111111', 'Indore', 'male', 'user', 1, 'Tue Jul 23 11:46:15 2019');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addcat`
--
ALTER TABLE `addcat`
  ADD PRIMARY KEY (`catid`),
  ADD UNIQUE KEY `catnm` (`catnm`);

--
-- Indexes for table `addsubcat`
--
ALTER TABLE `addsubcat`
  ADD PRIMARY KEY (`subcatid`),
  ADD UNIQUE KEY `subcatnm` (`subcatnm`);

--
-- Indexes for table `foodproduct`
--
ALTER TABLE `foodproduct`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`txnid`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`regid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addcat`
--
ALTER TABLE `addcat`
  MODIFY `catid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `addsubcat`
--
ALTER TABLE `addsubcat`
  MODIFY `subcatid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `foodproduct`
--
ALTER TABLE `foodproduct`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `txnid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `regid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
