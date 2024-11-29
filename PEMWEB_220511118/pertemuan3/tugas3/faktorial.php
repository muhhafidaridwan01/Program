<!DOCTYPE html>
<html lang="id">
<head>
    <title>Faktorial</title>
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
    </style>
</head>

<body>
    <div class="card">
        <h3><i class="fas fa-calculator"></i> Hitung Faktorial</h3>
        
        <form method="post" action="">
            <div class="form-group">
                <label for="n">Masukkan nilai n:</label>
                <input type="number" class="form-control" id="n" name="n" placeholder="Masukkan angka" required value="<?php echo isset($_POST['n']) ? htmlspecialchars($_POST['n']) : ''; ?>">
            </div>

            <?php
            function factorial($n) {
                if ($n < 0) {
                    return ["Faktorial tidak terdefinisi untuk bilangan negatif.", ""];
                } elseif ($n == 0 || $n == 1) {
                    return [1, "1"];
                } else {
                    $result = 1;
                    $factors = [];
                    for ($i = $n; $i >= 1; $i--) {
                        $factors[] = $i;
                        $result *= $i;
                    }
                    return [$result, implode(" x ", $factors)];
                }
            }

            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $n = intval($_POST["n"]);
                list($result, $factors) = factorial($n);
                echo "<div class='form-group mt-4'>
                        <label for='hasil'>Hasil Faktorial:</label>
                        <input type='text' class='form-control' id='hasil' value='$n! = $factors = $result' readonly>
                      </div>";
            } else {
                echo "<div class='form-group mt-4'>
                        <label for='hasil'>Hasil Faktorial:</label>
                        <input type='text' class='form-control' id='hasil' placeholder='Hasilnya akan keluar disini' readonly>
                      </div>";
            }
            ?>

            <button type="submit" class="btn btn-primary btn-block">Hitung Faktorial</button>
        </form>
    </div>
</body>
</html>
