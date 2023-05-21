#
import requests
import json

def print_res(resp):
  print(resp.status_code)
  if 'application/json' in resp.headers['Content-Type']:
    print(resp.json())
  else:
    print(resp.text)


status = 'available'
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}',
                   headers={'accept':'application/json'})
print_res(res)

petId = 125
new_pet = {"id": petId,
  "category": {
    "id": petId,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": petId,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.post(f'https://petstore.swagger.io/v2/pet',
                   headers={'accept':'application/json', 'Content-Type':'application/json'},
                   data=json.dumps(new_pet))

print_res(res)

updated_pet = new_pet
updated_pet["name"] = "Bobbie"

res = requests.put(f'https://petstore.swagger.io/v2/pet',
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                   data=json.dumps(updated_pet))

print_res(res)

res = requests.delete(f'https://petstore.swagger.io/v2/pet/{petId}',
                     headers={'accept': 'application/json'})
print_res(res)



