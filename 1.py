class HashTableChaining:
    def _init_(self, size):
        self.size = size
        self.table = [] # Initialize an empty list
        for _ in range(size):
            self.table.append([]) # Append an empty list for each index
        self.comparisons = 0 # Track comparisons

    def hash_function(self, key):
        return key % self.size # Simple modulo-based hash function

    def insert(self, key):
        self.comparisons = 0 # Reset comparison count
        index = self.hash_function(key)
        self.comparisons += 1 # One comparison for hash function
        self.table[index].append(key) # Insert key into the appropriate list

    def search(self, key):
        self.comparisons = 0 # Reset comparison count
        index = self.hash_function(key)
        self.comparisons += 1 # One comparison for hash function
        if key in self.table[index]:
            self.comparisons += len(self.table[index]) # Count comparisons for searching in the chain
            return True # Key found
        return False # Key not found

    def delete(self, key):
        self.comparisons = 0 # Reset comparison count
        index = self.hash_function(key)
        self.comparisons += 1 # One comparison for hash function
        if key in self.table[index]:
            self.comparisons += len(self.table[index]) # Count comparisons for searching in the chain
            self.table[index].remove(key) # Remove key from the list
            return True
        return False

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")
        print(f"Total comparisons: {self.comparisons}")

class HashTableLinearProbing:
    def _init_(self, size):
        self.size = size
        self.table = [None] * size # Initialize an empty list for linear probing
        self.comparisons = 0 # Track comparisons

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        self.comparisons = 0 # Reset comparison count
        index = self.hash_function(key)
        self.comparisons += 1 # One comparison for hash function
        for i in range(self.size):
            new_index = (index + i) % self.size
            self.comparisons += 1 # Count comparisons during probing
            if self.table[new_index] is None: # Found an empty slot
                self.table[new_index] = key
                return
        print("Hash table is full! Cannot insert new entry.")

    def search(self, key):
        self.comparisons = 0 # Reset comparison count
        index = self.hash_function(key)
        self.comparisons += 1 # One comparison for hash function
        for i in range(self.size):
            new_index = (index + i) % self.size
            self.comparisons += 1 # Count comparisons during probing
            if self.table[new_index] is None: # Empty slot means the key is not in the table
                return False
            if self.table[new_index] == key: # Key found
                return True
        return False

    def delete(self, key):
        self.comparisons = 0 # Reset comparison count
        index = self.hash_function(key)
        self.comparisons += 1 # One comparison for hash function
        for i in range(self.size):
            new_index = (index + i) % self.size
            self.comparisons += 1 # Count comparisons during probing
            if self.table[new_index] == key:
                self.table[new_index] = None # Remove the key from the table
                return True
        return False

    def display(self):
        for i, key in enumerate(self.table):
            print(f"Index {i}: {key if key is not None else 'Empty'}")
        print(f"Total comparisons: {self.comparisons}")

class TelephoneDirectory:
    def _init_(self, size, method):
        self.size = size
        self.method = method
        if method == 'chaining':
            self.table = HashTableChaining(size)
        elif method == 'linear_probing':
            self.table = HashTableLinearProbing(size)
        else:
            raise ValueError("Invalid method. Choose either 'chaining' or 'linear_probing'.")

    def insert(self, key):
        self.table.insert(key)

    def search(self, key):
        return self.table.search(key)

    def delete(self, key):
        return self.table.delete(key)

    def display(self):
        self.table.display()

def main():
    # User chooses between Chaining or Linear Probing
    method = input("Choose Hashing Method (chaining/linear_probing): ").strip().lower()
    size = int(input("Enter the size of the table: "))
    directory = TelephoneDirectory(size, method)
    
    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            key = int(input("Enter key to insert: "))
            directory.insert(key)
        elif choice == 2:
            key = int(input("Enter key to search: "))
            result = directory.search(key)
            print(f"Key {'found' if result else 'not found'}")
        elif choice == 3:
            key = int(input("Enter key to delete: "))
            result = directory.delete(key)
            print(f"Key {'deleted' if result else 'not found'}")
        elif choice == 4:
            directory.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice! Try again.")

if _name_ == "_main_":
    main()
