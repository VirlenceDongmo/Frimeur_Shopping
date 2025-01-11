
function AfficherList(panier){
    var panierString = ""
    panierString += "<h5>Voici votre liste d'articles sélectionnés :</h5>"
    var index = 1
    for(var x in panier){
        panierString += "Article " + index + " :"
        panierString += document.getElementById("aa"+x).innerHTML + " :"+ " Quantité = " + panier[x][0] + "</br>"
        index++
    }

    panierString += "<a href='/checkout' class='btn btn-primary'>Voir le panier</a>"

    $('[data-toggle="popover"]').popover()
    document.getElementById("panier").setAttribute('data-content', panierString)
}