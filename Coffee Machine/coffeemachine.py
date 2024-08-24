from prettytable import PrettyTable

if __name__ == '__main__':
    table = PrettyTable()
    table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmender"])
    table.add_column("Ability",["fire","fire","rain"])
    table.align="l"
    print(table.get_string())