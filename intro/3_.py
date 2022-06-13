import duckduckpy


for r in duckduckpy.query('Sausages').related_topics:
    print(r.first_url, ' - ', r.text)
