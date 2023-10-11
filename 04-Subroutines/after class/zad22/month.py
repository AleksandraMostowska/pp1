def month(n) -> str:
    if n < 1 or n > 12:
        raise ValueError("Wrong input")
    
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    return months[n - 1]