<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplikasi Menghitung Volume dan Luas Permukaan Kerucut</title>
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
            margin-bottom: 30px; /* Spacing between title and input */
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
        .kerucut-img {
            width: 80px; /* Enlarged cone image size */
            height: 80px; /* Enlarged cone image size */
            vertical-align: middle; /* Align with text */
            margin-left: 10px; /* Spacing between text and image */
        }
    </style>
</head>

<body>
    <div class="card">
        <h3>Kalkulator Kerucut <img src="https://png.pngtree.com/png-clipart/20220530/original/pngtree-cone-of-white-color-linear-sketch-png-image_7764410.png" alt="Kerucut" class="kerucut-img"/></h3>
        
        <form name="form1" method="POST" action="">
            <div class="form-group">
                <label for="jari_jari">Jari-jari Alas :</label>
                <input type="number" class="form-control" name="jari_jari" id="jari_jari" placeholder="Masukkan jari-jari" required min="0" value="<?php echo isset($_POST['jari_jari']) ? htmlspecialchars($_POST['jari_jari']) : ''; ?>" />
            </div>
            <div class="form-group">
                <label for="tinggi">Tinggi :</label>
                <input type="number" class="form-control" name="tinggi" id="tinggi" placeholder="Masukkan tinggi" required min="0" value="<?php echo isset($_POST['tinggi']) ? htmlspecialchars($_POST['tinggi']) : ''; ?>" />
            </div>

            <!-- Output fields for results -->
            <div id="hasil">
                <div class="form-group">
                    <label for="outputVolume">Volume</label>
                    <input type="text" class="form-control" id="outputVolume" placeholder="Volume akan muncul di sini" readonly>
                </div>
                <div class="form-group">
                    <label for="outputLuas">Luas Permukaan</label>
                    <input type="text" class="form-control" id="outputLuas" placeholder="Luas permukaan akan muncul di sini" readonly>
                </div>
            </div>

            <!-- Submit button -->
            <button type="submit" class="btn btn-primary btn-block">Hitung</button>
        </form>

        <?php
        // Check if the radius and height data exists in POST
        if (isset($_POST['jari_jari']) && is_numeric($_POST['jari_jari']) &&
            isset($_POST['tinggi']) && is_numeric($_POST['tinggi'])) {

            $jari_jari = $_POST['jari_jari'];
            $tinggi = $_POST['tinggi'];

            // Calculate volume and surface area
            $volume = (1 / 3) * pi() * pow($jari_jari, 2) * $tinggi;
            // Calculate slant height (hypotenuse) for surface area
            $sisi_miring = sqrt(pow($jari_jari, 2) + pow($tinggi, 2));
            $luas_permukaan = pi() * $jari_jari * ($jari_jari + $sisi_miring);

            // Output results in read-only fields
            echo "<script>
                    document.getElementById('outputVolume').value = '" . number_format($volume, 2) . " satuan³';
                    document.getElementById('outputLuas').value = '" . number_format($luas_permukaan, 2) . " satuan²';
                  </script>";
        }
        ?>
    </div>
</body>
</html>
