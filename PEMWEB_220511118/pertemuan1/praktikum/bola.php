<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplikasi Menghitung Volume dan Luas Permukaan Bola</title>
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
            overflow: hidden; /* Mencegah scroll bar saat animasi */
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
            animation: float 3s ease-in-out infinite; /* Menambahkan animasi mengambang */
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
            margin-bottom: 30px; /* Jarak antara judul dan input */
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
        .bola-img {
            width: 40px; /* Ukuran gambar bola */
            height: 40px; /* Ukuran gambar bola */
            vertical-align: middle; /* Menyelaraskan dengan teks */
            margin-left: 10px; /* Jarak antara teks dan gambar */
        }
    </style>
</head>

<body>
    <div class="card">
        <h3>Kalkulator Bola <img src="https://img.icons8.com/material-rounded/24/000000/sphere.png" alt="Bola" class="bola-img"/></h3>

        <form id="bolaForm">
            <div class="form-group">
                <input type="number" class="form-control" name="jari_jari" id="jari_jari" placeholder="Masukkan Jari-jari" required />
            </div>

            <!-- Output kotak untuk hasil, tidak akan hilang -->
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

            <!-- Tombol hitung di bagian paling bawah -->
            <button type="submit" class="btn btn-primary btn-block">Hitung</button>
        </form>
    </div>

    <script>
        document.getElementById('bolaForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Mencegah halaman melakukan reload

            // Mendapatkan nilai jari-jari
            let jari_jari = document.getElementById('jari_jari').value;

            // Validasi apakah input adalah angka
            if (jari_jari && !isNaN(jari_jari)) {
                jari_jari = parseFloat(jari_jari);

                // Perhitungan volume dan luas permukaan
                const volume = (4 / 3) * Math.PI * Math.pow(jari_jari, 3);
                const luas_permukaan = 4 * Math.PI * Math.pow(jari_jari, 2);

                // Menampilkan hasil di dalam input readonly
                document.getElementById('outputVolume').value = volume.toFixed(2) + ' satuan³';
                document.getElementById('outputLuas').value = luas_permukaan.toFixed(2) + ' satuan²';
            } else {
                document.getElementById('outputVolume').value = '';
                document.getElementById('outputLuas').value = '';
                alert("Masukkan jari-jari yang valid!");
            }
        });
    </script>
</body>
</html>
