<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplikasi Menghitung Volume dan Luas Permukaan Tabung</title>
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
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            background-color: white;
            width: 350px; /* Lebar diperluas */
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
        .title-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }
        .title-container h3 {
            color: #343a40;
            margin: 0;
            font-size: 20px; /* Ukuran font dikurangi */
        }
        .icon-img {
            width: 80px; /* Ukuran ikon diperbesar */
            height: 80px;
            margin-left: 10px; /* Jarak antara ikon dan teks */
        }
        .form-group input {
            margin-bottom: 15px;
            padding: 10px;
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
            padding: 10px; /* Memperbesar padding */
            font-size: 16px; /* Memperbesar ukuran font */
            border-radius: 5px;
            transition: background 0.3s ease, transform 0.3s ease;
            margin-top: 20px; /* Memperbesar margin atas */
        }
        .btn-primary:hover {
            background: linear-gradient(45deg, #66a6ff, #007bff);
            transform: scale(1.03);
        }
        .btn-primary:active {
            transform: scale(0.98);
        }
    </style>
</head>

<body>
    <div class="card">
        <div class="title-container">
            <h3>Kalkulator Tabung</h3>
            <img src="https://png.pngtree.com/png-clipart/20230407/original/pngtree-fused-liquids-line-icon-png-image_9033979.png" alt="Tabung" class="icon-img"/>
        </div>
        
        <form name="form1" method="POST" action="">
            <div class="form-group">
                <label for="jari_jari">Jari-jari Alas :</label>
                <input type="number" class="form-control" name="jari_jari" id="jari_jari" placeholder="Masukkan jari-jari" required min="0" value="<?php echo isset($_POST['jari_jari']) ? htmlspecialchars($_POST['jari_jari']) : ''; ?>" />
            </div>
            <div class="form-group">
                <label for="tinggi">Tinggi :</label>
                <input type="number" class="form-control" name="tinggi" id="tinggi" placeholder="Masukkan tinggi" required min="0" value="<?php echo isset($_POST['tinggi']) ? htmlspecialchars($_POST['tinggi']) : ''; ?>" />
            </div>

            <div id="hasil">
                <div class="form-group">
                    <label for="outputVolume">Volume Tabung</label>
                    <input type="text" class="form-control" id="outputVolume" placeholder="Volume akan muncul di sini" readonly>
                </div>
                <div class="form-group">
                    <label for="outputLuas">Luas Permukaan Tabung</label>
                    <input type="text" class="form-control" id="outputLuas" placeholder="Luas permukaan akan muncul di sini" readonly>
                </div>
            </div>

            <button type="submit" class="btn btn-primary btn-block">Hitung</button>
        </form>

        <?php
        if (isset($_POST['jari_jari']) && is_numeric($_POST['jari_jari']) &&
            isset($_POST['tinggi']) && is_numeric($_POST['tinggi'])) {

            $jari_jari = $_POST['jari_jari'];
            $tinggi = $_POST['tinggi'];

            // Hitung volume dan luas permukaan
            $volume = pi() * pow($jari_jari, 2) * $tinggi;
            $luas_permukaan = 2 * pi() * $jari_jari * ($jari_jari + $tinggi);

            // Output hasil di field readonly
            echo "<script>
                    document.getElementById('outputVolume').value = '" . number_format($volume, 2) . " satuan³';
                    document.getElementById('outputLuas').value = '" . number_format($luas_permukaan, 2) . " satuan²';
                  </script>";
        }
        ?>
    </div>
</body>
</html>
