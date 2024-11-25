# Зберігає інформацію про баланс кошельків
wallet = {"USD": 1000, "EUR": 900, "UAH": 25000}

# Зберігає курси конвертації до UAH
exchange_rates_uah = {"USD": 41.3, "EUR": 43.9, "UAH": 1.0}

# Лог для відстеження операцій
transactions = []


def add_currency(currency, amount):
    """Додає валюту в кошелек або оновлює її баланс."""
    
    
def convert_currency(from_currency, to_currency, amount):
    """Конвертує суму з однієї валюти в іншу за заданими курсами."""
   

def display_wallet():
    """Виводить баланс всіх кошельків."""
    

def log_transaction(description):
    """Логує транзакцію з відміткою часу."""
   

def display_transactions(last=True, count=3):
    """Виводить історію транзакцій."""
   

def reset_wallet():
    """ Скидає всі баланси кошельків."""
    
# ============================================


def main_process():
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
        