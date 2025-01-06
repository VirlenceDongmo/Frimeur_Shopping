

paypal.Buttons({
    createOrder: function(data, actions) {

        let totalcom = parseFloat(localStorage.getItem('totalcom')) 
        
        if (!totalcom || isNaN(totalcom)) {
            alert("Le montant total est manquant ou invalide. Veuillez vérifier votre panier.");
            return;
        }

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