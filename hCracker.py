import hashlib

def crack_hash_from_file(target_hash, wordlist_path, algorithm_type):
    # setting the input to lower case
    algo = algorithm_type.lower()
    
    print(f"[*] Target Hash: {target_hash}")
    print(f"[*] Algorithm: {algo}")
    print(f"[*] Wordlist: {wordlist_path}")
    print("-" * 40)

    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                password = line.strip()
                
                # creating the hash in one place
                if algo == "md5":
                    hashed_pass = hashlib.md5(password.encode()).hexdigest()
                elif algo == "sha-256" or algo == "sha256":
                    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
                else:
                    print("[!] Invalid algorithm type. Use 'md5' or 'sha-256'.")
                    return # leaving the function

                if hashed_pass == target_hash:
                    print(f"\n[+] Password Found: {password}")
                    return
                
                print(f"Trying: {password}...", end="\r")

        print("\n[-] Password not found in the wordlist.")

    except FileNotFoundError:
        print(f"[!] Error: The file '{wordlist_path}' was not found.")

print('''

██╗  ██╗ █████╗ ███████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║
███████║███████║███████╗███████║
██╔══██║██╔══██║╚════██║██╔══██║
██║  ██║██║  ██║███████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
      
[ repo : https://github.com/White20devilera/Cyb-weapons-lab ]  
      
''')

print()

# Inputs
algorithm = input("Enter the algorithm type (md5 / sha-256) : ").strip()
target = input("Enter the hash : ").strip()
wordlist = input("Enter the path to your wordlist (e.g., passwords.txt) : ").strip()

print("")

crack_hash_from_file(target, wordlist, algorithm)

