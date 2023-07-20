import http.client

conn = http.client.HTTPSConnection("planninglabs.carto.com")

for i in range(5):
    print(f"Getting file #{i+1}!")
    payload = ""
    conn.request("GET", f"/api/v2/sql?q=SELECT%20block,borocode,lot,lotarea,unitsres,unitstotal,%20%20%20%20%2F*%20id%3A3018260025%20*%2F%20%20%20%20st_x(st_centroid(the_geom))%20as%20lon,%20st_y(st_centroid(the_geom))%20as%20lat,%20%20%20%20the_geom,%20bbl%20AS%20id%20FROM%20dcp_mappluto%20WHERE%20bbl%20BETWEEN%20{i+1}000000000%20AND%20{i+1}999999999&format=geojson", payload)
    res = conn.getresponse()
    data = res.read()

    with open(f"{i+1}-data.json", 'w') as f:
        f.write(data.decode("utf-8"))