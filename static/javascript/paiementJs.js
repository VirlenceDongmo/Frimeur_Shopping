

document.getElementById('payment-method').addEventListener('change', function() {
    const method = this.value;
    document.getElementById('mobile-details').style.display = (method === 'mtn' || method === 'orange') ? 'block' : 'none';
});

document.getElementById('payment-form').addEventListener('submit', function() {

    function updatePanierCount() {
        document.getElementById("panier").innerHTML = "Panier = " + Object.keys(panier).length;
    }

    updatePanierCount();
});