from stats import Statistics

def main():
    statistics = Statistics()
    statistics.add()
    statistics.add()
    statistics.add()
    print(statistics)
    
    s2 = Statistics([12, 37, 6, 9, 17])
    print(s2)
    s2.add()
    print(s2)
    s2.display_stats()

if __name__ == "__main__":
    main()