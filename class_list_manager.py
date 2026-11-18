# Class List Manager - Group 7
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====
# Written by: Lamia Al-sultan
def sort_names(names):
    return sorted(names)

# Written by: Jory Al-subaie
def count_names(names):
    return len(names)



def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Sorted names:", sort_names(names))
    print("Number of names:", count_names(names))

main()
