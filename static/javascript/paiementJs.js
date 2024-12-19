

document.getElementById('payment-method').addEventListener('change', function() {
    const method = this.value;
    document.getElementById('mobile-details').style.display = (method === 'mtn' || method === 'orange') ? 'block' : 'none';
    document.getElementById('card-details').style.display = (method === 'card') ? 'block' : 'none';
});

document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const method = document.getElementById('payment-method').value;
    let paymentData = { method };

    if (method === 'mtn' || method === 'orange') {
        paymentData.phoneNumber = document.getElementById('phone-number').value;
    } else if (method === 'card') {
        paymentData.cardNumber = document.getElementById('card-number').value;
        paymentData.expiryDate = document.getElementById('expiry-date').value;
        paymentData.cvv = document.getElementById('cvv').value;
    }

    // Appel à l'API de paiement
    fetch('/paiement', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(paymentData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.response === 200) {
            alert('Paiement réussi !');
        } else {
            alert('Erreur de paiement : ' + data.message);
        }
    })
    .catch(error => {
        console.error('Erreur :', error);
        alert('Erreur lors du traitement du paiement.');
    });

    // Mettre à jour le panier
    function updatePanierCount() {
        document.getElementById("panier").innerHTML = "Panier = " + Object.keys(panier).length;
    }

    updatePanierCount();
});