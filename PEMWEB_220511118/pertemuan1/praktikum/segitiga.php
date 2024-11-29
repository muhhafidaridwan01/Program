<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplikasi Menghitung Luas dan Keliling Segitiga</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="icon" type="image/x-icon" href="./assets/favicon.ico"/>
    <style>
        body {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
        }
        .card {
            padding: 15px; /* Mengurangi padding */
            border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            background-color: white;
            width: 300px; /* Mengecilkan lebar */
            display: flex;
            flex-direction: column;
            height: auto;
            animation: float 3s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }
        .card h3 {
            color: #343a40;
            margin-bottom: 20px; /* Mengecilkan margin bawah */
            text-align: center;
        }
        .form-group input {
            margin-bottom: 15px; /* Mengecilkan margin bawah */
            padding: 8px; /* Mengecilkan padding */
            border-radius: 5px;
            border: 1px solid #ced4da;
            background-color: #f8f9fa;
            transition: border 0.3s ease, background-color 0.3s ease;
        }
        .form-group input:focus {
            border-color: #007bff;
            background-color: #ffffff;
        }
        #hasil {
            margin-top: 10px;
        }
        .form-group label {
            text-align: left;
            font-weight: bold;
            color: #495057;
        }
        .form-group input[readonly] {
            background-color: #f1f3f5;
            border-color: #ced4da;
        }
        .btn-primary {
            background: linear-gradient(45deg, #007bff, #66a6ff);
            border: none;
            padding: 8px; /* Mengecilkan padding */
            font-size: 14px; /* Mengecilkan ukuran font */
            border-radius: 5px;
            transition: background 0.3s ease, transform 0.3s ease;
            margin-top: 15px; /* Mengurangi margin atas */
        }
        .btn-primary:hover {
            background: linear-gradient(45deg, #66a6ff, #007bff);
            transform: scale(1.03);
        }
        .btn-primary:active {
            transform: scale(0.98);
        }
        .triangle-img {
            width: 60px; /* Mengecilkan ukuran gambar */
            height: 60px;
            vertical-align: middle;
            margin-left: 10px;
        }
    </style>
</head>

<body>
    <div class="card">
        <h3>Kalkulator Segitiga <img src="https://png.pngtree.com/png-clipart/20230330/original/pngtree-triangular-scale-line-icon-png-image_9009978.png" alt="Segitiga" class="triangle-img"/></h3>
        
        <form name="form1" method="POST" action="">
            <div class="form-group">
                <label for="alas">Alas :</label>
                <input type="number" class="form-control" name="alas" id="alas" placeholder="Masukkan alas" required min="0" value="<?php echo isset($_POST['alas']) ? htmlspecialchars($_POST['alas']) : ''; ?>" />
            </div>
            <div class="form-group">
                <label for="tinggi">Tinggi :</label>
                <input type="number" class="form-control" name="tinggi" id="tinggi" placeholder="Masukkan tinggi" required min="0" value="<?php echo isset($_POST['tinggi']) ? htmlspecialchars($_POST['tinggi']) : ''; ?>" />
            </div>
            <div class="form-group">
                <label for="sisi">Sisi miring :</label>
                <input type="number" class="form-control" name="sisi" id="sisi" placeholder="Masukkan sisi miring" required min="0" value="<?php echo isset($_POST['sisi']) ? htmlspecialchars($_POST['sisi']) : ''; ?>" />
            </div>

            <div id="hasil">
                <div class="form-group">
                    <label for="outputLuas">Luas Segitiga</label>
                    <input type="text" class="form-control" id="outputLuas" placeholder="Luas akan muncul di sini" readonly>
                </div>
                <div class="form-group">
                    <label for="outputKeliling">Keliling Segitiga</label>
                    <input type="text" class="form-control" id="outputKeliling" placeholder="Keliling akan muncul di sini" readonly>
                </div>
            </div>

            <button type="submit" class="btn btn-primary btn-block">Hitung</button>
        </form>

        <?php
        if (isset($_POST['alas']) && is_numeric($_POST['alas']) &&
            isset($_POST['tinggi']) && is_numeric($_POST['tinggi']) &&
            isset($_POST['sisi']) && is_numeric($_POST['sisi'])) {

            $alas = $_POST['alas'];
            $tinggi = $_POST['tinggi'];
            $sisi = $_POST['sisi'];

            // Hitung luas dan keliling
            $luas = 0.5 * $alas * $tinggi;
            $keliling = $alas + $tinggi + $sisi;

            // Output hasil di field readonly
            echo "<script>
                    document.getElementById('outputLuas').value = '" . number_format($luas, 2) . " satuan²';
                    document.getElementById('outputKeliling').value = '" . number_format($keliling, 2) . " satuan';
                  </script>";
        }
        ?>
    </div>
</body>
</html>
