

if(localStorage.getItem('panier') == null){
    var panier = {};
} else {
    panier = JSON.parse(localStorage.getItem('panier'));
}

function updatePanierCount() {
    document.getElementById("panier").innerHTML = "Panier = " + Object.keys(panier).length;
}

updatePanierCount();

$(document).on('click', '.ted', function(){
    var item_id = this.id.toString();
    var imageUrl = $(this).data('image')
    console.log(item_id);
    if(panier[item_id] != undefined){
        var quantite = panier[item_id][0] + 1;
        panier[item_id][0] = quantite;
        panier[item_id][2] += parseFloat(document.getElementById('price' + item_id).innerHTML);
    } else {
        var quantite = 1;
        var prix = parseFloat(document.getElementById('price' + item_id).innerHTML);
        var nom = document.getElementById("aa" + item_id).innerHTML; // Assurez-vous d'avoir cet élément
        panier[item_id] = [quantite, nom, prix];
    }
    console.log(panier);
    localStorage.setItem('panier', JSON.stringify(panier));

    updatePanierCount();
});

AfficherList(panier);

function AfficherList(panier){
    var panierString = "";
    var index = 1;
    for(var x in panier){
        panierString += "Article " + index + " : ";
        panierString += document.getElementById("aa" + x).innerHTML + " : Quantité = " + panier[x][0] + "<br>";
        index++;
    }

    $('[data-toggle="popover"]').popover();
    document.getElementById("panier").setAttribute('data-content', panierString);
}