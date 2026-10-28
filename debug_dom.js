
const table = document.querySelector('.qr-card-table');
const row = document.querySelector('.qr-card-row');
const btnTd = document.querySelector('.qr-col-btn');
const qrTd = document.querySelector('.qr-col-code');
const qrImg = document.querySelector('.qr-img');
console.log(JSON.stringify({
    tableRect: table.getBoundingClientRect(),
    btnTdRect: btnTd.getBoundingClientRect(),
    qrTdRect: qrTd.getBoundingClientRect(),
    qrImgRect: qrImg.getBoundingClientRect()
}));
