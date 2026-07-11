function showMessage(message) {
    alert(message);
}

function copyUPI() {
    const upi = "BHARATPE2C0E0F1I4X76930@unitype";
    navigator.clipboard.writeText(upi);
    alert("UPI ID Copied Successfully!");
}

console.log("Company Work Website Loaded");
