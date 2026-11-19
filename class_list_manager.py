# Class List Manager - Group 7
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# Written by: Nourah Alhazzani
def search_name(names, name):
    if name in names:
        return True
    else:
        return False

# Written by: Lamia Al-sultan
def sort_names(names):
    return sorted(names)

# Written by: Jory Al-subaie
def count_names(names):
    return len(names)
    
# Written by: Ghala Alamri
def names_starting_with(names, letter):
    result = []

    for name in names:
        if name.lower().startswith(letter.lower()):
            result.append(name)

    return result


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Sorted names:", sort_names(names))
    print("Number of names:", count_names(names))
    print("Names starting with L:", names_starting_with(names, "L"))
    print("Search for Noura:", search_name(names, "Noura"))

main()
