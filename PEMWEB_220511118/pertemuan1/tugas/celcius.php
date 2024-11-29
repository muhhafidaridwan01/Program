<!DOCTYPE html>
<html lang="id">
<head>
    <title>Konversi Suhu Celcius</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Kuliah Pemrograman Web">
    <meta name="keywords" content="HTML, CSS, JS, PHP">
    <meta name="author" content="Hafid">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="icon" type="image/x-icon" href="./assets/favicon.ico"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
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
            border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            background-color: white;
            width: 400px;
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
            margin-bottom: 30px;
            text-align: center;
        }
        .form-group input, .form-group select {
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ced4da;
            background-color: #f8f9fa;
            transition: border 0.3s ease, background-color 0.3s ease;
        }
        .form-group input:focus, .form-group select:focus {
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
    </style>
</head>

<body>
    <?php
    session_start();
    
    // Hapus session jika ada
    if ($_SERVER["REQUEST_METHOD"] != "POST") {
        session_unset();
        session_destroy();
    }
    ?>

    <div class="card">
        <h3><i class="fas fa-thermometer-half"></i> Konversi Suhu dari Celcius</h3>
        
        <form method="post" action="">
            <div class="form-group">
                <label for="celcius">Masukkan suhu dalam Celcius:</label>
                <input type="number" class="form-control" id="celcius" name="celcius" placeholder="Masukkan suhu" required value="<?php echo isset($_POST['celcius']) ? htmlspecialchars($_POST['celcius']) : ''; ?>">
            </div>

            <div class="form-group">
                <label for="konversi_ke">Pilih konversi ke:</label>
                <select class="form-control" id="konversi_ke" name="konversi_ke" required>
                    <option value="" disabled selected>Pilih satuan</option>
                    <option value="fahrenheit" <?php if (isset($_POST['konversi_ke']) && $_POST['konversi_ke'] == 'fahrenheit') echo 'selected'; ?>>Fahrenheit</option>
                    <option value="reamur" <?php if (isset($_POST['konversi_ke']) && $_POST['konversi_ke'] == 'reamur') echo 'selected'; ?>>Reamur</option>
                    <option value="kelvin" <?php if (isset($_POST['konversi_ke']) && $_POST['konversi_ke'] == 'kelvin') echo 'selected'; ?>>Kelvin</option>
                </select>
            </div>

            <!-- Display results if form is submitted -->
            <?php
            if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['konversi_ke'])) {
                $celcius = $_POST['celcius'];
                $konversi_ke = $_POST['konversi_ke'];
                $output = "";

                // Lakukan konversi berdasarkan pilihan
                if ($konversi_ke == "fahrenheit") {
                    $output = ($celcius * 9/5) + 32 . " °F";
                } elseif ($konversi_ke == "reamur") {
                    $output = $celcius * 4/5 . " °R";
                } elseif ($konversi_ke == "kelvin") {
                    $output = $celcius + 273.15 . " K";
                }

                // Tampilkan hasil
                echo "<div class='form-group mt-4'>
                        <label for='hasil'>Hasil Konversi:</label>
                        <input type='text' class='form-control' id='hasil' value='" . htmlspecialchars($output) . "' readonly>
                      </div>";
            } else {
                // Tampilkan placeholder jika tidak ada hasil
                echo "<div class='form-group mt-4'>
                        <label for='hasil'>Hasil Konversi:</label>
                        <input type='text' class='form-control' id='hasil' placeholder='Hasilnya akan keluar disini' readonly>
                      </div>";
            }
            ?>

            <!-- Submit button -->
            <button type="submit" class="btn btn-primary btn-block">Konversi</button>
        </form>
    </div>
</body>
</html>
