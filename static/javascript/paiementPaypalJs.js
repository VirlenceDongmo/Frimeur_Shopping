

document.addEventListener("DOMContentLoaded", function() {

    let totalcom = parseFloat(localStorage.getItem('totalcom'));

    if (isNaN(totalcom)) {
        console.log("Le montant total est manquant ou invalide.");
    } else {
        console.log(totalcom); 
    }

    paypal.Buttons({
    
        createOrder: function(data, actions) {
    
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: totalcom
                    }
                }]
            });
        },
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(details) {
                alert("Transaction réussie : " + details.payer.name.given_name);
            });
        },
        onError: function(err) {
            console.error("Erreur de paiement : ", err);
            alert("Échec du paiement !");
        }
    }).render('#paypal-button-container');
});

