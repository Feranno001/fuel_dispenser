import time
def main():
    petrol_price = 150
    gas_price = 1400
    kerosene_price = 200
    diesel_price = 250
    customer_amount = 50000

    print('Welcome to Ferano filling station\nPLEASE WAIT.......')



    def start():
        time.sleep(2)
        mainchoose = ('Menu\n______\n1 for Petrol\n2 for Gas\n3 for Kerosine\n4 for Diesel\n')
        print(mainchoose)
        print('select 1 for fuel\nselect 2 for Gas\nselect 3 for Kerosene\nselect 4 for Diesel\n')
        choose = input('     choose your choice from above\n   ____________________________________\n1)enter your choise: ')
        if choose == '1' and choose.isdigit():
            def petrol():
                print('\n     Litre or Cash\n    ______________\n1)Litre\n2)Cash\n   ____________\nchoose 1 for litre and 2 for cash')
                try:
                    choose_l_or_c = int(input('choose one above: '))

                    if choose_l_or_c == 1:
                        petrol_litre = int(input('\n1)How many litres: '))
                        if customer_amount > petrol_price * petrol_litre:
                            if petrol_litre < customer_amount / petrol_price:
                                time.sleep(2)
                                print('\n     Successful\n    ______________')
                                print('Petrol price: ' + str(petrol_price * petrol_litre))
                                print('Balance:' + str(customer_amount - petrol_price * petrol_litre))
                                print('Thanks for your patronage')
                                var = input('')
                                if var == '':
                                    pass
                                return main()

                            else:
                                print('\nWARNING: insufficient fund')
                                time.sleep(2)
                                return petrol()

                    elif choose_l_or_c == 2:
                        fuel_price = float(input('enter amount of petrol: '))
                        if customer_amount > fuel_price:
                            time.sleep(2)
                            print('\n     Successful\n    ______________')
                            print('Amount_litre: ' + str(fuel_price/petrol_price))
                            print('Price: ' +str(fuel_price))
                            print('Balance:' + str(customer_amount - fuel_price))
                            print('Thanks for your patronage')
                            var = input('')
                            if var == '':
                                pass
                            return main()

                    else:
                        print('\nWARNING: incorrect entry of number\n')
                        time.sleep(2)
                        return petrol()
                except:
                    print('\nWARNING: enter a corresponding input\n')
                    time.sleep(2)
                    return petrol()

            petrol()
        elif choose == '2' and choose.isdigit():
            def gas():
                kgs = '\n     Available kgs:\n   _______\n1)1kg\n2)2kg\n3)3kg\n4)4kg\n5)5kg\n'
                print(kgs)
                try:
                    choose_desired_kg = int(input('How many kg do you wanna buy:  '))
                    if customer_amount > choose_desired_kg * gas_price and choose_desired_kg <= 5:
                        time.sleep(2)
                        print('\n    Successful\n    ______________')
                        print('gas price:' + str(choose_desired_kg * gas_price))
                        print('Balance:' + str(customer_amount - choose_desired_kg * gas_price))
                        print('Thanks for your patronage')
                        var = input('')
                        if var == '':
                            pass
                        return main()
                    else:
                        print('\nWARNING: incorrect entry of number\n')
                        time.sleep(2)
                        return gas()
                except:
                    print('\nWARNING: enter a corresponding input\n')
                    time.sleep(2)
                    return gas()
            gas()
        elif choose == '3' and choose.isdigit():
            def kerosene():
                print('\n     Litre or Cash\n    ______________\n1)Litre\n2)Cash\n   ____________\nchoose 1 for litre and 2 for cash')
                try:
                    select_l_or_c = int(input('choose one above: '))

                    if select_l_or_c == 1:
                        kerosene_litre = int(input('\n1)How many litres: '))
                        if customer_amount > kerosene_price * kerosene_litre:
                            time.sleep(2)
                            print('\n     Successful\n    ______________')
                            print('\nKerosene price: ' + str(kerosene_price * kerosene_litre))
                            print('Balance:' + str(customer_amount - kerosene_price * kerosene_litre))
                            print('Thanks for your patronage')
                            var = input('')
                            if var == '':
                                pass
                            return main()

                    elif select_l_or_c == 2:
                        kerosene_prices = float(input('enter amount of kerosene: '))
                        if customer_amount > kerosene_prices:
                            time.sleep(2)
                            print('\n     Successful\n    ______________')
                            print('Amount_litre: ' + str(kerosene_prices / kerosene_price))
                            print('Price: ' + str(kerosene_prices))
                            print('Balance:' + str(customer_amount - kerosene_prices))
                            print('Thanks for your patronage')
                            var = input('')
                            if var == '':
                                pass
                            return main()

                    else:
                        print('\nWARNING: incorrect entry of number\n')
                        time.sleep(2)
                        return kerosene()

                except:
                    print('\nWARNING: enter a corresponding input\n')
                    time.sleep(2)
                    return kerosene()
            kerosene()
        elif choose == '4' and choose.isdigit():
            def diesel():
                print('\n     Litre or Cash\n    ______________\n1)Litre\n2)Cash\n   ____________\nchoose 1 for litre and 2 for cash')
                try:
                    pick_l_or_c = int(input('choose one above: '))

                    if pick_l_or_c == 1:
                        diesel_litre = int(input('\n1)How many litres: '))
                        if customer_amount > diesel_price * diesel_litre:
                            time.sleep(2)
                            print('\n     Successful\n    ______________')
                            print('\nKerosene price: ' + str(diesel_price * diesel_litre))
                            print('Balance:' + str(customer_amount - diesel_price * diesel_litre))
                            print('Thanks for your patronage')
                            var = input('')
                            if var == '':
                                pass
                            return main()

                    elif pick_l_or_c == 2:
                        diesel_prices = float(input('enter amount of diesel: '))
                        if customer_amount > diesel_prices:
                            time.sleep(2)
                            print('\n     Successful\n    ______________')
                            print('Amount_litre: ' + str(diesel_prices / diesel_price))
                            print('Price: ' + str(diesel_prices))
                            print('Balance:' + str(customer_amount - diesel_prices))
                            print('Thanks for your patronage')
                            var = input('')
                            if var == '':
                                pass
                            return main()

                    else:
                        print('\nWARNING: incorrect entry of number\n')
                        time.sleep(2)
                        return diesel()

                except:
                    print('\nWARNING: enter a corresponding input\n')
                    time.sleep(2)
                    return diesel()

            diesel()
        else:
            print('\nWARNING: enter related input\n')
            return start()
    start()
main()