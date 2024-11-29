<?php
$gajiPokok = '';
$status = '';
$jumlahAnak = '';
$tunjanganIstri = 0;
$tunjanganAnak = 0;
$totalPenghasilan = 0;
$pesanError = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $gajiPokok = $_POST['gajiPokok'];
    $status = $_POST['status'];
    $jumlahAnak = $_POST['jumlahAnak'];

    if (is_numeric($gajiPokok) && $gajiPokok > 0 && is_numeric($jumlahAnak) && $jumlahAnak >= 0) {
        if ($status == 'Menikah') {
            $tunjanganIstri = 0.1 * $gajiPokok; 
        }

        if ($status == 'Menikah' && $jumlahAnak > 0) {
            $tunjanganAnak = 0.05 * $gajiPokok * $jumlahAnak; // 5% dari Gaji Pokok x jumlah anak
        }

        $totalPenghasilan = $gajiPokok + $tunjanganIstri + $tunjanganAnak;
    } else {
        $pesanError = 'Masukkan data yang valid untuk Gaji Pokok dan Jumlah Anak.';
    }
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Penghitungan Tunjangan</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
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
            width: 600px;
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
        .form-row {
            display: flex;
            justify-content: space-between;
        }
        .form-row .form-group {
            flex: 1;
            margin-right: 10px;
        }
        .form-row .form-group:last-child {
            margin-right: 0;
        }
    </style>
</head>
<body>
    <div class="card">
        <h3><i class="fas fa-calculator"></i> Penghitungan Tunjangan</h3>
        <form method="POST" action="">
            <div class="form-group">
                <label for="gajiPokok">Gaji Pokok:</label>
                <input type="number" class="form-control" id="gajiPokok" name="gajiPokok" value="<?php echo $gajiPokok; ?>" placeholder="Masukkan gaji pokok">
            </div>

            <div class="form-group">
                <label for="status">Status Pernikahan:</label>
                <select class="form-control" id="status" name="status" required>
                    <option value="" disabled selected>Pilih status</option>
                    <option value="Menikah" <?php if ($status == 'Menikah') echo 'selected'; ?>>Menikah</option>
                    <option value="Duda" <?php if ($status == 'Duda') echo 'selected'; ?>>Duda</option>
                    <option value="Janda" <?php if ($status == 'Janda') echo 'selected'; ?>>Janda</option>
                    <option value="Single" <?php if ($status == 'Single') echo 'selected'; ?>>Single</option>
                </select>
            </div>

            <div class="form-group">
                <label for="jumlahAnak">Jumlah Anak (-18 thn):</label>
                <input type="number" class="form-control" id="jumlahAnak" name="jumlahAnak" value="<?php echo $jumlahAnak; ?>" placeholder="Masukkan jumlah anak">
            </div>

            <!-- Output perhitungan -->
            <div class="form-row mt-4">
                <div class="form-group">
                    <label for="tunjanganIstri">Tunjangan Istri:</label>
                    <input type="text" class="form-control" id="tunjanganIstri" value="Rp. <?php echo number_format($tunjanganIstri, 2); ?>" readonly>
                </div>

                <div class="form-group">
                    <label for="tunjanganAnak">Tunjangan Anak:</label>
                    <input type="text" class="form-control" id="tunjanganAnak" value="Rp. <?php echo number_format($tunjanganAnak, 2); ?>" readonly>
                </div>

                <div class="form-group">
                    <label for="totalPenghasilan">Total Penghasilan:</label>
                    <input type="text" class="form-control" id="totalPenghasilan" value="Rp. <?php echo number_format($totalPenghasilan, 2); ?>" readonly>
                </div>
            </div>

            <button type="submit" class="btn btn-primary btn-block">Hitung</button>

        </form>

        <?php if ($pesanError != ''): ?>
            <div class="alert alert-danger mt-3"><?php echo $pesanError; ?></div>
        <?php endif; ?>
    </div>
</body>
</html>
