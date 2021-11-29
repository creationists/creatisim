def reformation(text):
    data = repr(text).split('\\n')
    print(data)
    new_dic = {}
    for line in data :
        print(line)
        print('---------')
        key = line.split(':')[0].strip()
        item = line.split(':')[1].strip()
        new_dic.update({key : item})
    pp(new_dic)
        

text = """Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: ko-KR,ko;q=0.9
Connection: keep-alive
Content-Length: 39
Content-Type: application/x-www-form-urlencoded
Cookie: _tmp_vid=89d9f6e302cae9; _ga=GA1.2.1763194143.1637721394; _gid=GA1.2.1307223138.1637721394; _gat_gtag_UA_136712386_1=1; ch-veil-id=6ac47447-d91d-4679-a23c-19ef32768835; ch-session-18876=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiIxODg3Ni02MTlkYTUzNDIxNjQ4ZTRhNjFlYyIsImlhdCI6MTYzNzcyMTM5NiwiZXhwIjoxNjQwMzEzMzk2fQ.ikqN44A1vphppgSwlXYGVYxiyjCSnXJp1ix4Cf4YXJU; amp_752e71=L5fUOxAhwyBjp0nWIunuS3...1fl7sqhqc.1fl7sraed.5.0.5; _ga_PHL0WGSFWB=GS1.1.1637721393.1.1.1637721419.0
Host: api.itemscout.io
Origin: https://itemscout.io
Referer: https://itemscout.io/
sec-ch-ua: "Chromium";v="91", " Not;A Brand";v="99"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"""
reformation(text)