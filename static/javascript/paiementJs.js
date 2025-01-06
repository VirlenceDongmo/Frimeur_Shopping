document.getElementById('payment-method').addEventListener('change', function() {
    const method = this.value;
    const mobileDetails = document.getElementById('mobile-details');
    const paypalButtonContainer = document.getElementById('paypal-button-container');
    const submitButton = document.getElementById('submit-button');

    if (method === 'mtn' || method === 'orange') {
        mobileDetails.style.display = 'block';
        paypalButtonContainer.style.display = 'none';
        submitButton.style.display = 'inline'; 
    } else if (method === 'paypal') {
        window.location.href = "/paypal/";
    } else {
        mobileDetails.style.display = 'none';
        paypalButtonContainer.style.display = 'none';
        submitButton.style.display = 'inline'; 
    }
});

document.getElementById('submit-button').addEventListener('click', function() {
    const method = document.getElementById('payment-method').value;
    if (method === 'paypal') {
        window.location.href = "/paypal/";
    } else {
        document.getElementById('payment-form').submit();
    }
});

function updatePanierCount() {
    document.getElementById("panier").innerHTML = "Panier = " + Object.keys(panier).length;
}

updatePanierCount();