from neo4j.v1 import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "Wolf3105"))

def add_csv(tx):
    tx.run('LOAD CSV WITH HEADERS FROM "https://s3-eu-west-1.amazonaws.com/civicreactor1/180321CQC.csv" AS csvLine'
'MERGE (l:CQClocation {loc_id: csvLine.CQCLocationID, cqclocname: csvLine.Name, postcode: csvLine.Postcode})'
'MERGE (p:CQCprovider {prov_id: csvLine.CQCProviderID})'
'CREATE (l)-[:MANAGED_BY]->(p)')


with driver.session() as session:
    session.write_transaction(add_csv)
