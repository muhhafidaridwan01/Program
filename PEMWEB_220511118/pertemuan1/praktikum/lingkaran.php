<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplikasi Menghitung Luas dan Keliling Lingkaran</title>
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
            overflow: hidden; /* Prevent scroll bar during animation */
        }
        .card {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            background-color: white;
            width: 400px;
            display: flex;
            flex-direction: column;
            height: auto;
            animation: float 3s ease-in-out infinite; /* Floating animation */
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
            margin-bottom: 30px;
            text-align: center;
        }
        .form-group input {
            margin-bottom: 20px;
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
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            transition: background 0.3s ease, transform 0.3s ease;
            margin-top: 20px;
        }
        .btn-primary:hover {
            background: linear-gradient(45deg, #66a6ff, #007bff);
            transform: scale(1.03);
        }
        .btn-primary:active {
            transform: scale(0.98);
        }
        .circle-img {
            width: 80px;
            height: 80px;
            vertical-align: middle;
            margin-left: 10px;
        }
    </style>
</head>

<body>
    <div class="card">
        <h3>Kalkulator Lingkaran <img src="https://cdn-icons-png.flaticon.com/512/1077/1077063.png" alt="Lingkaran" class="circle-img"/></h3>
        
        <form name="form1" method="POST" action="">
            <div class="form-group">
                <label for="jari_jari">Jari-jari :</label>
                <input type="number" class="form-control" name="jari_jari" id="jari_jari" placeholder="Masukkan jari-jari" required min="0" value="<?php echo isset($_POST['jari_jari']) ? htmlspecialchars($_POST['jari_jari']) : ''; ?>" />
            </div>

            <div id="hasil">
                <div class="form-group">
                    <label for="outputLuas">Luas Lingkaran</label>
                    <input type="text" class="form-control" id="outputLuas" placeholder="Luas akan muncul di sini" readonly>
                </div>
                <div class="form-group">
                    <label for="outputKeliling">Keliling Lingkaran</label>
                    <input type="text" class="form-control" id="outputKeliling" placeholder="Keliling akan muncul di sini" readonly>
                </div>
            </div>

            <!-- Submit button -->
            <button type="submit" class="btn btn-primary btn-block">Hitung</button>
        </form>

        <?php
        if (isset($_POST['jari_jari']) && is_numeric($_POST['jari_jari'])) {
            $jari_jari = $_POST['jari_jari'];
            $luas = pi() * pow($jari_jari, 2);
            $keliling = 2 * pi() * $jari_jari;

            // Output results in read-only fields
            echo "<script>
                    document.getElementById('outputLuas').value = '" . number_format($luas, 2) . " satuan²';
                    document.getElementById('outputKeliling').value = '" . number_format($keliling, 2) . " satuan';
                  </script>";
        }
        ?>
    </div>
</body>
</html>
