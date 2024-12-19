


        if(localStorage.getItem('panier') == null){
            var panier = {}
        }else{
            panier = JSON.parse(localStorage.getItem('panier'));
        }
        $(document).on('click','.ted', function(){
            console.log('devhack');
            var item_id = this.id.toString()
            console.log(item_id)
            if(panier[item_id] != undefined){
                quantite = panier[item_id][0] + 1 
                panier[item_id][0] = quantite
                panier[item_id][2] += parseFloat(document.getElementById('price'+item_id).innerHTML)
            }else{
                quantite = 1
                prix = parseFloat(document.getElementById('price'+item_id).innerHTML)
                nom = document.getElementById("aa"+item_id).innerHTML
                panier[item_id] = [quantite, nom, prix]
            }
            console.log(panier)
            localStorage.setItem('panier', JSON.stringify(panier))
            document.getElementById("panier").innerHTML = "Panier = " + Object.keys(panier).length
        });
        
        AfficherList(panier)

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