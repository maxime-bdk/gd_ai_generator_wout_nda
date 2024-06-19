import sys
import time
import asyncio
from pprint import pprint
from ndaclient import AsyncNDAClient, NDAClient

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
nda = 'nda'
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python connection.py <input_file>")
        sys.exit(1)
    generated_code = sys.argv[1]

async def main():
    async with AsyncNDAClient('nda', 'nda', 'nda') as client:
        # Algorithm creation
            "I can't show it to you due to the nda, but here was just some json request"


        #Algorithm updating
        await client.update_object(nda, values={'COMPILED_CODE': generated_code })
        
        answer = await client.eval_alg(nda)
        print(answer)
        
        #Algorithm deleting
        await client.delete_object(nda)

        return answer

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
