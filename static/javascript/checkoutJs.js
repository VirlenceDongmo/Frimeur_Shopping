


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

    if(Object.keys(panier).length == 0) {
        $('#formulaireDeCommande').hide()
    }

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
    
        for (let uniqueKey in panier) {
            let nom = panier[uniqueKey][1];
            let quantite = panier[uniqueKey][0];
            let prix = parseFloat(panier[uniqueKey][2]);
    
            let prixTotal = quantite * prix; 
            total += prixTotal; 
    
            tableString += `
                <tr>
                    <td>
                        <div>${nom}</div>
                        <div>Couleur : ${panier[uniqueKey][4]}</div>
                        <div>Taille : ${panier[uniqueKey][5]}</div>
                        <div><img src="${panier[uniqueKey][3]}" style="width: 100px; height: auto;"></div>
                    </td>
                    <td>${quantite}</td>
                    <td>${prixTotal.toFixed(2)} FCFA</td>
                    <td>
                        <span><button class="btn btn-success add-quantity" data-id="${uniqueKey}">+</button></span>
                        <span><button class="btn btn-danger reduce-quantity" data-id="${uniqueKey}">-</button></span>
                    </td>
                </tr>
            `;
        }
    
        tableString += `
                </tbody>
            </table>
        `;

        $('.totalDesCommandes').text('Total = ' + total.toFixed(2) + ' FCFA');

        localStorage.setItem('totalcom', total)
    
        $('#item-list').html(tableString);

        updatePanierCount();
        document.getElementById('total1').value = total.toFixed(2) + " FCFA";
    
        $('#items').val(JSON.stringify(panier)); // Met à jour le champ caché ici

        console.log(total)
    }

    renderTable(); 

    $(document).on('click', '.reduce-quantity', function() {
        let uniqueKey = $(this).data('id');
        if (panier[uniqueKey]) {
            panier[uniqueKey][0]--; 
            if (panier[uniqueKey][0] <= 0) {
                delete panier[uniqueKey]; 
            }
            localStorage.setItem('panier', JSON.stringify(panier)); 
            renderTable(); 
        }
    });
    
    $(document).on('click', '.add-quantity', function(){
        let uniqueKey = $(this).data('id');
        if (panier[uniqueKey]) {
            panier[uniqueKey][0]++;
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