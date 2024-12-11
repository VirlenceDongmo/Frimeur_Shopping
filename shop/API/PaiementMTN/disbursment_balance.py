from apiDePaiement import PayClass


#Transfer money from disbursement account
withdrawmoney = PayClass.withdrawmtnmomo('200', 'EUR', 'bravo', '237654158175', 'cheers')

print(withdrawmoney["response"])
