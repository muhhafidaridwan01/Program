<!-- class = untuk memberikan satu atau beberapa nama kelas (class) pada elemen HTML.
name = memberikan nama pada elemen form. Nama ini dapat digunakan untuk mengidentifikasi form saat melakukan pemrosesan atau interaksi dengan JavaScript.
method = atribut method menentukan cara pengiriman data dari form ke server. 
-->
<form class="form-control" name="form1" method="POST" action="">
    <div class="mb-3">
        <label id="nilai" for="nilai">Nilai Akhir:</label>
        <input id="nilai" name="nilai" type="text" class="form-control"/>
    </div>
    <input id="kirim" name="kirim" type="hidden" class="form-control" value="1"/>
    <button type="submit" class="btn btn-dark">Submit</button>
</form>

<?php 

$nilai_akhir="";
$mutu="";
if(isset($_POST['kirim'])=="1"){
    $nilai_akhir=$_POST['nilai'];
    if($nilai_akhir>=85){
        $mutu = "A";
    } elseif($nilai_akhir>=75){
        $mutu = "B";
    } elseif($nilai_akhir>=55){
        $mutu = "C";
    } else {
        $mutu = "E";
    }
}
echo("Nilai Akhir=".$nilai_akhir);
echo("<br/>");
echo("Nilai Mutu=".$mutu);
?>


























/*isset($_POST['kirim']): Mengecek apakah elemen bernama "kirim" ada di dalam data POST.
$_POST['kirim'] == "1": Mengecek apakah nilai dari elemen "kirim" adalah "1".
$nilai = $_POST['nilai'] : adalah cara untuk mengambil data dari form HTML yang dikirim melalui metode POST. 
if(isset($_POST['kirim'])=="1"){
    $nilai = $_POST['nilai'];
    if($nilai>=60){
        echo("Anda lulus.");
    }else{
        echo("Anda tidak lulus.");
    }
}
*/ 