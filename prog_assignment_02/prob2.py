def read(filename):
  info = []
  with open(filename, 'r') as f:
    for line in f:
      addrs = [addr.strip() for addr in line.strip().split('|')]
      addr_info = {
        'name' : addrs[0],
        'company' : addrs[1],
        'address' : addrs[2],
        'zipcode' : addrs[3],
        'phones' : addrs[4],
        'email' : addrs[5]
      }
      info.append(addr_info)
  return info

def sorting(info, key):
  return sorted(info, key=lambda x: x[key])

def printing(info):
  for i in info:
        print(f"{i['name']}")
        print(f"Company: {i['company']}")
        print(f"Address: {i['address']}")
        print(f"Zipcode: {i['zipcode']}")
        print(f"Phones: {i['phones']}")
        print(f"Email: {i['email']}")
        print()

info = []

while True:
  command = input("$ ")
  if command.startswith("read "):
    filename = command.split()[1]
    info = read(filename)
  elif command.startswith("sort -"):
    key = command.split('-')[1]
    info = sorting(info, key)
  elif command == "print":
    printing(info)
  elif command == "exit":
    break
  else:
    print("알 수 없는 명령입니다.")