import datetime


# Зберігає інформацію про баланс кошельків
wallet = {"USD": 1000, "EUR": 900, "UAH": 25000}

# Зберігає курси конвертації до UAH
exchange_rates_uah = {"USD": 41.3, "EUR": 43.9, "UAH": 1.0}

# Лог для відстеження операцій
transactions = []


def add_currency(currency, amount):
    """Додає валюту в кошелек або оновлює її баланс."""
    if currency in wallet:
        wallet[currency] += amount
    else:
        wallet[currency] = amount
        
        # add exchange_rates_uah for new currency
        
    log_transaction(f"Added {amount} {currency} to wallet.")

    
    
def convert_currency(from_currency, to_currency, amount):
    """Конвертує суму з однієї валюти в іншу за заданими курсами."""
    if from_currency not in wallet or wallet[from_currency] < amount:
        print("Insufficient funds or invalid currency.")
        return
    
    if from_currency not in exchange_rates_uah or to_currency not in exchange_rates_uah:
        print("Exchange rate for the currency is missing.")
        return  
    
    coefficient_currency = exchange_rates_uah[from_currency] / exchange_rates_uah[to_currency] 
    converted_amount = round(amount * coefficient_currency, 2) 
    
    wallet[from_currency] -= amount
    wallet[to_currency] += converted_amount
    log_transaction(f"Converted {amount} {from_currency} to {converted_amount:.2f} {to_currency}. ")
    log_transaction(f"New balances: {from_currency}: {wallet[from_currency]}, {to_currency}: {wallet[to_currency]}.")
    
   
def display_wallet():
    """Виводить баланс всіх кошельків."""
    print("\nBallance of wallet:")
    for key, value in wallet.items():
        print(f"{key}: {value}")    
    

def log_transaction(description):
    """Логує транзакцію з відміткою часу."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_info = f"[{timestamp}] - {description}"
    transactions.append(log_info)
    print("---", log_info)
    
   

def display_transactions(count=0):
    """Виводить історію транзакцій."""
    print("\nAll transactions")
    last_transact = transactions[::-1]
    
    for tr in last_transact:
        print(tr)
   

def reset_wallet():
    """ Скидає всі баланси кошельків."""
    for currency in wallet.keys():
        wallet[currency] = 0
    log_transaction("All wallets have been reset")
    
# ============================================


def main_process():
    """
    Імплементація функціоналу спілкування з користувачем
    """
    while True:        
        print("\nChoose an option:")
        print("1. Add currency")
        print("2. Convert currency")
        print("3. Display wallet")
        print("4. Display transactions")
        print("5. Reset wallet")
        print("0. Exit")

        choice = input("Enter your choice: ") #5
        
        match choice:
            case "1":
                currency = input("Enter the currency (USD, EUR, UAH): ").upper()
                amount = float(input("Enter the amount to add: "))                
                add_currency(currency, amount)
            
            case "2":
                from_currency = input(f"Enter the currency to convert from {list(wallet.keys())}: ").upper()
                to_currency = input(f"Enter the currency to convert to {list(wallet.keys())}: ").upper()
                amount = float(input(f"Enter the amount of {from_currency} to convert: "))

                convert_currency(from_currency, to_currency, amount)  
            
            case "3":   
                display_wallet()
        
            case "4":
                count = "how trasactions show? (0 = all) "
                display_transactions(count = count)
            
            case "5":
                reset_wallet()
                
            case "0":
                print("Exit")
                break
            
            case _:
                print("Error. Try again")

def main_process_2():
    """
    Імплементація функціоналу спілкування з користувачем
    """
    print("\nChoose an option:")
    print("1. Add currency")
    print("2. Convert currency")
    print("3. Display wallet")
    print("4. Display transactions")
    print("5. Reset wallet")
    print("0. Exit")

    choice = input("Enter your choice: ") 
    
    if choice == "1":
        ...
        
    elif choice == "2":
        ...        
    
    elif choice == "3":
        ...
    
    elif choice == "4":
        ...
            
    elif choice == "5":
        ...
            
    elif choice == "0":
        ...
        
    else:
        ...



def test():
    # Зберігає інформацію про баланс кошельків
    wallet = {"USD": 1000, "EUR": 900, "UAH": 25000}

    # Зберігає курси конвертації до UAH
    exchange_rates_uah = {"USD": 41.3, "EUR": 43.9, "UAH": 1.0}

    print(wallet)
    convert_currency("EUR", "USD", 100)
    print("*"*25)
    print(wallet)
    
    
# test()

main_process()
