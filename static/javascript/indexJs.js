

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
    
    var size = $('#size' + item_id).val();
    var color = $('#color' + item_id).val();
    
 
    if (!size || !color) {
        alert('Veuillez sélectionner une taille et une couleur.');
        return;
    }
    
    
    var uniqueKey = item_id + '-' + size + '-' + color;

    if (panier[uniqueKey] != undefined) {
        
        panier[uniqueKey][0]++; 
    } else {
        
        var prix = parseFloat(document.getElementById('price' + item_id).innerHTML);
        var nom = document.getElementById("aa" + item_id).innerHTML;
        panier[uniqueKey] = [1, nom, prix, imageUrl, color, size];

        alert("Article ajouté avec succès")
        
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