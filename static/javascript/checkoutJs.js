


document.addEventListener("DOMContentLoaded", function() {
    if (localStorage.getItem('panier') == null) {
        var panier = {};
    } else {
        panier = JSON.parse(localStorage.getItem('panier'));
    }

    function updatePanierCount() {
        document.getElementById("panier").innerHTML = "Panier = " + Object.keys(panier).length;
    }

    updatePanierCount();

    function renderTable() {
        let total = 0;
        let tableString = `
            <table>
                <thead>
                    <tr>
                        <td>Image</td>
                        <td>Quantité</td>
                        <td>Prix</td>
                        <td>Action</td>
                    </tr>
                </thead>
                <tbody>
        `;

        for (let item in panier) {
            let nom = panier[item][1];
            let quantite = panier[item][0];
            let prix = parseFloat(panier[item][2]);

            let prixTotal = quantite * prix; 
            total += prixTotal; 

            tableString += `
                <tr>
                    <td>
                        <div>${nom}</div>
                        <div>Couleur : ${panier[item][4]}</div>
                        <div>Taille : ${panier[item][5]}</div>
                        <div><img src="${panier[item][3]}" style="width: 100px; height: auto;"></div>
                    </td>
                    <td>${quantite}</td>
                    <td>${prixTotal.toFixed(2)} FCFA</td>
                    <td>
                        <span><button class="btn btn-success add-quantity" data-id="${item}">Augmenter</button></span>
                        <span><button class="btn btn-danger reduce-quantity" data-id="${item}">Réduire</button></span>
                    </td>
                </tr>
            `;
        }

        tableString += `
                </tbody>
            </table>
            <div>
                Total: <span id="total">${total.toFixed(2)} FCFA</span>
            </div>
        `;

        $('#item-list').html(tableString);
        updatePanierCount();
        document.getElementById('total1').value = total.toFixed(2) + " FCFA";

        $('#items').val(JSON.stringify(panier)); // Met à jour le champ caché ici
    }

    renderTable(); 

    $(document).on('click', '.reduce-quantity', function() {
        let item_id = $(this).data('id');
        if (panier[item_id]) {
            panier[item_id][0]--; 
            if (panier[item_id][0] <= 0) {
                delete panier[item_id]; 
            }
            localStorage.setItem('panier', JSON.stringify(panier)); 
            renderTable(); 
        }
    });

    $(document).on('click', '.add-quantity', function(){
        let item_id = $(this).data('id');
        if (panier[item_id]) {
            panier[item_id][0]++;
        }
        localStorage.setItem('panier', JSON.stringify(panier));
        renderTable();
    });

    updatePanierCount();

    // Ajouter un gestionnaire d'événements pour le formulaire
    $('form').on('submit', function() {
        $('#items').val(JSON.stringify(panier)); // Met à jour le champ caché avant la soumission
    });
});