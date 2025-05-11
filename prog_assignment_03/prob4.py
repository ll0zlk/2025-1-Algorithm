class Node:
    def __init__(self, person):
        self.person = person
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, person):
        self.root = self._insert(self.root, person)
        return True

    def _insert(self, node, person):
        if node is None:
            return Node(person)
        if person['name'] < node.person['name']:
            node.left = self._insert(node.left, person)
        else:
            node.right = self._insert(node.right, person)
        return node

    def find(self, name):
        return self._find(self.root, name)

    def _find(self, node, name):
        if node is None:
            return None
        if name == node.person['name']:
            return node.person
        elif name < node.person['name']:
            return self._find(node.left, name)
        else:
            return self._find(node.right, name)

    def delete(self, name):
        if self.find(name) is None:
            return False
        self.root = self._delete(self.root, name)
        return True

    def _delete(self, node, name):
        if node is None:
            return None
        if name < node.person['name']:
            node.left = self._delete(node.left, name)
        elif name > node.person['name']:
            node.right = self._delete(node.right, name)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            succ = self._min(node.right)
            node.person = succ.person
            node.right = self._delete(node.right, succ.person['name'])
        return node

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    def trace(self, name):
        path = []
        node = self.root
        while node:
            path.append(node.person['name'])
            if name == node.person['name']:
                return path
            elif name < node.person['name']:
                node = node.left
            else:
                node = node.right
        return []

    def list_all(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.person)
            self._inorder(node.right, result)

def load(filename):
    tree = BST()
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()[1:]
            for line in lines:
                fields = line.strip().split('\t')
                if len(fields) < 6:
                    continue
                person = {
                    'name': fields[0],
                    'company': fields[1],
                    'address': fields[2],
                    'zip': fields[3],
                    'phone': fields[4],
                    'email': fields[5]
                }
                tree.insert(person)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return tree

def save(filename, people):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("name\tcompany\taddress\tzip\tphone\temail\n")
        for p in people:
            f.write(f"{p['name']}\t{p['company']}\t{p['address']}\t{p['zip']}\t{p['phone']}\t{p['email']}\n")

def main():
    tree = load('address_book2020.tsv')
    while True:
        command = input('$ ').strip()
        if command.startswith('find '):
            name = command[5:]
            person = tree.find(name)
            if person:
                print(f"{person['name']}")
                print(f"Company: {person['company']}")
                print(f"Address: {person['address']}")
                print(f"Zipcode: {person['zip']}")
                print(f"Phones: {person['phone']}")
                print(f"Email:\n{person['email']}")
            else:
                print("Not found.")
        elif command.startswith('trace '):
            name = command[6:]
            path = tree.trace(name)
            if path:
                for p in path:
                    print(p)
            else:
                print("Not found.")
        elif command.startswith('delete '):
            name = command[7:]
            if tree.delete(name):
                print(f"{name} was deleted.")
            else:
                print("Not found.")
        elif command.startswith('add '):
            name = command[4:]
            if tree.find(name):
                print("Name already exists.")
                continue
            company = input("Company? ").strip()
            address = input("Address? ").strip()
            zipcode = input("Zipcode? ").strip()
            phone = input("Phones? ").strip()
            email = input("Email? ").strip()
            person = {
                'name': name,
                'company': company,
                'address': address,
                'zip': zipcode,
                'phone': phone,
                'email': email
            }
            if tree.insert(person):
                print(f"{name} was successfully added.")
        elif command.startswith('list'):
            for person in tree.list_all():
                print(f"{person['name']}\t{person['company']}\t{person['address']}\t{person['zip']}\t{person['phone']}\t{person['email']}")
        elif command.startswith('save '):
            filename = command[5:]
            save(filename, tree.list_all())
            print(f"Saved to {filename}.")
        elif command == 'exit':
            break
        else:
            print("Unknown command.")

if __name__ == '__main__':
    main()