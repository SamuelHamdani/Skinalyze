// Format Pesan Whatsaoo
const formatMessage = (obj) => {
    return `Data Customer:
        Nama: ${obj.name}
        Email: ${obj.email}
        No HP: ${obj.phone}
        Alamat: ${obj.alamat}
    Data Pesanan:
    ${JSON.parse(obj.items).map((item) => `${item.name} (${item.quantity} x ${rupiah(item.total)}) \n`)}
    Total Harga: ${rupiah(obj.total)}
    Terima Kasih.`;
}

// Contact Form
function sendToWhatsApp(event) {
    event.preventDefault();

    const name = document.getElementById("contactName").value;
    const email = document.getElementById("contactEmail").value;
    const phone = document.getElementById("contactPhone").value;
    const message = document.getElementById("pesan").value;

    const whatsappMessage = `Nama: ${name}%0AEmail: ${email}%0ANomor HP: ${phone}%0APesan: ${message}`;

    const whatsappUrl = `https://wa.me/6282246689642?text=${whatsappMessage}`;

    window.open(whatsappUrl, '_blank');
}