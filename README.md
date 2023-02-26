<h1 align="center">
  Riot-auth
</h1>

<p align="center">
  Riot-auth is a example to get around riots cloudflare
</p>

<p align="center">
  <a href="https://kook.top/gpbTwZ">🌌・Kook</a></br>
  <img src="https://img.shields.io/github/stars/musnows/Riot-auth?style=social"> </a>
  <img src="https://img.shields.io/github/watchers/musnows/Riot-auth?style=social"> </a>
</p>

<h2 align="center">
  PLease  leave a like and follow

  Now supporting cookie reauth!
</h2>

---

<h3 align="center">
Here is an example of 2fa user with wrong verfiy code enter.

The access_token & Entitlements has been changed for security.
</h3>

```
[start test]
[EzAuth] 2fa user
{'status': False, 'auth': <EzAuth.EzAuth object at 0x7fc97cfe9f00>, '2fa_status': True}
input vcoode: 166729
verify code err, enter again
input vcoode: 166728
==================================================
Accestoken: eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJwcCI6eyJjIjoiYXMifSwic3ViIjoiNzc2NDg5NzktYzZkNS01ZmQ1LTk0MTgtNDEzMGEyNWVlYmYyIiwic2NwIjpbIm9wZW5pZCIsImxpbmsiLCJiYW4iLCJsb2xfcmVnaW9uIiwibG9sIiwic3VtbW9uZXIiLCJvZmZsaW5lX2FjY2VzcyJdLCJjbG0iOlsibG9ssbCwibG5rIjpbXSwiYyI6ImVjMSIsImxpZCI6IkwwV0c1aHZrbEluQ1VSVjE5bHRCV3cifSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJpb3RnYW1lcy5jb20iLCJleHAiOjE2Nzc0MTA1NzIsImlhdCI6MTY3NzQwNjk3MiwianRpIjoiN2FaSEV4TTZLcVEiLCJjaWQiOiJyaW90LWNsaWVudCJ9.SfYYtciCuhSg5sT6dChXFYJ01mDZL3ROc_x4L41YDvTDl5zFhMVKUCk_tCpH0g4MjoN2l_EZzGsmY2Ov-fBX4h4M-EaPIUWbXOAWmpmwIMwNJPRHEOah6u53dBtlZpAzSNqvtCu13cG5UwAz1n_0Odv4ck5bUoh_DI
--------------------------------------------------
Entitlements: eyJraWQiOiJrMSIsImFsZyI6IlJTMjU2In0.eyJlbnRpdGxlbWVudHMiOltdLCJhdF9oYXNoIjoieUFMSERxS0c4aDEwbmdNSG1jNFpxUSIsInN1YiI6IlbWVudHMuYXV0aC5yaW90Z2FtZXMuY29tIiwiaWF0IjoxNjc3NDA2OTczLCJqdGkiOiI3YVpIRXhNNktxUSJ9.yFHdcy_4PDgYujkz105DEp9idqHAoyvDVvLjllrtTPd-FtFFtrKo9BrnLtr3qfNJ-VACFh6o3vknPHPYVoUnQEIYkJhZwbZixj5xNyKcIQwLz0YK-MLqwU9qmiUyanNxKuq4ilshJ4UBstxuCbTznL63QLekmXQu4pLtPjTapu-EkufAKO1_0PhxEslXyJ2uxvEGZGGAvO7bfYriRF5UhrSfUyij-q4FAql-upw9o1jGmEyuf4pykWBs7v7iRbXbeTCnxL1cIMvBA
--------------------------------------------------
Userid: 77648979-c6d5-5fd5-9418-4130a25eebf2
--------------------------------------------------
Region: ap
--------------------------------------------------
Name: TB231D#1132
--------------------------------------------------
Createdat: 2022-07-28 05:15:04
--------------------------------------------------
Bantype: None
==================================================
[try to reauth]
==================================================
Accestoken: eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJwcCI6eyJjIjoiYXMifSwic3ViIjoiNzc2NDg5NzktYzZkNS01ZmQ1LTk0MTgtNDEzMGEyNWVlYmYyIiwic2NwIjpbIm9wZW5pZCIsImxpbmsiLCJiYW4iLCJsb2xfcmVnaW9uIiwibG9sIiwic3VtbW9uZXIiLCJvZmZsaW5lX2FjY2VzcyJdLCJjbG0iOlsibG9sX2FjY291bnQiLCJlbWFpbF92ZXJpZmllZCIsIm9wZW5pZCIsInB3IiwibG9sIiwib3JpZfYWNjb3VudF9pZCIsImFjY3QiLCJ1c2VybmFtZSJdLCJkYXQiOnsicCI6bnVsbCwiYyI6ImVjMSIsImxpZCI6IkwwV0c1aHZrbEluQ1VSVjE5bHRCV3cifSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJpb3RnYW1lcy5jb20iLCJleHAiOjE2Nzc0MTA1NzUsImlhdCI6MTY3NzQwNjk3NSwianRpIjoiU05yTFlqd21sOW8iLCJjaWQiOiJyaW90LWNsaWVudCJ9.eLIvmFMDUYgIRknc-AiLBRyTN51oXCX2o
--------------------------------------------------
Entitlements: eyJraWQiOiJrMSIsImFsZyI6IlJTMjU2In0.eyJlbnRpdGxlbWVudHMiOltdLCJhdF9oYXNoIjoiVTRaSWxGSTMzRWMtQXNScTRVS1dPZyIsInN1YiI6Ijc31LCJqdGkiOiJTTnJMWWp3bWw5byJ9.Ta6aPmIH9-rHV0AHJKsyUFlnH-iw3QKdsXjp--KHwDpfPmrZuhQEGVejjRjr0vG4vt9K1Q3pMAAvBNMb3UfGZYxK_E5TGGkITZWfbyEOyTIrEWxvrgePu7WXVj47BSvy8YaefEBps0xehgGhBm0Be2RPIfbTsEBTk1Iqpib-p-2scJe51nAdzWh42thduIZ0X6xQSgmwrtE23jhZbc81n57nlFUhJzChCuzjWBRLrckVQijkX8OTdS-q6o_PPjMHjyu4ssb1XX_KVQWxjw
--------------------------------------------------
Userid: 77648979-c6d5-5fd5-9418-4130a25eebf2
--------------------------------------------------
Region: ap
--------------------------------------------------
Name: TB231D#1132
--------------------------------------------------
Createdat: 2022-07-28 05:15:04
--------------------------------------------------
Bantype: None
==================================================
```