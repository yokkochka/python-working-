#!/usr/bin/env python3
from give import sudoku
import random
import time
import asyncio
import sys
import os

TL = 300
IP = os.getenv("HOST") if "HOST" in os.environ else "127.0.0.1"
PORT = int(os.getenv("PORT")) if "PORT" in os.environ else 4848
FLAG = os.getenv("FLAG") if "FLAG" in os.environ else "VKCTF{ph4k3_fl49}"

async def die(writer, check):
    writer.write(b"WRONG ANSWER!\n")
    print("Died at {}".format(check))
    await writer.drain()
    writer.close()

async def handle_requests(reader, writer):
    s = sudoku()
    addr = writer.get_extra_info("peername")
    print("[+] Got connection from {}".format(addr))
    GREETING = "Hello! Please solve this sudoku challenge go get flag. \nNotice that alphabet is '{}'. \nIf given sudoku is impossible, restart the challenge. \nChecker will accept any possible answer that satisfies sudoku rules. \nProvide answer in a format like challenge was given. \nGood luck!".format(s.chars)
    writer.write(bytes(GREETING, encoding="utf-8"))
    await writer.drain()

    s.fill(random.randint(400, 500))

    writer.write(b"\n")
    await writer.drain()
    print("started writing sudoku")
    for i in range(32):
            writer.write(bytes("".join([s.get(j, i) for j in range(32)]), encoding="utf-8") + b"\n")
            await writer.drain()
    print("finished writing sudoku")

    answer = []
    for i in range(32):
        line = await reader.readline()
        answer.append(line.decode("utf-8").strip())
        #except:
        #    await die(writer, 1)

    print(answer)

    #validate input
    for line in answer:
        if '*' in line:
            await die(writer, 2)
        if len(line)!=32:
            await die(writer, 3)
        for char in line:
            if char not in s.chars:
                await die(writer, 4)
    
    #check initial state
    for i in range(32):
        for j in range(32):
            if s.get(j, i) != answer[i][j] and s.get(j, i) != '*':
                await die(writer, 5)
    
    #check conditions(lines)
    for i in range(32):
        if len(list(set(answer[i]))) != 32:
            await die(writer, 6)
        if len(list(set([answer[j0][i] for j0 in range(32)]))) != 32:
            await die(writer, 7)
    #check conditions(squares)
    for i in range(16):
        xinit = (i%4)*8
        yinit = (i//4)*8
        if len(list(set([answer[i][j] for i in range(yinit, yinit+8) for j in range(xinit, xinit+8)]))) != 64:
            await die(writer, 8)
    
    
    writer.write(bytes("WOW, AWESOME {}\n".format(FLAG), encoding="utf-8"))
    await writer.drain()

    await writer.close()
    
loop = asyncio.get_event_loop()
if sys.version_info.minor < 10:
    coro = asyncio.start_server(handle_requests, IP, PORT, loop=loop)
else:
    coro = asyncio.start_server(handle_requests, IP, PORT)
server = loop.run_until_complete(coro)

print("Serving on {}".format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
