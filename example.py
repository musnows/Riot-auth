# a example for EzAuth
from EzAuth import EzAuth,EzAuthExp
import asyncio,traceback

auth = EzAuth()

async def auth_test(account,passwd):
    try:
        res = await auth.authorize(account,passwd)
        print(res)
        if not res['status']: # err, 2fa
            while True:
                try:
                    vcode = input("input vcoode: ")
                    await auth.email_verfiy(vcode)
                    break
                except EzAuthExp.MultifactorError as result:
                    if "multifactor_attempt_failed" in str(result):
                        print("verify code err, enter again")
                        continue
                    else:
                        raise result
                
        auth.print()

    except:
        traceback.print_exc()

async def reauth_test():
    try:
        await auth.reauthorize()
        auth.print()
    except:
        traceback.print_exc()

# set your riot account and passwd
print("[start test]")
asyncio.run(auth_test(account="",passwd=""))
print("[try to reauth]")
asyncio.run(reauth_test())