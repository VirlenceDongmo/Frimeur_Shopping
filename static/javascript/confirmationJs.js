

if(localStorage.getItem('panier') == null){
    var panier = {}
}else{
    panier = JSON.parse(localStorage.getItem('panier'));
}

function updatePanierCount() {
    document.getElementById("panier").innerHTML = "Panier = " + Object.keys(panier).length;
}

updatePanierCount();

$(document).on('click', '.ted', function() {
    var item_id = this.id.toString();
    var imageUrl = $(this).data('image');
    
    if (panier[item_id] != undefined) {
        // Si l'article existe déjà, augmentez simplement la quantité
        panier[item_id][0]++; // Augmentez la quantité
    } else {
        // Si c'est un nouvel article, ajoutez-le au panier
        var prix = parseFloat(document.getElementById('price' + item_id).innerHTML);
        var nom = document.getElementById("aa" + item_id).innerHTML;
        panier[item_id] = [1, nom, prix, imageUrl]; // Initialise la quantité à 1
    }
    
    localStorage.setItem('panier', JSON.stringify(panier));
    updatePanierCount();
});

AfficherList(panier)

function AfficherList(panier){
    var panierString = ""
    var index = 1
    for(var x in panier){
        panierString += "Article " + index + " :"
        panierString += document.getElementById("aa"+x).innerHTML + " :"+ " Quantité = " + panier[x][0] + "</br>"
        index++
    }

    //panierString += "<a href='{% url 'panier' %}' class='btn btn-primary'>Voir le panier</a>"

    $('[data-toggle="popover"]').popover()
    document.getElementById("panier").setAttribute('data-content', panierString)
}