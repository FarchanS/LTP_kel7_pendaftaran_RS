-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 29, 2021 at 01:57 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ltp_final_project1_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `dokter`
--

CREATE TABLE `dokter` (
  `IdDokter` varchar(20) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `BidangKedokteran` varchar(20) NOT NULL,
  `JadwalHari1` tinyint(1) NOT NULL,
  `Jam1Mulai` varchar(10) NOT NULL,
  `Jam1Berakhir` varchar(10) NOT NULL,
  `JadwalHari2` tinyint(1) NOT NULL,
  `Jam2Mulai` varchar(10) NOT NULL,
  `Jam2Berakhir` varchar(10) NOT NULL,
  `JadwalHari3` tinyint(1) NOT NULL,
  `Jam3Mulai` varchar(10) NOT NULL,
  `Jam3Berakhir` varchar(10) NOT NULL,
  `JadwalHari4` tinyint(1) NOT NULL,
  `Jam4Mulai` varchar(10) NOT NULL,
  `Jam4Berakhir` varchar(10) NOT NULL,
  `JadwalHari5` tinyint(1) NOT NULL,
  `Jam5Mulai` varchar(10) NOT NULL,
  `Jam5Berakhir` varchar(10) NOT NULL,
  `JadwalHari6` tinyint(1) NOT NULL,
  `Jam6Mulai` varchar(10) NOT NULL,
  `Jam6Berakhir` varchar(10) NOT NULL,
  `JadwalHari7` tinyint(1) NOT NULL,
  `Jam7Mulai` varchar(10) NOT NULL,
  `Jam7Berakhir` varchar(10) NOT NULL,
  `Kapasitas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dokter`
--

INSERT INTO `dokter` (`IdDokter`, `Nama`, `phone`, `BidangKedokteran`, `JadwalHari1`, `Jam1Mulai`, `Jam1Berakhir`, `JadwalHari2`, `Jam2Mulai`, `Jam2Berakhir`, `JadwalHari3`, `Jam3Mulai`, `Jam3Berakhir`, `JadwalHari4`, `Jam4Mulai`, `Jam4Berakhir`, `JadwalHari5`, `Jam5Mulai`, `Jam5Berakhir`, `JadwalHari6`, `Jam6Mulai`, `Jam6Berakhir`, `JadwalHari7`, `Jam7Mulai`, `Jam7Berakhir`, `Kapasitas`) VALUES
('1', 'rita', '083446787765', 'Kandungan', 1, '10:00:00', '12:00:00', 1, '10:30:00', '12:30:00', 1, '08:00:00', '11:00:00', 1, '09:00:00', '10:00:00', 1, '08:30:00', '11:30:00', 0, '00:00:00', '00:00:00', 0, '00:00:00', '00:00:00', 4),
('2', 'Irfan', '0833983983', 'Penyakit Dalam', 1, '16:00:00', '18:00:00', 0, '00:00:00', '00:00:00', 1, '16:00:00', '18:00:00', 0, '00:00:00', '00:00:00', 1, '16:00:00', '18:00:00', 0, '00:00:00', '00:00:00', 0, '00:00:00', '00:00:00', 4),
('3', 'Ida', '082905328328', 'Dokter Umum', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 0, '08:00:00', '17:00:00', 5),
('4', 'Anas', '08394759284', 'Dokter Umum', 0, '00:00:00', '00:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 5),
('5', 'Wawan', '08523572938', 'Anak', 1, '08:00:00', '15:00:00', 1, '08:00:00', '15:00:00', 1, '08:00:00', '15:00:00', 1, '08:00:00', '15:00:00', 1, '08:00:00', '15:00:00', 0, '00:00:00', '00:00:00', 0, '00:00:00', '00:00:00', 6),
('6', 'Ari', '08428493849', 'Bedah', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 1, '08:00:00', '17:00:00', 0, '00:00:00', '00:00:00', 0, '00:00:00', '00:00:00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `kedatangan`
--

CREATE TABLE `kedatangan` (
  `No` int(11) NOT NULL,
  `KTP` int(15) NOT NULL,
  `IdDokter` varchar(20) NOT NULL,
  `BidangKedokteran` varchar(50) NOT NULL,
  `DatangTgl` date NOT NULL,
  `DatangJam` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kedatangan`
--

INSERT INTO `kedatangan` (`No`, `KTP`, `IdDokter`, `BidangKedokteran`, `DatangTgl`, `DatangJam`) VALUES
(1, 2, '1', 'Kandungan', '2021-12-29', '10:30:00'),
(2, 2, '2', 'Penyakit Dalam', '2021-12-31', '17:00:00'),
(3, 1, '2', 'Penyakit Dalam', '2021-12-25', '19:00:00'),
(4, 2, '2', 'Penyakit Dalam', '2021-12-25', '19:30:00'),
(5, 2, '2', 'Penyakit Dalam', '2021-12-25', '19:45:00'),
(6, 1, '1', 'Kandungan', '2021-12-25', '17:00:00'),
(7, 1, '1', 'Kandungan', '2021-12-25', '17:00:00'),
(8, 1, '1', 'Kandungan', '2021-12-25', '17:00:00'),
(9, 1, '2', 'Penyakit Dalam', '2021-12-25', '17:00:00'),
(10, 2, '1', 'Kandungan', '2021-12-25', '11:20:00'),
(11, 1, '3', 'Dokter Umum', '2021-12-30', '10:00:00'),
(12, 1, '1', 'Kandungan', '2021-12-30', '10:30:00'),
(13, 1, '5', 'Anak', '2021-12-30', '10:30:00'),
(14, 1, '2', 'Penyakit Dalam', '2021-12-30', '10:30:00'),
(15, 1, '6', 'Bedah', '2021-12-30', '10:30:00'),
(16, 1, '1', 'Kandungan', '2021-12-30', '10:30:00'),
(17, 2, '5', 'Anak', '2021-12-30', '10:30:00'),
(18, 2, '1', 'Kandungan', '2021-12-30', '10:30:00'),
(19, 2, '1', 'Kandungan', '2021-12-30', '10:30:00'),
(20, 2, '1', 'Kandungan', '2021-12-30', '10:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `pasien`
--

CREATE TABLE `pasien` (
  `KTP` int(15) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Alamat` text NOT NULL,
  `TempatLahir` varchar(50) NOT NULL,
  `TanggalLahir` date NOT NULL,
  `Kelamin` varchar(10) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pasien`
--

INSERT INTO `pasien` (`KTP`, `Nama`, `Alamat`, `TempatLahir`, `TanggalLahir`, `Kelamin`, `Phone`, `Status`) VALUES
(1, 'hanz', 'depok	', 'sidoarjo', '2000-06-17', 'pria', '0818828829', 'Kawin'),
(2, 'Rita', 'Indonesia', 'Indonesia', '1999-04-28', 'wanita', '081329723412', 'Kawin'),
(3, 'Royan Habibie', 'Tangerang', 'Tangerang', '1990-05-17', 'pria', '089624471952', 'Kawin');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `IdUser` int(11) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`IdUser`, `Nama`, `Password`, `Role`) VALUES
(1, 'hanz', '0cc175b9c0f1b6a831c399e269772661', 'Admin'),
(2, 'hanz2', '7694f4a66316e53c8cdd9d9954bd611d', 'Admin'),
(3, 'rita', '202cb962ac59075b964b07152d234b70', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dokter`
--
ALTER TABLE `dokter`
  ADD PRIMARY KEY (`IdDokter`),
  ADD KEY `IdDokter` (`IdDokter`);

--
-- Indexes for table `kedatangan`
--
ALTER TABLE `kedatangan`
  ADD PRIMARY KEY (`No`),
  ADD KEY `IdDokter` (`IdDokter`),
  ADD KEY `KTP` (`KTP`);

--
-- Indexes for table `pasien`
--
ALTER TABLE `pasien`
  ADD PRIMARY KEY (`KTP`),
  ADD KEY `KTP` (`KTP`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`IdUser`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kedatangan`
--
ALTER TABLE `kedatangan`
  MODIFY `No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `IdUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `kedatangan`
--
ALTER TABLE `kedatangan`
  ADD CONSTRAINT `kedatangan_ibfk_1` FOREIGN KEY (`KTP`) REFERENCES `pasien` (`KTP`),
  ADD CONSTRAINT `kedatangan_ibfk_2` FOREIGN KEY (`IdDokter`) REFERENCES `dokter` (`IdDokter`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
