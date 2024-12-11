from apiDePaiement import PayClass

callPay = PayClass.momopay('50', 'EUR','1234test199','237654158175', 'Commande réussie')

#Verify the transaction

if callPay['response'] == 200 or callPay['response'] == 202 :
    verify = PayClass.verifymomo(callPay['ref'])
    print(verify)
    if verify['status'] == 'SUCCESSFUL':
        print('Merci pour votre confiance')
    else :
        print("La transaction a échoué veuillez rééssayer")
else :
    print("ther was a problem making a transaction")