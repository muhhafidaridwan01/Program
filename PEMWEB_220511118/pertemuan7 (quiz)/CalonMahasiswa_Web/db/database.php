<?php
require_once __DIR__ . "/../vendor/autoload.php"; // add this library using: composer require vlucas/phpdotenv

class Database {
    private $pdo;  // Mendeklarasikan properti $pdo yang akan menyimpan koneksi database

    public function __construct() {
        // Memuat variabel lingkungan dari file .env
        $dotenv = Dotenv\Dotenv::createImmutable(__DIR__ . "/..");
        $dotenv->load();

        // Mengambil data konfigurasi dari variabel lingkungan
        $host = $_ENV["DB_HOST"];
        $dbname = $_ENV["DB_DATABASE"];
        $username = $_ENV["DB_USERNAME"];
        $password = $_ENV["DB_PASSWORD"];
        $charset = $_ENV["DB_CHARSET"];
        
        // Memanggil fungsi connect untuk menghubungkan ke database
        $this->connect($host, $dbname, $username, $password, $charset);
    }

    private function connect($host, $dbname, $username, $password, $charset) {
        try {
            // Mencoba untuk menghubungkan ke database dengan menggunakan PDO
            $this->pdo = new PDO("mysql:host={$host};dbname={$dbname};charset={$charset}", $username, $password);
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);  // Mengatur mode error menjadi exception
            
        } catch (PDOException $e) {
            // Menangkap kesalahan jika koneksi gagal dan menampilkan pesan kesalahan
            die("Database connection failed: " . $e->getMessage());
        }
    }

    public function query($sql, $params = []) {
        // Menyiapkan statement SQL
        $stmt = $this->pdo->prepare($sql);

        if ($stmt) {
            // Menjalankan query dengan parameter yang diberikan
            $stmt->execute($params);
            return $stmt;  // Mengembalikan statement yang telah dijalankan
        } else {
            // Jika terjadi kesalahan dalam persiapan query
            die("Error in query: " . print_r($this->pdo->errorInfo(), true));
        }
    }

    public function executeQuery($sql, $params = []) {
        try {
            // Menyiapkan dan mengeksekusi query SQL yang diberikan
            $stmt = $this->pdo->prepare($sql);

            if ($stmt) {
                // Menjalankan query dengan parameter yang diberikan
                $stmt->execute($params);
                return $stmt;  // Mengembalikan statement yang telah dijalankan
            } else {
                // Jika terjadi kesalahan dalam persiapan query
                die("Error in query: " . print_r($this->pdo->errorInfo(), true));
            }
        } catch (PDOException $e) {
            // Menangkap kesalahan PDO dan menampilkan pesan kesalahan
            die("Database error: " . $e->getMessage());
        }
    }

    public function getLastInsertId() {
        // Mengembalikan ID terakhir yang dimasukkan ke dalam database
        return $this->pdo->lastInsertId();
    }
    
}
