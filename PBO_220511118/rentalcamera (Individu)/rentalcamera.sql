-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 24 Feb 2024 pada 10.22
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rentalcamera`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `camera`
--

CREATE TABLE `camera` (
  `id` int(11) NOT NULL,
  `kode_camera` varchar(100) NOT NULL,
  `merek_camera` varchar(100) NOT NULL,
  `tahun_rilis` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `catatan_order`
--

CREATE TABLE `catatan_order` (
  `id` int(11) NOT NULL,
  `namapelanggan` varchar(100) NOT NULL,
  `noktp` int(100) NOT NULL,
  `kodecamera` int(100) NOT NULL,
  `merekcamera` varchar(100) NOT NULL,
  `banyakcamera` int(100) NOT NULL,
  `statusbayar` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pelanggan`
--

CREATE TABLE `pelanggan` (
  `id` int(100) NOT NULL,
  `nama_pelanggan` varchar(100) NOT NULL,
  `jk` enum('Laki-laki','Perempuan') NOT NULL,
  `nomor_ktp` int(100) NOT NULL,
  `nomor_hp` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `id` int(11) NOT NULL,
  `namepelanggan` varchar(100) NOT NULL,
  `banyak_camera` enum('1','2','3','4','5') NOT NULL,
  `tanggal` date NOT NULL,
  `tarif_perjam` enum('10000','20000','30000','40000','50000') NOT NULL,
  `jam_peminjaman` varchar(100) NOT NULL,
  `jam_pengembalian` varchar(100) NOT NULL,
  `durasi_waktu` varchar(100) NOT NULL,
  `total_bayar` int(100) NOT NULL,
  `status_bayar` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('admin','pelanggan') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `email`, `nama`, `password`, `level`) VALUES
(1, 'hafid@umc.ac.id', 'Hafid', '$2y$10$BzqqNPejAUyOraPKKKCK2.xbrToZgOq9GnlmBtAMThvtB2zCTg4O.', 'admin'),
(2, 'ridho@gmail.com', 'Ridho', '$2y$10$NgiUETWu9BYXGKOTil.aOO5NobC1Nq5kREKYxG9cdnl4rhUZ/Tpci', 'pelanggan'),
(3, 'fitri@gmail.com', 'Fitri', '$2y$10$i.GRsHyXlF0DUlIyGF96Zul5PFkm3Rq7C/1WOxd19WmKQercK5J8i', 'pelanggan');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `camera`
--
ALTER TABLE `camera`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode_kamera` (`kode_camera`),
  ADD UNIQUE KEY `kode_kamera_2` (`kode_camera`);

--
-- Indeks untuk tabel `catatan_order`
--
ALTER TABLE `catatan_order`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `namapelanggan` (`namapelanggan`);

--
-- Indeks untuk tabel `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama_pelanggan` (`nama_pelanggan`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `namepelanggan` (`namepelanggan`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `camera`
--
ALTER TABLE `camera`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `catatan_order`
--
ALTER TABLE `catatan_order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
